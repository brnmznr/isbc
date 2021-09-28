import asyncio
import iterm2


async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description = 'kubectx | kubens',
        detailed_description = 'Current context and namespace',
        exemplar = '⎈ context-xyz / namespace-abc',
        update_cadence = 5,
        identifier = 'ch.maze.iterm2-component.kubectx-kubens',
        knobs = [],
    )

    @iterm2.StatusBarRPC
    async def kubectx_kubens_coroutine(knobs):
        proc_ctx = await asyncio.create_subprocess_shell(
            '/bin/bash -l -c "kubectx -c"',
            stdout = asyncio.subprocess.PIPE,
            stderr = asyncio.subprocess.PIPE,
        )
        stdout_ctx, stderr_ctx = await proc_ctx.communicate()
        ctx =  stdout_ctx.decode().strip() if not stderr_ctx else 'CTX ERR'

        proc_ns = await asyncio.create_subprocess_shell(
            '/bin/bash -l -c "kubens -c"',
            stdout = asyncio.subprocess.PIPE,
            stderr = asyncio.subprocess.PIPE,
        )
        stdout_ns, stderr_ns = await proc_ns.communicate()
        ns =  stdout_ns.decode().strip() if not stderr_ns else 'NS ERR'

        return f'☸️ {ctx} / {ns}'

    await component.async_register(connection, kubectx_kubens_coroutine)

iterm2.run_forever(main)
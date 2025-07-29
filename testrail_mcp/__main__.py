"""Entry point for the TestRail MCP server when run as a module."""

import click
import sys
import asyncio

from testrail_mcp.mcp_server import TestRailMCPServer


@click.command()
@click.option(
    "--mode",
    "mode",
    default="stdio",
    show_default=True,
    help="mcp mode",
)
@click.option(
    "--host",
    "host",
    default="0.0.0.0",
    show_default=True,
    help="host",
)
@click.option(
    "--port",
    "port",
    default=9002,
    show_default=True,
    type=int,
    help="port",
)
def main(mode: str, host: str, port: int):
    """Run the TestRail MCP server."""
    print("Starting TestRail MCP server in stdio mode", file=sys.stderr)
    server = TestRailMCPServer()

    if mode == "http":
        asyncio.run(
            server.run(transport="http", host=host, port=port, path="/mcp")
        )
    else:
        asyncio.run(server.run_stdio_async())


if __name__ == "__main__":
    main()

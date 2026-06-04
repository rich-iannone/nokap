from __future__ import annotations

import sys
from pathlib import Path

import click

import nokap


@click.group(invoke_without_command=True)
@click.version_option(package_name="nokap", prog_name="nokap")
@click.pass_context
def cli(ctx: click.Context) -> None:
    """Screenshots and PDFs from web pages. Powered by headless Chrome."""
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())



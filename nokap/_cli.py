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


@cli.command()
@click.argument("url")
@click.argument("file", default="webshot.png")
@click.option("--vwidth", default=992, type=int, help="Viewport width in pixels.")
@click.option("--vheight", default=744, type=int, help="Viewport height in pixels.")
@click.option("--selector", "-s", default=None, help="CSS selector to capture.")
@click.option("--expand", "-e", default=0, type=int, help="Pixels to expand around selector.")
@click.option("--delay", "-d", default=0.2, type=float, help="Seconds to wait after page load.")
@click.option("--zoom", "-z", default=1.0, type=float, help="Zoom/scale factor.")
@click.option("--useragent", default=None, help="Custom User-Agent string.")
@click.option("--page-size", default="letter", help="Paper size for PDF (e.g., letter, a4).")
@click.option("--landscape", is_flag=True, help="Use landscape orientation for PDF.")
@click.option("--print-background", is_flag=True, help="Print CSS backgrounds in PDF.")
def webshot(
    url: str,
    file: str,
    vwidth: int,
    vheight: int,
    selector: str | None,
    expand: int,
    delay: float,
    zoom: float,
    useragent: str | None,
    page_size: str,
    landscape: bool,
    print_background: bool,
) -> None:
    """Take a screenshot or PDF of a URL or local file.

    URL can be an http/https URL or a local file path.
    FILE is the output path (default: webshot.png). Format is determined by
    extension: .png, .jpg, .webp for images; .pdf for PDF.
    """
    try:
        result = nokap.webshot(
            url,
            file,
            vwidth=vwidth,
            vheight=vheight,
            selector=selector,
            expand=expand,
            delay=delay,
            zoom=zoom,
            useragent=useragent,
            page_size=page_size,
            landscape=landscape,
            print_background=print_background,
        )
        click.echo(result)
    except nokap.NokapError as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)
    finally:
        nokap.close()



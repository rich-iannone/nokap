"""
Generate a matrix of GT table captures for visual verification.

Scans across:
- Format: PNG, PDF (full-page), PDF (element-bounded)
- Zoom: 1, 2, 3
- Expand (margin): 0, 5, 20

Output goes to _visual_check/ with descriptive filenames.
"""

from __future__ import annotations

import itertools
from pathlib import Path

import nokap

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "_visual_check"

# Parameters to scan
ZOOMS = [1, 2, 3]
PDF_ZOOMS = [1, 1.5, 2]  # Chrome PDF scale is limited to [0.1, 2.0]
EXPANDS = [0, 5, 20]

# A simple GT table rendered to HTML
GT_HTML: str | None = None


def _get_gt_html() -> str:
    global GT_HTML
    if GT_HTML is not None:
        return GT_HTML

    from great_tables import GT, exibble

    GT_HTML = GT(exibble.head(5)).as_raw_html(make_page=True, all_important=True)
    return GT_HTML


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    html = _get_gt_html()
    generated: list[Path] = []

    # --- PNG captures (element-bounded screenshots) ---
    for zoom, expand in itertools.product(ZOOMS, EXPANDS):
        name = f"png_zoom{zoom}_expand{expand}.png"
        out = OUTPUT_DIR / name
        print(f"  {name} ...", end=" ", flush=True)
        nokap.from_html(
            html, out, selector="table", zoom=zoom, expand=expand, delay=0.3
        )
        print(f"{out.stat().st_size / 1024:.1f} KB")
        generated.append(out)

    # --- PDF element-bounded captures ---
    for zoom, expand in itertools.product(PDF_ZOOMS, EXPANDS):
        name = f"pdf_element_zoom{zoom}_expand{expand}.pdf"
        out = OUTPUT_DIR / name
        print(f"  {name} ...", end=" ", flush=True)
        nokap.from_html(
            html,
            out,
            selector="table",
            zoom=zoom,
            expand=expand,
            delay=0.3,
        )
        print(f"{out.stat().st_size / 1024:.1f} KB")
        generated.append(out)

    # --- PDF full-page captures (varying zoom and page sizes) ---
    page_sizes = ["letter", "a4"]
    for zoom, page_size in itertools.product(PDF_ZOOMS, page_sizes):
        name = f"pdf_fullpage_zoom{zoom}_{page_size}.pdf"
        out = OUTPUT_DIR / name
        print(f"  {name} ...", end=" ", flush=True)
        nokap.from_html(
            html,
            out,
            zoom=zoom,
            delay=0.3,
            page_size=page_size,
            print_background=True,
        )
        print(f"{out.stat().st_size / 1024:.1f} KB")
        generated.append(out)

    nokap.close()

    print(f"\nGenerated {len(generated)} files in {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()

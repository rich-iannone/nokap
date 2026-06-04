from __future__ import annotations

import platform
import socket
import sys
from pathlib import Path
from urllib.parse import quote


def file_url(path: str | Path) -> str:
    """Convert a local file path to a file:/// URL."""
    p = Path(path).resolve()
    # On Windows, paths need forward slashes and a leading /
    if sys.platform == "win32":
        return "file:///" + quote(str(p).replace("\\", "/"), safe=":/")
    return "file://" + quote(str(p), safe="/:")



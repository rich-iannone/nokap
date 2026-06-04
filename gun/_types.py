from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

ImageFormat = Literal["png", "jpeg", "webp"]
PaperSize = Literal["letter", "legal", "tabloid", "ledger", "a0", "a1", "a2", "a3", "a4", "a5", "a6"]


# Paper dimensions in inches (width, height)
PAPER_SIZES: dict[str, tuple[float, float]] = {
    "letter": (8.5, 11),
    "legal": (8.5, 14),
    "tabloid": (11, 17),
    "ledger": (17, 11),
    "a0": (33.1, 46.8),
    "a1": (23.4, 33.1),
    "a2": (16.5, 23.4),
    "a3": (11.7, 16.5),
    "a4": (8.27, 11.7),
    "a5": (5.83, 8.27),
    "a6": (4.13, 5.83),
}



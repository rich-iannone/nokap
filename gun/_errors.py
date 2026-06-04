from __future__ import annotations

from typing import Any


class GunError(Exception):
    """Base exception for all gun errors."""


class ChromeNotFoundError(GunError):
    """Raised when Chrome/Chromium cannot be found on the system."""

    def __init__(self, message: str | None = None) -> None:
        super().__init__(
            message
            or (
                "Chrome/Chromium not found. Install Chrome or set the CHROME_PATH "
                "environment variable to the Chrome executable path."
            )
        )


class ChromeStartError(GunError):
    """Raised when Chrome fails to start or report its DevTools URL."""

    def __init__(self, message: str, stderr: str = "") -> None:
        detail = f"\nChrome stderr: {stderr[:500]}" if stderr else ""
        super().__init__(f"{message}{detail}")
        self.stderr = stderr


class ConnectionError_(GunError):
    """Raised when the CDP WebSocket connection fails or drops."""

    def __init__(self, message: str = "CDP WebSocket connection failed") -> None:
        super().__init__(message)


class NavigationError(GunError):
    """Raised when page navigation fails."""

    def __init__(self, url: str, reason: str = "") -> None:
        msg = f"Navigation failed for {url!r}"
        if reason:
            msg += f": {reason}"
        super().__init__(msg)
        self.url = url
        self.reason = reason


class PageLoadTimeout(GunError):
    """Raised when a page does not finish loading within the timeout."""

    def __init__(self, url: str, timeout: float) -> None:
        super().__init__(f"Page load timed out after {timeout}s: {url!r}")
        self.url = url
        self.timeout = timeout


class SelectorError(GunError):
    """Raised when a CSS selector matches no elements."""

    def __init__(self, selector: str) -> None:
        super().__init__(f"No element matches selector: {selector!r}")
        self.selector = selector


class CDPError(GunError):
    """Error returned by the Chrome DevTools Protocol."""

    def __init__(self, message: str, error_data: dict[str, Any] | None = None) -> None:
        super().__init__(message)
        self.error_data = error_data or {}

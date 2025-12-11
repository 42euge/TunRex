"""TUI applications for TunRex."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from textual.app import App

AVAILABLE_APPS: dict[str, str] = {
    "main": "The main TunRex TUI dashboard",
}


def get_app(name: str) -> type["App"] | None:
    """Get a TUI application class by name.

    Args:
        name: The name of the TUI app to retrieve.

    Returns:
        The App class if found, None otherwise.
    """
    if name == "main":
        from tunrex.tui.main import MainApp

        return MainApp
    return None

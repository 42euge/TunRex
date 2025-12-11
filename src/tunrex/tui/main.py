"""Main TUI application for TunRex."""

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer, Header, Static

from tunrex import __version__


class WelcomePanel(Static):
    """Welcome panel displayed on the main screen."""

    def compose(self) -> ComposeResult:
        yield Static(
            f"""
[bold cyan]TunRex[/bold cyan] v{__version__}

Welcome to TunRex - A flexible TUI/CLI toolkit.

[dim]Press [bold]q[/bold] to quit, [bold]?[/bold] for help[/dim]
""",
            id="welcome-content",
        )


class MainApp(App):
    """The main TunRex TUI application."""

    TITLE = "TunRex"
    SUB_TITLE = "A flexible TUI/CLI toolkit"

    CSS = """
    Screen {
        align: center middle;
    }

    WelcomePanel {
        width: 60;
        height: auto;
        border: solid $primary;
        padding: 1 2;
    }

    #welcome-content {
        text-align: center;
    }
    """

    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("?", "help", "Help"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield WelcomePanel()
        yield Footer()

    def action_help(self) -> None:
        """Show help information."""
        self.notify("Help: Press 'q' to quit", title="TunRex Help")

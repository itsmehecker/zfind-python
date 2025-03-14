from textual.app import App, ComposeResult
from textual.containers import Vertical, ScrollableContainer, Horizontal
from textual.widgets import Button, Static, Input
from rich import print
import pyperclip
import os
import re
import uuid

ZSH_HISTORY_PATH = os.path.expanduser("~/.zsh_history")

class ZshHistoryApp(App):
    CSS_PATH = "styles.tcss"

    def __init__(self):
        super().__init__()
        self.commands = self.load_history()

    def load_history(self):
        try:
            with open(ZSH_HISTORY_PATH, "r", encoding="utf-8") as file:
                lines = file.readlines()
                commands = [re.sub(r"^: \d+:\d+;", "", line.strip()) for line in lines]
                return list(dict.fromkeys(reversed(commands)))
        except FileNotFoundError:
            return ["[.zsh_history not found]"]

    def compose(self) -> ComposeResult:
        yield Vertical(
            Static("Zsh History Search", classes="header"),
            Static("Press 'q' to quit, 'c' to clear search", classes="header-shortcuts"),
            Static("Search:", classes="header"),
            Input(placeholder="Type to filter...", id="search", classes="input"),
            ScrollableContainer(id="command_list"),
            Static("Waiting for command...", id="status", classes="status"),
    )

    def on_mount(self) -> None:
        self.update_command_list(self.commands)

    def update_command_list(self, filtered_commands):
        container = self.query_one("#command_list", ScrollableContainer)
        filtered_commands = filtered_commands[:]
        container.remove_children(tuple(container.children))
        buttons = [Button(cmd, id=f"cmd_{uuid.uuid4()}") for cmd in filtered_commands]
        container.mount(*buttons)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        command = event.button.label
        pyperclip.copy(command)
        all_widgets = self.query("Static")
        print("All Static widgets:", [widget.id for widget in all_widgets if widget.id])
        try:
            status_widget = self.query_one("#status", Static)
            status_widget.update(f"Copied: {command}")
            print(f"Updated status widget: Copied '{command}'")
        except Exception as e:
            print("Error updating status widget:", e)

    def on_input_changed(self, event: Input.Changed) -> None:
        query = event.value.lower()
        filtered = [cmd for cmd in self.commands if query in cmd.lower()]
        self.update_command_list(filtered)

    BINDINGS = [
        ("q", "quit", "Quit the application"),
        ("c", "clear_search", "Clear the search input")
    ]

    def action_quit(self) -> None:
        self.exit()

    def action_clear_search(self) -> None:
        self.query_one("#search", Input).value = ""
        self.update_command_list(self.commands)

    def notify(self, message: str) -> None:
        print(f"[bold magenta]{message}[/bold magenta]")

if __name__ == "__main__":
    ZshHistoryApp().run()

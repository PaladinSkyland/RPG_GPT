from rich.markdown import Markdown
from rich.console import Group, Console
from rich.align import Align
from rich.rule import Rule
from rich.progress import Progress, BarColumn, MofNCompleteColumn
from rich.prompt import Prompt
from rich.table import Table
from rich.panel import Panel
import time
from threading import Thread

class CustomLiveable:
    def __init__(self):
        self.console = Console()
        self.console.clear()
        self.input = ''
        self.cursor = 0
        self.cursor_visible = True
        self.last_action = 0
        Thread(target=self.toggle_cursor, daemon=True).start()


    def __rich__(self):
        page = [""]
        page.append(Align.center("Fight time :fire:"))
        page.append(Rule())
        page.append(Align.center("Goblin attacked you dealing 10 damage!"))
        page.append("")
        
        group = []
        group.append("Player: (You)")
        progress = Progress("HP :yellow_heart:", BarColumn(), MofNCompleteColumn(), auto_refresh=False)
        progress.add_task("", completed=40, total=100)
        group.append(progress)
        group.append(":chart_increasing: Effects: :shield: :mushroom:")
        group.append("")
        
        group.append("Enemy: (Goblin)")
        progress = Progress("HP :yellow_heart:", BarColumn(), MofNCompleteColumn(), auto_refresh=False)
        progress.add_task("", completed=30, total=100)
        group.append(progress)
        group.append(":chart_increasing: Effects:")
        group.append("")

        grid = Table.grid(padding=(1, 5))
        grid.add_column(justify="left")
        grid.add_column(justify="left")
        grid.add_row(":white_large_square: > 1. :crossed_swords:  Attack", ":white_large_square: > 2. :shield:  Defend")
        grid.add_row(":white_large_square: > 3. :mushroom: Use item", ":white_large_square: > 4. :running: Run")
        group.append(Panel(grid, expand=False, title="Actions", title_align="left", padding=(1, 2)))
        group.append("")

        # input
        group.append(Align.center("[red]Invalid action entered![/red]"))
        cursor = f"[reverse]{self.input[self.cursor:self.cursor+1] or ' '}[/reverse]" if self.cursor_visible else self.input[self.cursor:self.cursor+1]
        input = self.input[:self.cursor] + cursor + self.input[self.cursor + 1:]
        group.append(f"Next action: {input}")

        page.append(Align.center(Group(*group)))
        return Align(Group(*page, fit=False), vertical="top", height=self.console.height)

    def key_pressed(self, key):
        if key == 'backspace':
            self.input = self.input[:max(self.cursor - 1, 0)] + self.input[self.cursor:]
            self.move_cursor(-1)
        elif key == 'delete':
            self.input = self.input[:self.cursor] + self.input[self.cursor + 1:]
        elif key == 'return':
            self.input = ''
            self.cursor = 0
        elif key == 'left':
            self.move_cursor(-1)
        elif key == 'right':
            self.move_cursor(1)
        elif len(key) == 1:
            self.input = self.input[:self.cursor] + key + self.input[self.cursor:]
            self.move_cursor(1)
        self.cursor_visible = True
        self.last_action = time.time()

    def move_cursor(self, value):
        self.cursor += value
        if self.cursor > len(self.input):
            self.cursor = len(self.input)
        if self.cursor < 0:
            self.cursor = 0

    def toggle_cursor(self):
        while True:
            now = time.time()
            if self.last_action + 0.5 < now:
                self.cursor_visible = not self.cursor_visible
                time.sleep(0.5)
            else:
                time.sleep(self.last_action + 0.5 - now)

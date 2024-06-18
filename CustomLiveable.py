from rich.console import Group, Console
from rich.align import Align
from rich.rule import Rule
from rich.progress import Progress, BarColumn, MofNCompleteColumn
from rich.table import Table
from rich.panel import Panel
import time
from threading import Thread
from rich.panel import Panel
from rich.box import MINIMAL

class CustomLiveable:
    def __init__(self, player):
        self.player = player
        self.enemy = None
        self.actions = []
        self.title = ""
        self.description = ""
        self.previous_action = None
        self.input = ''
        self.cursor_visible = True
        self.last_action = 0
        self.console = Console()
        self.console.clear()
        Thread(target=self.toggle_cursor, daemon=True).start()


    def __rich__(self):
        page = [""]
        page.append(Align.center(f"[bold]{self.title}[/bold]"))
        page.append(Rule())
        page.append(Align.center(self.description))
        
        group = []
        group.append(f"{self.player.name} (you)")
        progress = Progress("HP :yellow_heart:", BarColumn(bar_width=None), MofNCompleteColumn(), auto_refresh=False)
        progress.add_task("", completed=self.player.get_max_hp() - self.player.hp_loss, total=self.player.get_max_hp())
        group.append(progress)
        grid = Table(expand=True, box=None, show_header=False)
        grid.add_column(justify="left")
        grid.add_column(justify="left")
        grid.add_column(justify="left")
        grid.add_row(f":crossed_swords:  Attack: {self.player.get_attack()}", f"🛡️  Defense: {self.player.get_defense()}", f":chart_increasing: Effects:")
        grid.add_row(f":star: Level: {self.player.get_level()}", f":gem: XP: {self.player.get_exp()}", f":moneybag: Gold: {self.player.get_gold()}")
        group.append(grid)
        group.append("")

        if self.enemy:
            group.append(f"{self.enemy.name} (enemy)")
            progress = Progress("HP :yellow_heart:", BarColumn(bar_width=None), MofNCompleteColumn(), auto_refresh=False)
            progress.add_task("", completed=self.enemy.health, total=self.enemy.max_health)
            group.append(progress)
            grid = Table.grid(expand=True)
            grid.add_column(justify="left")
            grid.add_column(justify="left")
            grid.add_column(justify="left")
            grid.add_row(f":crossed_swords: Attack: {self.enemy.attack}", f"🛡️ Defense: {self.enemy.defense}", f":chart_increasing: Effects:")
            grid.add_row(f":gem: XP: {self.enemy.xp}", f":moneybag: Gold: {self.enemy.gold}", "")
            group.append(grid)
            group.append("")

        grid = Table.grid(padding=(1, 3), collapse_padding=True, expand=True)
        grid.add_column(justify="left", no_wrap=False, ratio=1, overflow="crop")
        grid.add_column(justify="left", no_wrap=False, ratio=1, overflow="crop")
        row = []
        for i, action in enumerate(self.actions):
            icon = ":white_large_square:" if self.input != str(i + 1) else ":white_check_mark:"
            row.append(f"{icon} {i + 1}. {action['icon']}  {action['title'].capitalize()}")
            if len(row) == 2:
                grid.add_row(*row)
                row = []
        if row:
            grid.add_row(*row)
        group.append(Panel(grid, expand=True, title="Actions", title_align="left", padding=(1, 2)))
        group.append("")

        # input
        if self.input.isnumeric() and int(self.input) in range(1, len(self.actions) + 1):
            action = self.actions[int(self.input) - 1]
            group.append(f"Next action: {self.input}. {action['icon']}  {action['title'].capitalize()}")
            group.append("")
            group.append(f"[dim]{action['description']}[/dim]")
        else:
            cursor = "[reverse] [/reverse]" if self.cursor_visible else ' '
            group.append(f"Next action: {self.input}{cursor}")

        page.append(Align.center(Panel(Group(*group), box=MINIMAL, width=max(60, self.console.width // 2))))
        return Align(Group(*page, fit=False), vertical="top", height=self.console.height)

    def key_pressed(self, key):
        if key == 'backspace' or key == 'delete':
            self.input = self.input[:-1]
        elif key == 'return':
            self.input = ''
        elif key == 'up':
            if not self.input.isnumeric():
                self.input = '1'
            else:
                self.input = str(((int(self.input) - 2) % len(self.actions) + 1))
        elif key == 'down':
            if not self.input.isnumeric():
                self.input = str(len(self.actions))
            else:
                self.input = str(int(self.input) % len(self.actions) + 1)
        elif len(key) == 1 and key.isdigit() and int(key) in range(1, len(self.actions) + 1):
            self.input = key
        self.cursor_visible = True
        self.last_action = time.time()

    def toggle_cursor(self):
        while True:
            now = time.time()
            if self.last_action + 0.5 < now:
                self.cursor_visible = not self.cursor_visible
                time.sleep(0.5)
            else:
                time.sleep(self.last_action + 0.5 - now)

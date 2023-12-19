import typer
from rich.table import Table
from rich.console import Console

console = Console()

app = typer.Typer()


@app.command(short_help="Adding an item")
def add(task: str, category: str):
    typer.echo(f"Adding { task }, { category }.")
    show()


@app.command(short_help="Deleting an item")
def delete(position: int):
    typer.echo(f"Deleting { position }.")
    show()


@app.command(short_help="Adding an item")
def update(position: int, task: str = None, category: str = None):
    typer.echo(f"Updating { position }.")
    show()


@app.command(short_help="Complete task")
def complete(position: int):
    typer.echo(f"Complete { position }.")
    show()


@app.command(short_help="Showing all To-Do")
def show():
    tasks = [("ToDo1", "Study"), ("ToDo2", "Sports")]
    console.print("[bold magenta]To-Dos[/bold magenta]!", "💻")

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("ToDo", min_width=20)
    table.add_column("Category", min_width=12, justify="right")
    table.add_column("Done", min_width=12, justify="right")


    def get_category_color(category):
        COLORS = {'Learn': 'cyan', 'YouTube': 'red', 'Sports': 'cyan', 'Study': 'green'}
        if category in COLORS: 
            return COLORS[category]
        return 'white'


    for index, task in enumerate(tasks, start=1):
        c = get_category_color(task[1])
        is_done_str = "✅" if True == 2 else "❌"
        table.add_row(str(index), task[0], f'[{c}]{task[1]}[/{c}]', is_done_str)

    console.print(table)


if __name__ == "__main__":
    app()

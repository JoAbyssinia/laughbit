from typing_extensions import Annotated
from typing import Optional
import requests
from rich.prompt import Prompt

import typer
from rich import print

app = typer.Typer()

# constant
URL = "https://v2.jokeapi.dev/joke"
blacklist = "nsfw,racist,religious"
categories = ["Any", "Misc", "Programming", "Dark", "Pun", "Spooky", "Christmas"]

__version__ = "0.1.0"

def version_callback(value: bool):
    if value:
        print(f"LaughBit: {__version__}")
        raise typer.Exit()

@app.command()
def laughBit(category: str = typer.Option(default="", help="categories like 'Any, Misc, Programming, Dark, Pun, Spooky, Christmas' (case insensitive)"),
             search: str = typer.Option(default="",help="search work like dog, cat..."),
             version: Annotated[
                 Optional[bool], typer.Option("--version", callback=version_callback)
             ] = None
             ):
    """
    optionally with --category to set the category of the joke.
    """
    if category and isinstance(category, str):
        if category.capitalize() in categories:
            url = f"{URL}/{category.replace(' ', '%20')}?blacklistFlags={blacklist}"
        else:
            print(f"[bold red]Category {category} is not a valid category.")
            print(f"use one of those categories is {categories}.")
            raise typer.Exit()
    else:
        url = f"{URL}/Any?blacklistFlags="+blacklist

    if search:
        url = f"{url}&contains={search}"

    joke = get_joke(url)
    custom_print(joke)

def get_joke(url: str) -> dict:

    response = requests.get(url)
    joke = response.json()

    return joke

def custom_print(joke: dict) -> None:
    category = joke["category"]
    ct = typer.style(category.capitalize(), fg=typer.colors.GREEN, bold=True)
    typer.echo("category: "+ct)
    joke_type = joke["type"]
    if joke_type =="single":
        jk = joke["joke"]
        print(jk)
    if joke_type =="twopart":
        typer.echo(typer.style("press enter to continue...", fg=typer.colors.GREEN))
        setup = joke["setup"]
        delivery = joke["delivery"]

        Prompt.ask(setup)
        print(delivery)


if __name__ == '__main__':
    app()
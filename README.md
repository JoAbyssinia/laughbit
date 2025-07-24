# LaughBit

LaughBit is a command-line application that fetches and displays jokes from the [JokeAPI](https://v2.jokeapi.dev/). It's a fun and easy way to get a quick laugh right in your terminal.

## Installation

You can install LaughBit directly from PyPI using pip:

```bash
pip install laughbit
```

## Usage

Once installed, you can use the `laughbit` command to get a random joke:

```bash
laughbit
```

### Get a joke from a specific category

You can also specify a category to get a joke from. The available categories are:

*   Any
*   Misc
*   Programming
*   Dark
*   Pun
*   Spooky
*   Christmas

To get a joke from a specific category, use the `--category` option:

```bash
laughbit --category Programming
```

### Search for a joke

You can also search for a joke containing a specific word or phrase using the `--search` option:

```bash
laughbit --search "dog"
```

## Sample Output

Here's an example of what you might see when you run `laughbit`:

```
category: Dark
Why did the invisible man turn down the job offer?
He couldn't see himself doing it.
```

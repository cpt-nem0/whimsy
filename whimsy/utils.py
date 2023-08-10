"""Utility functions for the whimsy CLI."""

import json
import os


def create_directory_if_not_exists(directory) -> None:
    """Create a directory if it doesn't exist.

    Args:
        directory: The directory to create.
    """

    if not os.path.exists(directory):
        os.mkdir(directory)


def save_credentials_to_file(credentials, filename) -> None:
    """Save the credentials to a file.

    Args:
        credentials: The credentials to save.
        filename: The filename to save the credentials to.
    """

    with open(filename, "w") as f:
        json.dump(credentials, f)


def load_credentials_from_file(filename) -> dict | None:
    """Load the credentials from a file.

    Args:
        filename: The filename to load the credentials from.

    Returns:
        The credentials if the file exists, None otherwise.
    """

    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None


def color_print(
    message: str,
    color: str,
    attrs: list[str] = None,
    **kwargs,
) -> None:
    """Prints a message in the provided color on the terminal.

    Args:
      message: The message to print.
      color: The color to print the message in.
    """
    attrs = attrs or []

    fixed_colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
    }

    fixed_attrs = {
        "bold": "\033[1m",
        "underline": "\033[4m",
        "italic": "\033[3m",
    }

    applied_attrs = ""
    for attr in attrs:
        if attr not in attrs:
            raise ValueError("Invalid attribute: " + attr)
        applied_attrs += fixed_attrs[attr]

    if color not in fixed_colors:
        raise ValueError("Invalid color: " + color)

    print(applied_attrs + fixed_colors[color] + message + "\033[0m", **kwargs)

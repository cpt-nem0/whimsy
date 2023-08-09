"""CLI class to handle stdin/stdout and command line arguments."""

import argparse
import importlib.metadata
import sys


class CLI:
    """CLI class to handle stdin/stdout and command line arguments. also have some functions to handle the commands.
    with argparse to handle the command line arguments.
    """

    def __init__(self):
        """Initiate the CLI class with the parser and the arguments."""
        self.parser = argparse.ArgumentParser(
            description="Bard CLI - Ask me a question and I'll answer you."
        )
        self.parser.add_argument(
            "-v",
            "--version",
            action="version",
            version="%(prog)s (version {version})".format(
                version=importlib.metadata.version("bard_cli")
            ),
        )
        self.parser.add_argument(
            "-p",
            "--prompt",
            metavar="prompt",
            type=str,
            nargs="?",
            help="Prompt for Bard.",
        )
        self.parser.add_argument(
            "-i",
            "--system",
            action="store_true",
            help="Include system info in the question.",
        )
        self.parser.add_argument(
            "-c",
            "--cwd",
            action="store_true",
            help="Include current working directory in the question.",
        )
        self.parser.add_argument(
            "-s",
            "--show",
            action="store_true",
            default=False,
            help="Show the final prompt before sending it.",
        )

    def get_args(self):
        """Get the arguments from the command line and return it as a string."""
        return self.parser.parse_args()

    def print_error(self, error):
        """Print the error to stderr."""
        print(error, file=sys.stderr)

    def print_help(self):
        """Print the help to stdout."""
        print(self.parser.format_help())

    def print_answer(self, answer):
        """Print the answer to stdout."""
        print(answer)

    def print_prompt(self, prompt):
        """Print the prompt to stdout."""
        print(prompt)

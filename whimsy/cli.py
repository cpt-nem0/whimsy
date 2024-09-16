"""CLI class to handle stdin/stdout and command line arguments."""

import argparse
import importlib.metadata
import sys

from .utils import color_print


class CLI:
    """
    A command-line interface class for handling user input/output and parsing command-line arguments.

    Uses argparse for argument parsing and includes various helper methods for printing
    errors, prompts, and handling piped stdin input.
    """

    def __init__(self):
        """Initiate the CLI class with the parser and the arguments."""
        self.parser = argparse.ArgumentParser(
            description="Whimsy - Ask me a question and I'll answer you."
        )
        self._add_arguments()

    def _add_arguments(self):
        self.parser.add_argument(
            "prompt",
            type=str,
            nargs="?",
            help="Prompt for llm.",
        )
        self.parser.add_argument(
            "-v",
            "--version",
            action="version",
            version="%(prog)s (version {version})".format(
                version=importlib.metadata.version("whimsy")
            ),
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
            "-t",
            "--cwd-tree",
            action="store_true",
            help="Include current working directory tree in the question.",
        )
        self.parser.add_argument(
            "-o",
            "--stdin",
            action="store_true",
            help="Include the output from last ran command",
        )

    def get_args(self):
        """Get the arguments from the command line and return it as a string."""
        args = self.parser.parse_args()

        if len(sys.argv) == 1:
            self.print_help()
            sys.exit(0)

        if not args.prompt:
            self.print_error("Prompt is required to ask question.")
            self.print_help()
            sys.exit(1)

        return args

    def get_stdin(self):
        """Get stdin from the from any terminla command piped to whimsy."""

        # check if stdin is provided
        if not sys.stdin.isatty():
            stdin = sys.stdin.read()
        else:
            stdin = ""

        return stdin

    def print_error(self, error):
        """Print the error to stderr."""
        color_print(error, color="red", file=sys.stderr)

    def print_help(self):
        """Print the help to stdout."""
        color_print(self.parser.format_help(), color="yellow")

    def print_answer(self, answer: str):
        """Print the answer to stdout."""
        color_print(f"Answer:\n{answer}", color="green")

    def print_prompt(self, prompt: str):
        """Print the prompt to stdout."""
        color_print(f"Prompt:\n{prompt}", color="blue", attrs=["bold"])

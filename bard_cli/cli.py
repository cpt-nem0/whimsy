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
            "question",
            metavar="question",
            type=str,
            nargs="?",
            help="Question to ask the Bard.",
        )
        self.parser.add_argument(
            "-s",
            "--system",
            action="store_true",
            help="Include system info in the question.",
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

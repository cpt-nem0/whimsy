from .bard import BardClient
from .cli import CLI


def main():
    bard = BardClient()
    cli = CLI()

    args = cli.get_args()

    if args.question:
        answer = bard.ask(args.question)
        cli.print_answer(answer["content"])
    else:
        cli.print_help()

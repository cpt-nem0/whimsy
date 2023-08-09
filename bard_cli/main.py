from .bard import BardClient
from .cli import CLI
from .prompt import Prompt


def main():
    """The main function which is called when the CLI is executed."""
    cli = CLI()
    args = cli.get_args()

    if args.prompt:
        prompt = Prompt(
            args.prompt,
            options={
                "system": args.system,
                "cwd": args.cwd,
                "cwd_tree": args.cwd_tree,
            },
        )
        cli.print_prompt(prompt.get_prompt())
        return

    if args.show:
        cli.print_prompt(args.question)

    bard_client = BardClient()
    answer = bard_client.get_answer(args.question)
    cli.print_answer(answer)


if __name__ == "__main__":
    main()

from .bard import BardClient
from .cli import CLI
from .prompt import Prompt


def main():
    """The main function which is called when the CLI is executed."""
    cli = CLI()
    args = cli.get_args()

    if not args.prompt:
        cli.print_error("No prompt provided.")
        exit(1)

    prompt = Prompt(
        args.prompt,
        stdin=cli.get_stdin(),
        options={
            "system": args.system,
            "cwd": args.cwd,
            "cwd-tree": args.cwd_tree,
        },
    )

    if args.show:
        cli.print_prompt(prompt.get_prompt())

    bard_client = BardClient()
    answer = bard_client.get_answer(args.prompt)
    cli.print_answer(answer)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        exit(0)

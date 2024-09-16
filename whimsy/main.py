from .backends.gemini import GeminiClient
from .cli import CLI
from .config import get_gemini_credentials
from .prompt import Prompt


def main():
    """The main function which is called when the CLI is executed."""
    cli = CLI()
    args = cli.get_args()

    prompt = Prompt(
        args.prompt,
        stdin=cli.get_stdin() if args.stdin else "",
        options={
            "system": args.system,
            "cwd": args.cwd,
            "cwd-tree": args.cwd_tree,
        },
    )

    cli.print_prompt(prompt.get_prompt())

    gemini_creds = get_gemini_credentials()

    gemini_client = GeminiClient(
        api_key=gemini_creds.api_key, model_name=gemini_creds.llm_model
    )
    gemini_client.initialize()
    answer = gemini_client.get_answer(prompt.get_prompt())
    cli.print_answer(answer)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        exit(0)

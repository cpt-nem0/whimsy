"""This module contains the Prompt class which is used to create a prompt for the CLI."""

import os


class Prompt:
    """The Prompt class which is used to create a prompt for the CLI."""

    def __init__(self, prompt: str, options: dict = None):
        """Initiate the Prompt class with the prompt."""
        self.prompt = prompt
        self.options = options or {}

    def _get_system_info(self):
        """get the system info using the neofetch command"""

        return os.popen("neofetch --stdout").read()

    def _get_cwd(self):
        """get the current working directory"""

        return os.getcwd()

    def _get_cwd_tree(self):
        """get the tree of the current working directory"""

        return os.popen("tree").read()

    def update_prompt(self):
        """Update the prompt with the system info and the cwd"""

        if self.options.get("system"):
            self.prompt += f"\nSystem Info: \n {self._get_system_info()}"

        if self.options.get("cwd"):
            self.prompt += f"\nCurrent Working Directory: \n {self._get_cwd()}"

        if self.options.get("cwd_tree"):
            self.prompt += (
                f"\nCurrent Working Directory Tree structure: \n {self._get_cwd_tree()}"
            )

    def get_prompt(self):
        """Get the prompt."""
        self.update_prompt()

        return self.prompt

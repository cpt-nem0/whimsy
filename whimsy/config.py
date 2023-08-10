"""Configuration file for whimsy.

This file contains functions for loading and updating the whimsy configuration file.
"""


import json
import os

from .utils import create_directory_if_not_exists, load_credentials_from_file

CONFIG_DIRECTORY = os.path.expanduser("~/.config/whimsy")
create_directory_if_not_exists(CONFIG_DIRECTORY)


def load_config_file() -> dict:
    """Load the whimsy configuration file.

    Returns:
        The whimsy configuration file.
    """
    whimsy_cli_config = load_credentials_from_file(
        os.path.join(CONFIG_DIRECTORY, "config.json")
    )
    if whimsy_cli_config is None:
        return {}

    return whimsy_cli_config


def update_config_file(config: dict) -> None:
    """Update the whimsy configuration file.

    Args:
        config: The configuration to update the whimsy configuration file with.
    """

    with open(
        os.path.join(CONFIG_DIRECTORY, "config.json"),
        "w",
    ) as f:
        json.dump(config, f)


def _get_bard_token() -> str:
    """Get the bard token from the whimsy configuration file.

    Returns:
        The bard token.
    """
    config = load_config_file()
    if "bard-token" in config:
        return config["bard-token"]

    token = input(
        "Enter your Bard token (can be found in the site cookies under `__Secure-1PSID` key): "
    )
    config["bard-token"] = token
    update_config_file(config)

    return token


BARD_TOKEN = _get_bard_token()

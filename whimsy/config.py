"""Configuration file for whimsy.

This file contains functions for loading and updating the whimsy configuration file.
"""

import json
import os

from .models import GeminiConfig
from .utils import (
    create_directory_if_not_exists,
    get_user_choice_from_list,
    load_credentials_from_file,
)

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


def get_gemini_credentials() -> GeminiConfig:
    from .backends.gemini import GeminiClient

    config = load_config_file()
    if "gemini" in config:
        return GeminiConfig(**config["gemini"])

    api_key = input("Enter you Gemini API key (for help: https://ai.google.dev/):")

    model_options = GeminiClient.available_models()
    model_name = get_user_choice_from_list("Select model:", model_options)

    gemini_config = GeminiConfig(api_key=api_key, llm_model=model_name)

    config["gemini"] = dict(gemini_config)

    update_config_file(config)

    return gemini_config

import json
import os

from .utils import create_directory_if_not_exists, load_credentials_from_file

CONFIG_DIRECTORY = os.path.expanduser("~/.bard-cli")
create_directory_if_not_exists(CONFIG_DIRECTORY)


def load_config_file():
    oh_py_god_config = load_credentials_from_file(
        os.path.join(CONFIG_DIRECTORY, "config.json")
    )
    if oh_py_god_config is None:
        return {}

    return oh_py_god_config


def update_config_file(config):
    with open(
        os.path.join(CONFIG_DIRECTORY, "config.json"),
        "w",
    ) as f:
        json.dump(config, f)


def _get_bard_token():
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

import json
import os


def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)


def save_credentials_to_file(credentials, filename):
    with open(filename, "w") as f:
        json.dump(credentials, f)


def load_credentials_from_file(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

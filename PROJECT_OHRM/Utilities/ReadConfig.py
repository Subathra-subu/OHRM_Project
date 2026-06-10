from configparser import ConfigParser
import os


def get_config(category, key):

    config = ConfigParser()

    base_path = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    config_path = os.path.join(
        base_path,
        "Configuration",
        "config.ini"
    )

    config.read(config_path)

    return config.get(category, key)
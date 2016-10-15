"""Module to work with execution configuration file."""
import logging
import argparse

from settings import Settings
from default import DefaultScenario


def create_config(config_path):
    """
    Create configuration file.

    :param config_path: Path for new configuation file.
    """
    config = DefaultScenario()
    config.create_config()
    config.settings.write_config(config_path)


def parse_config(config_path):
    """
    Obtain config from configuration file.

    :param config_path: Path of the configuation file.

    :returns: The config object.
    """
    config = Settings()
    config.load_config(config_path)
    return config


def _parse_args():
    """
    Parse commandline arguments.

    :returns: Instance of :class:`argparse.Namespace`.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--config_path", dest="config_path", type=str, required=True,
        help="Path to new configuration file."
        )
    return parser.parse_args()


def _create_new_config():
    """Method for create new configuration file."""
    formatter = logging.Formatter(
        "%(asctime)s:%(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(console_handler)

    settings_logger = logging.getLogger("settings")
    settings_logger.setLevel(logging.INFO)
    settings_logger.addHandler(console_handler)

    args = _parse_args()
    create_config(args.config_path)

if __name__ == "__main__":
    _create_new_config()

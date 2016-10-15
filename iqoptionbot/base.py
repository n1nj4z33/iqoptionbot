"""Module for base configuration."""
from iqoptionbot.settings import Settings


class BaseScenario(object):
    """Class to prepare base configuration."""
    # pylint: disable=too-few-public-methods

    def __init__(self):
        self.settings = Settings()

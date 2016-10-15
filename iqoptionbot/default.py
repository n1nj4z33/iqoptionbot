"""Module for default scenario configuration."""
from base import BaseScenario


class DefaultScenario(BaseScenario):
    """Class to prepare default configuration."""
    # pylint: disable=too-few-public-methods

    # def __init__(self):
    #     super(DefaultScenario, self).__init__()

    def _prepare_connection_settings(self):
        """Prepare connection settings configuration section."""
        self.settings.set_connection_hostname("hostname")
        self.settings.set_connection_username("username")
        self.settings.set_connection_password("password")

    def _prepare_trade_settings(self):
        """Prepare trade settings configuration section."""
        self.settings.set_trade_actives(["actives"])
        self.settings.set_trade_patterns(["patterns"])

    def create_config(self):
        """Create default configuration."""
        self._prepare_connection_settings()
        self._prepare_trade_settings()

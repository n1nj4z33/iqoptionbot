"""Module for configuration settings."""
import json
import logging

import constants as config_constants


class Settings(object):
    """Class for configuration settings."""
    # pylint: disable=too-many-public-methods

    def __init__(self):
        self.__config_data = {}

    @property
    def config_data(self):
        """Property to get configuration data.

        :returns: The configuration data dictionary.
        """
        return self.__config_data

    @property
    def _connection_settings(self):
        """Property to get connection settings.

        :returns: The connection settings dictionary.
        """
        return self.__config_data.setdefault(config_constants.CONNECTION_SETTINGS_KEY, {})

    def set_connection_hostname(self, connection_hostname):
        """Set connection hostname.

        :param connection_hostname: The connection hostname.
        """
        self._connection_settings[config_constants.CONNECTION_HOSTNAME_KEY] = connection_hostname

    def get_connection_hostname(self):
        """Get connection hostname.

        :returns: The connection hostname.
        """
        return self._connection_settings[config_constants.CONNECTION_HOSTNAME_KEY]

    def set_connection_username(self, connection_username):
        """Set connection username.

        :param connection_username: The connection username.
        """
        self._connection_settings[config_constants.CONNECTION_USERNAME_KEY] = connection_username

    def get_connection_username(self):
        """Get connection username.

        :returns: The connection username.
        """
        return self._connection_settings[config_constants.CONNECTION_USERNAME_KEY]

    def set_connection_password(self, connection_password):
        """Set connection password.

        :param connection_password: The connection password.
        """
        self._connection_settings[config_constants.CONNECTION_PASSWORD_KEY] = connection_password

    def get_connection_password(self):
        """Get connection password.

        :returns: The connection password.
        """
        return self._connection_settings[config_constants.CONNECTION_PASSWORD_KEY]

    @property
    def _trade_settings(self):
        """Property to get trade settings.

        :returns: The trade settings dictionary.
        """
        return self.__config_data.setdefault(config_constants.TRADE_SETTINGS_KEY, {})

    def set_trade_actives(self, trade_actives):
        """Set trade actives.

        :param trade_actives: The list of trade actives.
        """
        self._trade_settings[config_constants.TRADE_ACTIVES_KEY] = trade_actives

    def get_trade_actives(self):
        """Get trade actives.

        :returns: The list of trade actives.
        """
        return self._trade_settings[config_constants.TRADE_ACTIVES_KEY]

    def set_trade_patterns(self, trade_patterns):
        """Set trade patterns.

        :param trade_patterns: The list of trade patterns.
        """
        self._trade_settings[config_constants.TRADE_PATTERNS_KEY] = trade_patterns

    def get_trade_patterns(self):
        """Get trade patterns.

        :returns: The list of trade patterns.
        """
        return self._trade_settings[config_constants.TRADE_PATTERNS_KEY]

    def write_config(self, config_path):
        """Write configuration to file.

        :param config_path: The path to config file.
        """
        logger = logging.getLogger(__name__)
        logger.info("Create a new configuration file '%s'.", config_path)
        with open(config_path, "wb") as config_file:
            json.dump(self.__config_data, config_file, indent=4, sort_keys=True)

    def load_config(self, config_path):
        """Create configuration object from file.

        :param config_path: The path to configuration file.
        """
        logger = logging.getLogger(__name__)
        logger.info("Load configuration from file '%s'.", config_path)
        with open(config_path, "rb") as config_file:
            self.__config_data = json.load(config_file)

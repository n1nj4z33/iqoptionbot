"""Module for IQ Option API starter."""

import os
import argparse
import logging

from iqoptionapi.api import IQOptionAPI
from config import parse_config
from signaler import create_signaler
from trader import create_trader


class Starter(object):
    """Calss for IQ Option API starter."""

    def __init__(self, config):
        """
        :param config: The instance of :class:`Settings
            <iqoptionpy.settings.settigns.Settings>`.
        """
        self.config = config
        self.api = IQOptionAPI(
            self.config.get_connection_hostname(),
            self.config.get_connection_username(),
            self.config.get_connection_password()
            )

    def create_connection(self):
        """Method for create connection to IQ Option API."""
        logger = logging.getLogger(__name__)
        logger.info("Create connection.")
        self.api.connect()
        logger.info("Successfully connected.")

    def start_signalers(self, actives):
        """Method for start signalers."""
        logger = logging.getLogger(__name__)
        logger.info("Create signalers.")
        signalers = []
        actives = self.config.get_trade_actives()
        patterns = self.config.get_trade_patterns()
        for active in actives:
            signaler = create_signaler(self.api, active)
            signaler.set_patterns(patterns)
            signaler.start()
            signalers.append(signaler)
        return signalers

    def start_traders(self, actives):
        """Method for start traders."""
        logger = logging.getLogger(__name__)
        logger.info("Create traders.")
        traders = []
        actives = self.config.get_trade_actives()
        for active in actives:
            trader = create_trader(self.api, active)
            trader.start()
            traders.append(trader)
        return traders

def _prepare_logging():
    """Prepare logging for starter."""
    formatter = logging.Formatter(
        "%(asctime)s:%(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    logs_folder = "logs"
    if not os.path.exists(logs_folder):
        os.makedirs(logs_folder)

    starter_logger = logging.getLogger(__name__)
    starter_logger.setLevel(logging.INFO)

    starter_file_handler = logging.FileHandler(os.path.join(logs_folder, "starter.log"))
    starter_file_handler.setLevel(logging.DEBUG)
    starter_file_handler.setFormatter(formatter)

    starter_logger.addHandler(console_handler)
    starter_logger.addHandler(starter_file_handler)

    api_logger = logging.getLogger("iqoptionapi")

    api_file_handler = logging.FileHandler(os.path.join(logs_folder, "iqapi.log"))
    api_file_handler.setLevel(logging.DEBUG)
    api_file_handler.setFormatter(formatter)

    api_logger.addHandler(console_handler)
    api_logger.addHandler(api_file_handler)

    signaler_logger = logging.getLogger("signaler")
    signaler_logger.setLevel(logging.INFO)

    signaler_file_handler = logging.FileHandler(os.path.join(logs_folder, "signaler.log"))
    signaler_file_handler.setLevel(logging.DEBUG)
    signaler_file_handler.setFormatter(formatter)

    signaler_logger.addHandler(console_handler)
    signaler_logger.addHandler(signaler_file_handler)

    trader_logger = logging.getLogger("trader")
    trader_logger.setLevel(logging.INFO)

    trader_file_handler = logging.FileHandler(os.path.join(logs_folder, "trader.log"))
    trader_file_handler.setLevel(logging.DEBUG)
    trader_file_handler.setFormatter(formatter)

    trader_logger.addHandler(console_handler)
    trader_logger.addHandler(trader_file_handler)

    websocket_logger = logging.getLogger("websocket")

    websocket_file_handler = logging.FileHandler(os.path.join(logs_folder, "websocket.log"))
    websocket_file_handler.setLevel(logging.DEBUG)
    websocket_file_handler.setFormatter(formatter)

    websocket_logger.addHandler(console_handler)
    websocket_logger.addHandler(websocket_file_handler)


def _create_starter(config):
    """Create IQ Option API starter.

    :param config: The instance of :class:`ConfigurationSettings
        <iqpy.configuration.settigns.ConfigurationSettings>`.

    :returns: Instance of :class:`Starter <iqpy.starter.Starter>`.
    """
    return Starter(config)


def start():
    """Main method for start."""
    _prepare_logging()
    args = _parse_args()
    config = parse_config(args.config_path)
    starter = _create_starter(config)
    starter.create_connection()
    signalers = starter.start_signalers(["EURUSD-OTC"])
    traders = starter.start_traders(["EURUSD-OTC"])

    while True:
        for signaler in signalers:
            signal = signaler.get_signal()

            if signal:

                for trader in traders:
                    if signaler.active == trader.active:
                        trader.trade(signal)


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


if __name__ == "__main__":
    start()

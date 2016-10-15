"""Module for IQ Option API trader."""

import logging
import iqoptionapi.constants as api_constants


class Trader(object):
    """Calss for IQ Option API trader."""

    def __init__(self, api, active):
        self.api = api
        self.active = active

    def start(self):
        """Method for start trader."""
        logger = logging.getLogger(__name__)

        self.api.timesync.expiration_time = 1

        logger.info("Trader for active '%s' started.", self.active)

        logger.info("Trader for active '%s' wait for signal.", self.active)

    def trade(self, signal):
        """Method for trade."""
        logger = logging.getLogger(__name__)
        logger.info("Trader for active '%s' recived signal '%s'.", self.active, signal.direction)

        self.api.buy(
            signal.price,
            api_constants.ACTIVES[self.active],
            signal.option,
            signal.direction)

        logger.info("Trader for active '%s' successfully buy in direction '%s'.",
                    self.active, signal.direction)

        import time
        time.sleep(3)


def create_trader(api, active):
    """Method for create trader.

    :param api: The IQ Option API.
    :param active: The trader active.
    """
    logger = logging.getLogger(__name__)
    logger.info("Create trader for active '%s'.", active)
    return Trader(api, active)

# -*- coding: utf-8 -*-
"""Module for IQ Option API signaler."""
import logging

import iqpy.iqapi.constants as api_constants
from iqpy.signaler.signal import Signal


class Signaler(object):
    """Calss for  IQ Option API signaler."""

    def __init__(self, api, active):
        self.api = api
        self.active = active
        self.patterns = None

    def start(self):
        """Method for start trading."""
        logger = logging.getLogger(__name__)

        self.api.setactives([api_constants.ACTIVES[self.active]])

        logger.info("Signaler for active '%s' started.", self.active)
        logger = logging.getLogger(__name__)
        for pattern in self.patterns:
            logger.info("Signaler for active '%s' wait for pattern '%s'.",
                        self.active, pattern.name)

    def set_patterns(self, patterns):
        """Method for set patterns.

        :param patterns: The list of patters to wait signal.
        """
        self.patterns = patterns


    def get_signal(self):
        """Get signal from patterns.

        :returns: The instance of :class:`Signal <signaler.signal.Signal>`.
        """
        logger = logging.getLogger(__name__)

        for pattern in self.patterns:
            if pattern.call():
                logger.info("Signaler for active '%s' recived pattern '%s' in direction 'call'.",
                            self.active, pattern.name)
                return Signal("call", 10, api_constants.ACTIVES[self.active], "turbo")
            if pattern.put():
                logger.info("Signaler for active '%s' recived pattern '%s' in direction 'put'.",
                            self.active, pattern.name)
                return Signal("put", 10, api_constants.ACTIVES[self.active], "turbo")


def create_signaler(api, active):
    """Method for create signaler.

    :param api: The IQ Option API.
    :param active: The signaler active.
    """
    logger = logging.getLogger(__name__)
    logger.info("Create signaler for active '%s'.", active)
    return Signaler(api, active)

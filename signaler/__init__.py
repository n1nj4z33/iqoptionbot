# -*- coding: utf-8 -*-
"""Module for IQ Option API signaler."""

import logging


def _prepare_logging():
    """Prepare logger for module IQ Option API signaler."""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.NullHandler())

_prepare_logging()

# -*- coding: utf-8 -*-
"""Module for IQ Option API signal."""


class Signal(object):
    """Class for IQ Option API signal."""
    def __init__(self, direction, price, active, option):
        self.direction = direction
        self.price = price
        self.active = active
        self.option = option

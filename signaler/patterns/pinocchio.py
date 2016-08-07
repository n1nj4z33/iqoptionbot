# -*- coding: utf-8 -*-
"""Module for IQ Option API pinocchio bars pattern."""

import time

from signaler.patterns.base import Base


class Pinocchio(Base):
    """Class for pinocchio bars pattern."""
    def __init__(self, api):
        super(Pinocchio, self).__init__(api)
        self.name = "Pinocchio"

    def call(self):
        if self.api.timesync.server_datetime.second == 0:
            
            self.api.getcandles(76, 60)


            time.sleep(0.5)

            candles = self.api.candles

            if candles.first_candle.candle_type == "green":
                return True

    def put(self):
        if self.api.timesync.server_datetime.second == 0:
            
            self.api.getcandles(76, 60)

            time.sleep(0.5)

            candles = self.api.candles

            if candles.first_candle.candle_type == "red":
                return True

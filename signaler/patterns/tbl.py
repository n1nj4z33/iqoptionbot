# -*- coding: utf-8 -*-
"""Module for IQ Option API TBL pattern."""

import time

from signaler.patterns.base import Base


class TBL(Base):
    """Class for TBH pattern."""
    def __init__(self, api):
        super(TBL, self).__init__(api)
        self.name = "TBL"

    def call(self):
        if self.api.timesync.server_datetime.second == 0:
            
            self.api.getcandles(76, 60)

            time.sleep(0.5)

            candles = self.api.candles

            if candles.first_candle.candle_low == candles.second_candle.candle_low:

                if candles.current_candle.candle_low > candles.second_candle.candle_low:
                    return True

    def put(self):
        if self.api.timesync.server_datetime.second == 0:
            
            self.api.getcandles(76, 60)

            time.sleep(0.5)

            candles = self.api.candles

            if candles.first_candle.candle_low == candles.second_candle.candle_low:

                if candles.current_candle.candle_low < candles.second_candle.candle_low:
                    return True
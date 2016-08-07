# -*- coding: utf-8 -*-
"""Module for IQ Option API DBLHC pattern."""

import time

from signaler.patterns.base import Base


class DBLHC(Base):
    """Class for DBLHC pattern."""
    def __init__(self, api):
        super(DBLHC, self).__init__(api)
        self.name = "DBLHC (Бычий сетап)"

    def call(self):
        if self.api.timesync.server_datetime.second == 0:
            
            self.api.getcandles(76, 60)

            time.sleep(0.5)

            candles = self.api.candles

            if candles.first_candle.candle_low == candles.second_candle.candle_low:

                if candles.second_candle.candle_close > candles.first_candle.candle_low:
                    return True

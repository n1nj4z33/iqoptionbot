"""Module for IQ Option API TBH pattern."""

from base import Base


class TBH(Base):
    """Class for TBH pattern."""

    def __init__(self, api):
        """
        :param api: The instance of
            :class:`IQOptionAPI <iqoptionapi.api.IQOptionAPI>`.
        """
        super(TBH, self).__init__(api)
        self.name = "TBH"

    def call(self):
        """Method to check call pattern."""
        if self.candles:
            if self.candles.first_candle.candle_high == self.candles.second_candle.candle_high:
                if self.candles.current_candle.candle_high > self.candles.second_candle.candle_high:
                    return True

    def put(self):
        """Method to check put pattern."""
        if self.candles:
            if self.candles.first_candle.candle_high == self.candles.second_candle.candle_high:
                if self.candles.current_candle.candle_low < self.candles.second_candle.candle_low:
                    return True

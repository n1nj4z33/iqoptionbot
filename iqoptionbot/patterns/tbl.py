"""Module for IQ Option API TBL pattern."""

from base import Base


class TBL(Base):
    """Class for TBH pattern."""

    def __init__(self, api):
        """
        :param api: The instance of
            :class:`IQOptionAPI <iqoptionapi.api.IQOptionAPI>`.
        """
        super(TBL, self).__init__(api)
        self.name = "TBL"

    def call(self):
        """Method to check call pattern."""
        if self.candles.first_candle.candle_low == self.candles.second_candle.candle_low:
            if self.candles.current_candle.candle_low > self.candles.second_candle.candle_low:
                return True

    def put(self):
        """Method to check put pattern."""
        if self.candles.first_candle.candle_low == self.candles.second_candle.candle_low:
            if self.candles.current_candle.candle_low < self.candles.second_candle.candle_low:
                return True

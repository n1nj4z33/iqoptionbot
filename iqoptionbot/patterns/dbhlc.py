"""Module for IQ Option API DBHLC pattern."""

from base import Base


class DBHLC(Base):
    """Class for DBLHC pattern."""
    # pylint: disable=too-few-public-methods

    def __init__(self, api):
        """
        :param api: The instance of
            :class:`IQOptionAPI <iqoptionapi.api.IQOptionAPI>`.
        """
        super(DBHLC, self).__init__(api)
        self.name = "DBHLC"

    def put(self):
        """Method to check put pattern."""
        if self.candles.first_candle.candle_high == self.candles.second_candle.candle_high:
            if self.candles.second_candle.candle_close < self.candles.first_candle.candle_low:
                return True

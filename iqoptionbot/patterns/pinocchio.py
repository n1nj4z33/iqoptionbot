"""Module for IQ Option API pinocchio bars pattern."""
from base import Base


class Pinocchio(Base):
    """Class for pinocchio bars pattern."""

    def __init__(self, api):
        """
        :param api: The instance of
            :class:`IQOptionAPI <iqoptionapi.api.IQOptionAPI>`.
        """
        super(Pinocchio, self).__init__(api)
        self.name = "Pinocchio"

    def call(self):
        """Method to check call pattern."""
        if self.candles.first_candle.candle_type == "green":
            return True

    def put(self):
        """Method to check put pattern."""
        if self.candles.first_candle.candle_type == "red":
            return True

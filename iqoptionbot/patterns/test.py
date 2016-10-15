"""Module for IQ Option API TEST pattern."""

from base import Base


class TEST(Base):
    """Class for TEST pattern."""

    def __init__(self, api):
        """
        :param api: The instance of
            :class:`IQOptionAPI <iqoptionapi.api.IQOptionAPI>`.
        """
        super(TEST, self).__init__(api)
        self.name = "TEST"

    def call(self):
        """Method to check call pattern."""
        if self.candles:
            return True

    def put(self):
        """Method to check put pattern."""
        if self.candles:
            return True

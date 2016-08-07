# -*- coding: utf-8 -*-
"""Module for IQ Option API base pattern."""


class Base(object):
    """Class for IQ Option API base pattern."""

    def __init__(self, api):
        self.api = api

    def call(self):
        pass

    def put(self):
        pass
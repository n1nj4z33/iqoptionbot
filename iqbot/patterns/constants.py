# -*- coding: utf-8 -*-
"""Module for IQ Option API trade pattern constants."""

from iqbot.patterns.test import TEST
from iqbot.patterns.dblhc import DBLHC
from iqbot.patterns.dbhlc import DBHLC
from iqbot.patterns.tbh import TBH
from iqbot.patterns.tbl import TBL


PATTERNS = {
    "TEST": TEST,
    "TBH": TBH,
    "TBL": TBL,
    "DBHLC": DBHLC,
    "DBLHC": DBLHC
}

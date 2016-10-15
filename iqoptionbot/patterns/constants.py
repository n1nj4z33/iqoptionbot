"""Module for IQ Option API trade pattern constants."""

from iqoptionbot.patterns.test import TEST
from iqoptionbot.patterns.dblhc import DBLHC
from iqoptionbot.patterns.dbhlc import DBHLC
from iqoptionbot.patterns.tbh import TBH
from iqoptionbot.patterns.tbl import TBL


PATTERNS = {
    "TEST": TEST,
    "TBH": TBH,
    "TBL": TBL,
    "DBHLC": DBHLC,
    "DBLHC": DBLHC
}

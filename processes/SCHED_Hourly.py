# wowsstats/processes/SCHED_Hourly.py

import logging

from wowsstats.processes import UPDATE_Clans, UPDATE_Players, SCRAPE_CBClanHistory
from wowsstats.wowsstatslogging import setup_logging, debug_logging

def SCHED_Hourly():

    logger = logging.getLogger(__name__)
    logger.info("started")

    UPDATE_Clans()

    UPDATE_Players()

    SCRAPE_CBClanHistory()
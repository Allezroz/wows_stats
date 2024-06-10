# wowsstats/processes/SCHED_Daily.py

import logging

from wowsstats.processes import UPDATE_TrackedClans
from wowsstats.processes import SCRAPE_CBClanHistory
from wowsstats.wowsstatslogging import setup_logging, debug_logging

def SCHED_Daily():

    logger = logging.getLogger(__name__)
    logger.info("started")
    
    UPDATE_TrackedClans()
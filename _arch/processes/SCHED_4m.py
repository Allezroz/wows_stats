# wowsstats/processes/SCHED_4m.py

import logging

from wowsstats.processes import SCRAPE_CBGames, SCRAPE_CBStats
from wowsstats.wowsstatslogging import setup_logging, debug_logging

def SCHED_4m():

    logger = logging.getLogger(__name__)
    logger.info("started")
    
    SCRAPE_CBGames()
    
    SCRAPE_CBStats()
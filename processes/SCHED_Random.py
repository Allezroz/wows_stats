# wowsstats/processes/SCHED_Random.py

# currently takes about 22 minutes to run

import logging

from wowsstats.functions import WEBGET_Maps, WEBGET_Ships, WEBGET_ClanBattleSeasons
from wowsstats.processes import UPDATE_PlayerRandomStats
from wowsstats.wowsstatslogging import setup_logging, debug_logging

def SCHED_Random():

    logger = logging.getLogger(__name__)
    logger.info("started")
    
    UPDATE_PlayerRandomStats()
    
    #PR

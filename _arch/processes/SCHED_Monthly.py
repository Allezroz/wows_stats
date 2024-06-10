# wowsstats/processes/SCHED_Monthly.py

# currently takes about 22 minutes to run

import logging

from wowsstats.functions import WEBGET_Maps, WEBGET_Ships, WEBGET_ClanBattleSeasons
from wowsstats.processes import UPDATE_PlayerRandomStats
from wowsstats.wowsstatslogging import setup_logging, debug_logging

def SCHED_Monthly():

    logger = logging.getLogger(__name__)
    logger.info("started")

    WEBGET_Maps()
    WEBGET_Ships()
    WEBGET_ClanBattleSeasons()
    
    # UPDATE_PlayerRandomStats()
    
    #PR

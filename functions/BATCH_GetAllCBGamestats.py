# wowsstats/functions/BATCH_GetAllCBGamestats.py

import datetime, logging, cProfile, pstats

from wowsstats.functions.WEBGET_CBGamestats import WEBGET_CBGamestats
from wowsstats.wowsstatslogging import setup_logging, debug_logging

def BATCH_GetAllCBGamestats(players, season, priority):

    logger = logging.getLogger(__name__)
    logger.info("started")
    logger.info(players)
    logger.info(f"fetching data for {len(players)} players")
    
    for player in players:
        print(player)
        WEBGET_CBGamestats(player["PlayerID"], season, player["Timestamp"], priority, player['Realm'])
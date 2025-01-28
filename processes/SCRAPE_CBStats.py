# wowsstats/processes/SCRAPE_CBStats.py

import datetime, logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging

from wowsstats.functions import SQLGET_CurrentSeason
from wowsstats.functions import SQLGET_WatchedClans
from wowsstats.functions import WEBGET_CaptureIncrementalDamage
from wowsstats.functions import SQLGET_GetPlayersWithNewCBs
from wowsstats.functions import BATCH_GetAllCBGamestats
from wowsstats.functions import SQLGET_RecheckCBStats

def SCRAPE_CBStats():

    logger = logging.getLogger(__name__)
    logger.info("started")

    season = SQLGET_CurrentSeason()
    # testing overwrite
    # season = 19

    logger.info(f"current season: {season}")

    clans = SQLGET_WatchedClans()

    logger.info(f"fetched {len(clans)} watched clans")
    
    for clan in clans:
        WEBGET_CaptureIncrementalDamage(clan['clanId'], season, clan['Realm'])             # dodgy float averages
        BATCH_GetAllCBGamestats(SQLGET_GetPlayersWithNewCBs(), season, 9)      # actual sane int data

    BATCH_GetAllCBGamestats(SQLGET_RecheckCBStats(), season, 11) #weirdo edgecase rechecks

# wowsstats/functions/SQLGET_MissingHistoryClans.py

import logging 

from wowsstats.wowsstatslogging import setup_logging, debug_logging
from wowsstats.functions import SQLGET_CurrentSeason
from wowsstats.config import config

def SQLGET_MissingHistoryClans():

    logger = logging.getLogger(__name__)
    logger.info("started")

    if config.env in ('prod', 'dev'):
        season = SQLGET_CurrentSeason()
    elif config.env == 'test':
        season = config.test_season

    config.dbcon.execute("CALL usp_GetMissingHistoryClans(%s)", (season))
    ret = []
    for t in config.dbcon:
        ret.append(t['ClanID'])
    return(ret)
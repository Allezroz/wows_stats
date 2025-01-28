# wowsstats/functions/BATCH_CaptureIncDmgFromAllClans.py

import logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging

import wowsstats.functions.SQLGET_TrackedClans
import wowsstats.functions.SQLGET_CurrentSeason
import wowsstats.functions.BATCH_GetAllCBGamestats
import wowsstats.functions.WEBGET_CaptureIncrementalDamage
import wowsstats.functions.SQLGET_GetPlayersWithNewCBs
from wowsstats.config import config

def BATCH_CaptureIncDmgFromAllClans():

    logger = logging.getLogger(__name__)
    logger.info("started")

    if config.env in ('prod', 'dev'):
        season = SQLGET_CurrentSeason()
    elif config.env == 'test':
        season = config.test_season

    for clan in SQLGET_TrackedClans():
        WEBGET_CaptureIncrementalDamage(clan['clanId'], season, clan[realm])
        BATCH_GetAllCBGamestats(SQLGET_GetPlayersWithNewCBs(), season)
# wowsstats/functions/SQLGET_TrackedClans.py

import logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging
from wowsstats.config import config

def SQLGET_WatchedClans():

    logger = logging.getLogger(__name__)
    logger.info("started")

    config.dbcon.execute(f"CALL usp_getWatchedClans")
    ret = []
    for t in config.dbcon:
        ret.append(t)
    return(ret)
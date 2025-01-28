# wowsstats/functions/SQLGET_RandomPlayersToUpdate.py

import logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging

from wowsstats.config import config

def SQLGET_RandomPlayersToUpdate():

    logger = logging.getLogger(__name__)
    logger.info("started")

    config.dbcon.execute(f"CALL usp_GetPlayersToUpdateRandomStats")
    ret = []
    for t in config.dbcon:
        ret.append(t)
    return(ret)
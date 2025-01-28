# wowsstats/functions/GetPlayersWithNewCBs.py

import logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging
from wowsstats.config import config

def SQLGET_GetPlayersWithNewCBs():

    logger = logging.getLogger(__name__)
    logger.info("started")

    sql = f"CALL usp_GetPlayersWithNewCBs"
    logger = logging.getLogger(__name__)
    logger.debug(f"{sql}")
    config.dbcon.execute(sql)
    ret = []
    for t in config.dbcon:
        ret.append(t)

    logger.debug(f"{ret}")

    return(ret)

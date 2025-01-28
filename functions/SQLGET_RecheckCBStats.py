# wowsstats/functions/SQLGET_RecheckCBStats.py

import logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging
from wowsstats.config import config

def SQLGET_RecheckCBStats():

    logger = logging.getLogger(__name__)
    logger.info("started RECHECK")

    sql = f"CALL usp_StatsRecheck"
    logger = logging.getLogger(__name__)
    logger.debug(f"{sql}")
    config.dbcon.execute(sql)
    ret = []
    for t in config.dbcon:
        ret.append(t)

    logger.debug(f"{ret}")

    return(ret)

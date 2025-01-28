# wowsstats/functions/SQLGET_CurrentSeason.py

import logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging
from wowsstats.config import config

def SQLGET_CurrentSeason():

    logger = logging.getLogger(__name__)
    logger.info("started")
    
    config.dbcon.execute(f"CALL usp_CurrentSeason")
    ret = config.dbcon.fetchone()
    return(ret['Season'])
# wowsstats/functions/SQLGET_PurgeDb.py

import logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging

from wowsstats.config import config

def SQLPUT_PurgeDb():

    logger = logging.getLogger(__name__)
    logger.info("started")

    if config.dbcon is None:

        logger.error("Database connection is not initialized.")
        return []

    ret = []
    if config.env == "test":

        sql = f"CALL usp_ResetButton('very yes')"

        logger.info(f"{sql}")

        config.dbcon.execute(sql)

        for t in config.dbcon:
            ret.append(t)
        logger.info(f"{ret}")

    elif config.env == "dev":
        logger.warning("WARNING: ATTEMPTING TO PURGE DEV DATABASE! - CANCELLED PURGE")

    elif config.env == "prod":
        logger.critical("ERROR: ATTEMPTING TO PURGE PROD DATABASE! - CANCELLED PURGE")

    return ret
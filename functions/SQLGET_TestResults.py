# wowsstats/functions/SQLGET_TestResults.py

import logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging

from wowsstats.config import config

def SQLGET_TestResults():

    logger = logging.getLogger(__name__)
    logger.info("started")

    if config.dbcon is None:

        logger.error("Database connection is not initialized.")
        return []

    ret = []

    sql = f"call usp_TestResults()"

    logger.info(f"{sql}")

    config.dbcon.execute(sql)

    for t in config.dbcon:
        ret.append(t)
    logger.info(f"{ret}")

    return ret
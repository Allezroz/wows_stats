# wowsstats/functions/WEBGET_SCRAPE.py

import requests, logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging

# janky stuff
def WEBGET_SCRAPE(url, cookies):

    logger = logging.getLogger(__name__)
    logger.debug(f"{url}")

    try:
        result = requests.get(url, cookies=cookies).json()
    except:
        result = {}
        logger.debug(f"No games at {url}")
    return [result]
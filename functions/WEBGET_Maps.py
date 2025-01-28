# wowsstats/functions/WEBGET_Maps.py

import logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging
from wowsstats.functions.WEBGET_API import WEBGET_API
from wowsstats.classes.Map import Map
from wowsstats.config import config

def WEBGET_Maps():

    logger = logging.getLogger(__name__)
    logger.info("started")

    url = f"https://api.worldofwarships.eu/wows/encyclopedia/battlearenas/?application_id={config.appid}"
    logger.debug(f"{url}") 
    maps = WEBGET_API(url)

    if maps["status"] == "ok":

        maps = maps["data"]

        logger.info(f"Fetched {len(maps)} maps from API")
        for wowsmap in maps:

            wowsmap = Map(
                maps[wowsmap]["battle_arena_id"],
                maps[wowsmap]["name"],
                maps[wowsmap]["icon"]
            )
            wowsmap.load()
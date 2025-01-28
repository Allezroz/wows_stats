# wowsstats/functions/WEBGET_ClanBattleSeasons.py

# 1 appID call

import datetime
import logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging
from wowsstats.functions.WEBGET_API import WEBGET_API
from wowsstats.classes.Season import Season
from wowsstats.config import config

def WEBGET_ClanBattleSeasons():

    logger = logging.getLogger(__name__)
    logger.info("started")

    url = f"https://api.worldofwarships.eu/wows/clans/season/?application_id={config.appid}"
    logger.debug(f"{url}")
    seasons = WEBGET_API(url)

    if seasons["status"] == "ok":

        seasons = seasons["data"]
        for season in seasons:
            
            leagues = seasons[season]["leagues"]

            if int(season) < 101:                               # this could use some reliability work
                season = Season(
                    seasons[season]["season_id"],
                    seasons[season]["name"],
                    seasons[season]["ship_tier_min"],
                    seasons[season]["ship_tier_max"],
                    datetime.datetime.fromtimestamp(seasons[season]["start_time"]).strftime("%Y-%m-%d %H:%M:%S"),
                    datetime.datetime.fromtimestamp(seasons[season]["finish_time"]).strftime("%Y-%m-%d %H:%M:%S"),
                    seasons[season]["division_points"]
                )
    
                season.load()
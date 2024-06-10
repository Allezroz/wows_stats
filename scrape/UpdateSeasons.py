# wowsstats/classes/Season.py

import logging, datetime

from wows_stats.conf import setup_logging, debug_logging, config, ReturnObj
from .GetMethods import APIGet

def LoadSeason(Season, SeasonName, MinTier, MaxTier, StartDate, EndDate, DivisionPoints):
       
    logger = logging.getLogger(__name__)
    sql = ("CALL usp_UpdateSeasons(%s,%s,%s,%s,%s,%s,%s)",(Season, SeasonName, MinTier, MaxTier, StartDate, EndDate, DivisionPoints))
    logger.debug(sql)
    config.dbcon.execute(sql[0],sql[1])
    return config.dbcon.fetchone()["Outcome"]

def UpdateSeasons():

    logger = logging.getLogger(__name__)
    logger.info("started")

    url = f"https://api.worldofwarships.eu/wows/clans/season/?application_id={config.appid}"
    logger.debug(f"{url}")
    seasons = APIGet(url)

    ret = ReturnObj(__name__,[])
    if seasons["status"] == "ok":

        seasons = seasons["data"]

        ret = ReturnObj(__name__,seasons)

        for season in seasons:
            
            leagues = seasons[season]["leagues"]

            if int(season) < 101:                               # this could use some reliability work
                ret.Inc(LoadSeason(
                    seasons[season]["season_id"],
                    seasons[season]["name"],
                    seasons[season]["ship_tier_min"],
                    seasons[season]["ship_tier_max"],
                    datetime.datetime.fromtimestamp(seasons[season]["start_time"]).strftime("%Y-%m-%d %H:%M:%S"),
                    datetime.datetime.fromtimestamp(seasons[season]["finish_time"]).strftime("%Y-%m-%d %H:%M:%S"),
                    seasons[season]["division_points"]
                ))
    
    return(ret)
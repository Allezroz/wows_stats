# /wows_stats/scrape/UpdateMaps.py

import logging

from wows_stats.conf import setup_logging, debug_logging, config, ReturnObj
from .GetMethods import APIGet


def LoadMap(MapID,MapName,MapImage):
    sql = ("CALL usp_UpdateMaps(%s,%s,%s)",(MapID,MapName,MapImage))
    logger = logging.getLogger(__name__)
    logger.debug(sql)
    config.dbcon.execute(sql[0],sql[1])
    return config.dbcon.fetchone()["Outcome"]


def UpdateMaps():

    logger = logging.getLogger(__name__)
    logger.info("started")

    url = f"https://api.worldofwarships.eu/wows/encyclopedia/battlearenas/?application_id={config.appid}"
    logger.debug(f"{url}") 
    maps = APIGet(url)

    if maps["status"] == "ok":

        maps = maps["data"]

        ret = ReturnObj(__name__, maps)

        logger.info("Fetched {0} records from API".format(ret.Fetched))
        
        for wowsmap in maps:
            outcome = LoadMap(maps[wowsmap]["battle_arena_id"],
                            maps[wowsmap]["name"],
                            maps[wowsmap]["icon"])
            ret.Inc(outcome)
    
        if ret.Error == 0:
            logger.info("Completed without errors")
        else:
            logger.warn("Completed with " + str(ret.Error) + " errors")

    else:
        logger.error("API Failure in " + __name__)
        ret = ReturnObj(__name__, [])
        ret.Inc('Error')
    return(ret)
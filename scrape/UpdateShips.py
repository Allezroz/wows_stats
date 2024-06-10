# /wows_stats/scrape/GetShips.py

# 1 single non-appID API call

import logging

from wows_stats.conf import setup_logging, debug_logging, config, ReturnObj
from .GetMethods import APIGet

def LoadShip(ShipID,ShipName,ShortName,Tier,Class,Nation):
    
    logger = logging.getLogger(__name__)
    sql = ("CALL usp_UpdateShip(%s,%s,%s,%s,%s,%s)",(ShipID,ShipName,ShortName,Tier,Class,Nation))
    logger.debug(sql)
    config.dbcon.execute(sql[0],sql[1])
    ret = config.dbcon.fetchone()["Outcome"]
    return(ret)

def UpdateShips():

    logger = logging.getLogger(__name__)
    logger.info("started")

    ship_class_mapping = {
        "Destroyer": "DD",
        "Cruiser": "CA",
        "Battleship": "BB",
        "Submarine": "SS",
        "AirCarrier": "CV"
    }

    url = "http://vortex.worldofwarships.eu/api/encyclopedia/en/vehicles/"
    logger.debug(f"Requesting URL: {url}") 
    ships = APIGet(url)
    

    if ships["status"] == "ok":
        ships = ships["data"]
        
        
        ret = ReturnObj(__name__, ships)

        logger.info("Fetched {0} records from API".format(ret.Fetched))
        for SID in ships:
            outcome = LoadShip(
                int(SID),                                        # SID
                ships[SID]["localization"]["mark"]["en"],               # Name
                ships[SID]["localization"]["shortmark"]["en"],          # ShortName
                int(ships[SID]["level"]),                               # Tier
                ship_class_mapping.get(ships[SID]["tags"][0], "??"),    # class
                ships[SID]["nation"]                                    # nation
                )
            ret.Inc(outcome)

        if ret.Error == 0:
            logger.info("Completed without errors")
        else:
            logger.warn("Completed with " + str(ret.Error) + " errors")
        return ret

    else:
        logger.error("API Failure in " + __name__)
        ret = ReturnObj(__name__, [])
        ret.Inc('Error')

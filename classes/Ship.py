# wowsstats/classes/Ship.py

import logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging

from wowsstats.config import config

class Ship():

    def __init__(self, shipID, shipName, shortName, Tier, Class, Nation):

        self.shipID = int(shipID)
        self.shipName = shipName.replace("'", "''")
        self.shortName = shortName.replace("'", "''")
        self.Tier = int(Tier)
        self.Class = Class
        self.Nation = Nation

    def __str__(self):

        return f"{self.shipID} | {self.shipName} | {self.shortName} | {self.Tier} | {self.Class} | {self.Nation}"

    def load(self):

        sql = f"CALL usp_UpdateShip({self.shipID},'{self.shipName}','{self.shortName}',{self.Tier},'{self.Class}','{self.Nation}')"
        logger = logging.getLogger(__name__)
        logger.debug(f"{sql}") 
        config.dbcon.execute(sql)
        return(config.dbcon.fetchone()["Outcome"])

# wowsstats/classes/cbPlayer.py

import logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging

from wowsstats.config import config

class cbPlayer():
    def __init__(self, teamID, playerID, shipID, Survived, realm):

        self.teamID = int(teamID)
        self.playerID = int(playerID)
        self.shipID = int(shipID)
        self.Survived = int(Survived)
        self.realm = realm

    def __str__(self):

        return f"{self.teamID} | {self.playerID} | {self.shipID} | {self.Survived} | {self.realm}"

    def load(self):
        sql = (f"CALL usp_UpdateCBPlayers({self.teamID},{self.playerID},{self.shipID},{self.Survived}, '{self.realm}')")
        logger = logging.getLogger(__name__)
        logger.debug(sql) 
        config.dbcon.execute(sql)
        return(config.dbcon.fetchone()["Outcome"])
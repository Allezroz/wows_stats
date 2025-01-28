# wowsstats/classes/cbGame.py

import logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging

from wowsstats.config import config
dbcon = config.dbcon


class cbGame():

    def __init__(self, gameID, mapID, season, clusterID, arenaID, finishedAt):

        self.gameID = int(gameID)
        self.mapID = int(mapID)
        self.season = int(season)
        self.clusterID = int(clusterID)
        self.arenaID = int(arenaID)
        self.finishedAt = finishedAt  # this should be a datetime formatted string

    def __str__(self):

        return f"{self.gameID} | {self.mapID} | {self.season} | {self.clusterID} | {self.arenaID} | {self.finishedAt}"

    def load(self):
        
        sql = (f"CALL usp_UpdateCBGames({self.gameID},{self.mapID},{self.season},{self.clusterID},{self.arenaID},'{self.finishedAt}')")
        #sql = ("CALL usp_UpdateCBGames(%s,%s,%s,%s,%s,\'%s\')" % (self.gameID,self.mapID,self.season,self.clusterID,self.arenaID,self.finishedAt))
        logger = logging.getLogger(__name__)
        logger.debug(sql)
        config.dbcon.execute(sql)
        tst = config.dbcon.fetchone()
        return(tst['Outcome'])
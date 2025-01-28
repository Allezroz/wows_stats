# wowsstats/classes/Season.py

import logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging

from wowsstats.config import config

class Season():

    def __init__(self, Season, SeasonName, MinTier, MaxTier, StartDate, EndDate, DivisionPoints):

        self.Season = int(Season)
        self.SeasonName = SeasonName.replace("'", "''")
        self.MinTier = int(MinTier)
        self.MaxTier = int(MaxTier)
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.DivisionPoints = int(DivisionPoints)

    def __str__(self):

        return (f"{self.Season} | {self.SeasonName} | {self.MinTier} | {self.MaxTier} | {self.StartDate} | {self.EndDate} | {self.DivisionPoints}")

    def load(self):

        sql = (f"CALL usp_UpdateSeasons({self.Season},'{self.SeasonName}',{self.MinTier},{self.MaxTier},'{self.StartDate}','{self.EndDate}',{self.DivisionPoints})")
        logger = logging.getLogger(__name__)
        logger.debug(sql)
        config.dbcon.execute(sql)
        return config.dbcon.fetchone()["Outcome"]

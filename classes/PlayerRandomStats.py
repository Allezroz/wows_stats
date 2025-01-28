# wowsstats/classes/PlayerRandomStats.py

import logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging

from wowsstats.config import config

class PlayerRandomStats():

    def __init__(self, playerID, shipID, Games, WR, Surv, Frags, Dam, Spot, Tank, XP, MatchType):

        self.playerID = int(playerID)
        self.shipID = int(shipID)
        self.Games = int(Games)
        self.WR = int(WR)
        self.Surv = int(Surv)
        self.Frags = float(Frags)
        self.Dam = int(Dam)
        self.Spot = int(Spot)
        self.Tank = int(Tank)
        self.XP = int(XP)
        self.MatchType = MatchType
        assert MatchType in ('random', 'ranked', 'solo'), "MatchType must be one of 'random','ranked' or 'solo'"

    def __str__(self):

        return f"{self.playerID} | {self.shipID} | {self.Games} | {self.WR} | {self.Surv} | {self.Frags} | {self.Dam} | {self.Spot} | {self.Tank} | {self.XP} | '{self.MatchType}'"

    def load(self):

        sql = f"CALL usp_UpdatePlayerRandomStats({self.playerID},{self.shipID},{self.Games},{self.WR},{self.Surv},{self.Frags},{self.Dam},{self.Spot},{self.Tank},{self.XP},'{self.MatchType}')"
        logger = logging.getLogger(__name__)
        logger.debug(sql)
        config.dbcon.execute(sql)
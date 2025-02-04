# wowsstats/classes/cbTeam.py

import logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging

from wowsstats.config import config

class cbTeam():
    def __init__(self, gameID, teamID, clanID, realm, teamAB, league, division, rating, rating_delta, result):

        self.gameID = int(gameID)
        self.teamID = int(teamID)
        self.clanID = int(clanID)
        self.realm = realm
        self.teamAB = teamAB
        self.league = int(league)
        self.division = int(division)
        self.rating = int(rating)
        self.rating_delta = int(rating_delta)
        self.result = int(result)

    def __str__(self):

        return f"{self.gameID} | {self.teamID} | {self.clanID} | {self.realm} | {self.teamAB} | {self.league} | {self.division} | {self.rating} | {self.rating_delta} | {self.result}"

    def load(self):

        sql = (f"CALL usp_UpdateCBTeams({self.gameID},{self.teamID},{self.clanID},'{self.realm}','{self.teamAB}',{self.league},{self.division},{self.rating},{self.rating_delta},{self.result})")
        logger = logging.getLogger(__name__)
        logger.debug(sql)
        config.dbcon.execute(sql)
        return(config.dbcon.fetchone()["Outcome"])

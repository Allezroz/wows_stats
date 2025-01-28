# wowsstats/classes/LiveDamage.py

import logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging

from wowsstats.config import config

class LiveDamage():
    def __init__(self, clanID, playerID, Games, Damage, Frags, last_battle_time, Season):

        self.clanID = int(clanID)
        self.playerID = int(playerID)
        self.Games = int(Games)
        self.Damage = float(Damage)
        self.Frags = float(Frags)
        # this should be a datetime formatted string
        self.last_battle_time = last_battle_time
        self.Season = int(Season)

    def __str__(self):

        return f"{self.clanID} | {self.playerID} | {self.Games} | {self.Damage} | {self.Frags} | {self.last_battle_time} | {self.Season}"

    def load(self):

        sql = (f"CALL usp_UpdateLiveDamage({self.clanID},{self.playerID},{self.Games},{self.Damage},{self.Frags},'{self.last_battle_time}',{self.Season})")
        logger = logging.getLogger(__name__)
        logger.debug(sql)
        config.dbcon.execute(sql)
        return(config.dbcon.fetchone()["Outcome"])
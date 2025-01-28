# wowsstats/classes/Player.py

import logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging

from wowsstats.config import config

class Player():

    # LastSeen - last time we had a game with the player in. LastChecked will be a sql datestamp on update.

    def __init__(self, playerID, clanID, Nickname, Realm, isHidden, lastSeen):

        self.playerID = int(playerID)
        self.clanID = int(clanID)
        self.Nickname = Nickname
        self.Realm = Realm
        self.isHidden = bool(isHidden)
        self.lastSeen = lastSeen

    def __str__(self):
        
        return f"{self.playerID} | {self.clanID} | {self.Nickname} | {self.Realm} | {self.isHidden} | {self.lastSeen}"

    def load(self):

        config.dbcon.execute(f"CALL usp_UpdatePlayers({self.playerID},{self.clanID},'{self.Nickname}','{self.Realm}',{self.isHidden})")
        return(config.dbcon.fetchone()["Outcome"])
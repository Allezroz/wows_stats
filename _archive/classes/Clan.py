# wowsstats/classes/Clan.py

import logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging

from wowsstats.config import config

class Clan():
    def __init__(self, clanID, clanName, Realm, clanTag, isDisbanded):

        self.clanID = int(clanID)
        self.clanName = clanName.replace("'", "''")
        self.Realm = Realm
        self.clanTag = clanTag
        self.isDisbanded = bool(isDisbanded)

    def __str__(self):

        return f"{self.clanID} | {self.clanName} | {self.Realm} | {self.clanTag} | {self.isDisbanded}"

    def load(self):

        sql = (f"CALL usp_UpdateClans({self.clanID},'{self.clanName}','{self.Realm}','{self.clanTag}',{self.isDisbanded})")
        logger = logging.getLogger(__name__)
        logger.debug(sql)
        config.dbcon.execute(sql)
        return(config.dbcon.fetchone()["Outcome"])


def GetClans():

    config.dbcon.execute(f"CALL usp_getClans")
    ret = []
    for t in config.dbcon:
        ret.append(t)
    return(ret)
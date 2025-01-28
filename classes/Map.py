# wowsstats/classes/Map.py

import logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging

from wowsstats.config import config

class Map():

    def __init__(self, MapID, MapName, MapImage):

        self.MapID = int(MapID)
        self.MapName = MapName.replace("'", "''")
        self.MapImage = MapImage

    def __str__(self):

        return (f"{self.MapID} | {self.MapName} | {self.MapImage}")

    def load(self):

        sql = (f"CALL usp_UpdateMaps({self.MapID}, '{self.MapName}', '{self.MapImage}')")
        logger = logging.getLogger(__name__)
        logger.debug(f"{sql}") 
        config.dbcon.execute(sql)
        return config.dbcon.fetchone()["Outcome"]
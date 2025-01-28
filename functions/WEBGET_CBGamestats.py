# wowsstats/functions/WEBGET_CBGamestats.py

import logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging
from wowsstats.classes.cbGameStats import cbGameStats
from wowsstats.functions.WEBGET_API import WEBGET_API
from wowsstats.config import config

def WEBGET_CBGamestats(playerID, season, timestamp, priority,realm):
    RealmMap = {"eu":"eu", "us":"com", "ru":"ru", "sg":"asia"} 
    Realm = RealmMap[realm]
    logger = logging.getLogger(__name__)
    logger.info("started")
    
    url = f"https://api.worldofwarships.{Realm}/wows/clans/seasonstats/?application_id={config.appid}&account_id={playerID}"
    logger.debug(f"Requesting URL: {url}") 
    cbgamestats = WEBGET_API(url)

    if cbgamestats["status"] == "ok":
        cbgamestats=cbgamestats["data"]
        if not cbgamestats == {}:
            if not cbgamestats[str(playerID)] == None:
                cbgamestats = cbgamestats[str(playerID)]["seasons"]
                if not cbgamestats == []:
                    #below is probably fucking jank but it appears to work
                    #cbgamestats = cbgamestats[next((i for i, item in enumerate(cbgamestats) if item["season_id"] == season), None)]
                    for game in cbgamestats:
                        if game["season_id"]==season:
                            cbgamestats=game
                            cbgamestat = cbGameStats(
                                playerID,
                                timestamp,
                                season,
                                cbgamestats["main_battery"]["frags"],
                                cbgamestats["main_battery"]["hits"],
                                cbgamestats["main_battery"]["shots"],
                                cbgamestats["art_agro"],
                                cbgamestats["ships_spotted"],
                                cbgamestats["second_battery"]["frags"],
                                cbgamestats["second_battery"]["hits"],
                                cbgamestats["second_battery"]["shots"],
                                cbgamestats["survived_battles"],
                                cbgamestats["dropped_capture_points"],
                                cbgamestats["torpedo_agro"],
                                cbgamestats["draws"],
                                cbgamestats["control_captured_points"],
                                cbgamestats["planes_killed"],
                                cbgamestats["battles"],
                                cbgamestats["survived_wins"],
                                cbgamestats["frags"],
                                cbgamestats["damage_scouting"],
                                cbgamestats["capture_points"],
                                cbgamestats["ramming"]["frags"],
                                cbgamestats["torpedoes"]["frags"],
                                cbgamestats["torpedoes"]["hits"],
                                cbgamestats["torpedoes"]["shots"],
                                cbgamestats["aircraft"]["frags"],
                                cbgamestats["team_capture_points"],
                                cbgamestats["control_dropped_points"],
                                cbgamestats["wins"],
                                cbgamestats["losses"],
                                cbgamestats["damage_dealt"],
                                cbgamestats["team_dropped_capture_points"],
                                priority                                
                                )
                            cbgamestat.load()
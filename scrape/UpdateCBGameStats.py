# wowsstats/functions/WEBGET_CBGamestats.py
# wowsstats/classes/cbGameStats.py

import logging

from wows_stats.conf import setup_logging, debug_logging, config, ReturnObj
from .GetMethods import APIGet, RealmMap

def LoadCBGameStats(
        PlayerID, GameTime,Season, mainBatteryFrags,mainBatteryHits,mainBatteryShots,
        artAgro,shipsSpotted,secondBatteryFrags,secondBatteryHits,secondBatteryShots,
        survivedBattles,droppedCapturePoints,torpedoAgro,draws,
        controlCapturedPoints,planesKilled,battles,survivedWins,
        frags,damageScouting,capturePoints,rammingFrags,torpedoesFrags,
        torpedoesHits,torpedoesShots,aircraftFrags,teamCapturePoints,
        controlDroppedPoints,wins,losses,damageDealt,teamDroppedCapturePoints,Priority):

    logger = logging.getLogger(__name__)

    sql = ("CALL usp_UpdateCBGameStats(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
        PlayerID, GameTime, Season,battles,wins, losses, draws, survivedBattles, survivedWins, damageDealt, frags, mainBatteryFrags, secondBatteryFrags, torpedoesFrags, aircraftFrags,
        rammingFrags,mainBatteryShots, secondBatteryShots, torpedoesShots, mainBatteryHits, secondBatteryHits, torpedoesHits, artAgro, torpedoAgro, shipsSpotted, damageScouting,
        planesKilled, droppedCapturePoints, capturePoints, controlCapturedPoints, controlDroppedPoints, teamCapturePoints, teamDroppedCapturePoints,Priority))
    logger.debug(sql)
    config.dbcon.execute(sql[0],sql[1])

   
    return config.dbcon.fetchone()["Outcome"]

def UpdateCBGameStats(PlayerID, Realm, Season, Timestamp, Priority):

    # This one is absolute jank that was thrown together. It seems to work.

    Realm = RealmMap(Realm)
    logger = logging.getLogger(__name__)
    logger.info("started")
    
    url = f"https://api.worldofwarships.{Realm}/wows/clans/seasonstats/?application_id={config.appid}&account_id={PlayerID}"
    logger.debug(f"Requesting URL: {url}") 
    cbgamestats = APIGet(url)

    if cbgamestats["status"] == "ok":
        cbgamestats=cbgamestats["data"]
        ret = ReturnObj(__name__,cbgamestats)
        if not cbgamestats == {}:
            if not cbgamestats[str(PlayerID)] == None:
                cbgamestats = cbgamestats[str(PlayerID)]["seasons"]
                if not cbgamestats == []:
                    for game in cbgamestats:
                        if game["season_id"]==Season:
                            ret.Inc(LoadCBGameStats(
                                PlayerID,
                                Timestamp,
                                Season,
                                game["main_battery"]["frags"],
                                game["main_battery"]["hits"],
                                game["main_battery"]["shots"],
                                game["art_agro"],
                                game["ships_spotted"],
                                game["second_battery"]["frags"],
                                game["second_battery"]["hits"],
                                game["second_battery"]["shots"],
                                game["survived_battles"],
                                game["dropped_capture_points"],
                                game["torpedo_agro"],
                                game["draws"],
                                game["control_captured_points"],
                                game["planes_killed"],
                                game["battles"],
                                game["survived_wins"],
                                game["frags"],
                                game["damage_scouting"],
                                game["capture_points"],
                                game["ramming"]["frags"],
                                game["torpedoes"]["frags"],
                                game["torpedoes"]["hits"],
                                game["torpedoes"]["shots"],
                                game["aircraft"]["frags"],
                                game["team_capture_points"],
                                game["control_dropped_points"],
                                game["wins"],
                                game["losses"],
                                game["damage_dealt"],
                                game["team_dropped_capture_points"],
                                Priority                                
                                ))
    return(ret)
# wows_stats/scrape/UpdatePlayer.py

import datetime
import logging

from wows_stats.conf import setup_logging, debug_logging, config, ReturnObj
from .GetMethods import APIGet, RealmMap

def LoadPlayer(PlayerID, ClanID, Nickname, Realm, IsHidden, LastSeen):
    sql = ("CALL usp_UpdatePlayers(%s,%s,%s,%s,%s)",(PlayerID, ClanID, Nickname, Realm, IsHidden))
    logger = logging.getLogger(__name__)
    logger.debug(sql)
    config.dbcon.execute(sql[0],sql[1])
    return(config.dbcon.fetchone()["Outcome"])

    
def UpdatePlayer(PlayerID, Realm):

    Realm = RealmMap(Realm)
    # Fetch player name and hidden profile status
    url = f"https://api.worldofwarships.{Realm}/wows/account/info/?account_id={PlayerID}&application_id={config.appid}&fields=nickname"
    logger = logging.getLogger(__name__)
    logger.debug(f"Requesting URL: {url}")
    player_data = APIGet(url)

    ret = ReturnObj(__name__, [1])

    if player_data["status"] == "error":
        print("api error, check app ID")
        ret.Inc('Error')
        return ret
    nickname = player_data["data"][str(
        PlayerID)]["nickname"] if player_data["data"][str(PlayerID)] else None

    # Fetch player clan ID - we get gameclan from CB process, player data from here, but we do not have the player clan without an explicit check
    url = f"https://api.worldofwarships.eu/wows/clans/accountinfo/?account_id={PlayerID}&application_id={config.appid}"
    logger.debug(f"Requesting URL: {url}")
    clan_data = APIGet(url)
    if clan_data["status"] == "error":
        print("api error, check app ID")
        ret.Inc('Error')
        return ret
    clan_id = clan_data["data"][str(
        PlayerID)]["clan_id"] if clan_data["data"][str(PlayerID)] else 99999999

    # If any required data is missing, return
    if not all([nickname, clan_id]):
        print("Player data not found.")
        ret.Inc('Error')
        return ret

    # Create player object
    ret.Inc(LoadPlayer(
        PlayerID,
        clan_id,
        nickname,
        "EU",  # TODO: realm handling
        1 if player_data["meta"]["hidden"] and player_data["meta"]["hidden"][0] == PlayerID else 0,
        datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ))

    return ret

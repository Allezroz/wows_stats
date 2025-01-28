# wowsstats/functions/WEBGET_Player.py

import datetime
import logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging
from wowsstats.classes import Player
from wowsstats.functions.WEBGET_API import WEBGET_API
from wowsstats.config import config

def WEBGET_Player(playerID, realm):
    RealmMap = {"eu":"eu", "us":"com", "ru":"ru", "sg":"asia"} 
    Realm = RealmMap[realm]
    # Fetch player name and hidden profile status
    url = f"https://api.worldofwarships.{Realm}/wows/account/info/?account_id={playerID}&application_id={config.appid}&fields=nickname"
    logger = logging.getLogger(__name__)
    logger.debug(f"Requesting URL: {url}")
    player_data = WEBGET_API(url)
    if player_data["status"] == "error":
        print("api error, check app ID")
        return None
    nickname = player_data["data"][str(
        playerID)]["nickname"] if player_data["data"][str(playerID)] else None

    # Fetch player clan tag
    url = f"https://api.worldofwarships.{Realm}/wows/clans/accountinfo/?account_id={playerID}&application_id={config.appid}"
    logger.debug(f"Requesting URL: {url}")
    clan_data = WEBGET_API(url)
    if clan_data["status"] == "error":
        print("api error, check app ID")
        return None
    clan_id = clan_data["data"][str(
        playerID)]["clan_id"] if clan_data["data"][str(playerID)] else 99999999

    # If any required data is missing, return
    if not all([nickname, clan_id]):
        print("Player data not found.")
        return None

    # Create player object
    player = Player(
        playerID,
        clan_id,
        nickname,
        realm,  # TODO: realm handling
        1 if ((player_data["meta"]["hidden"]) and (player_data["meta"]["hidden"][0] == playerID)) else 0,
        datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )

    # Update database entry for player
    player.load()

    return player
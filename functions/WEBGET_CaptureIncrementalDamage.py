# wowsstats/functions/WEBGET_CaptureIncrementalDamage.py

# 1 single non-appID API call

import datetime
import logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging
from wowsstats.functions.WEBGET_API import WEBGET_API
from wowsstats.classes.LiveDamage import LiveDamage

def WEBGET_CaptureIncrementalDamage(clanID, seasonNumber, realm):
    RealmMap = {"eu":"eu", "us":"com", "ru":"ru", "sg":"asia"} 
    Realm = RealmMap[realm]
    logger = logging.getLogger(__name__)
    logger.info("started")

    url = f"https://clans.worldofwarships.{Realm}/api/members/{clanID}/?battle_type=cvc&season={seasonNumber}"
    logger.debug(f"{url}") 
    players = WEBGET_API(url)
    for player in players["items"]:
        if not player["is_hidden_statistics"]:
            player = LiveDamage(
                clanID,
                player["id"],
                player["battles_count"],
                player["damage_per_battle"],
                player["frags_per_battle"],
                datetime.datetime.fromtimestamp(player["last_battle_time"]).strftime("%Y-%m-%d %H:%M:%S"),
                seasonNumber
            )
            player.load()
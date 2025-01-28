# wowsstats/functions/WEBGET_ClanData.py

import logging

from wowsstats.functions.WEBGET_API import WEBGET_API
from wowsstats.wowsstatslogging import setup_logging, debug_logging
from wowsstats.config import config

def WEBGET_ClanData(clanID, realm):
    RealmMap = {"eu":"eu", "us":"com", "ru":"ru", "sg":"asia"} 
    Realm = RealmMap[realm]
    logger = logging.getLogger(__name__)
    logger.info("started")

    url = f"https://api.worldofwarships.{Realm}/wows/clans/info/?application_id={config.appid}&clan_id={clanID}"
    logger.debug(f"{url}")
    clandata = WEBGET_API(url)
    logger.debug(f"recieved{type(clandata)}")

    return clandata
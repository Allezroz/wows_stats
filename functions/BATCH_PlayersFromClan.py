# wowsstats/functions/BATCH_PlayersFromClan.py

import logging

from wowsstats.functions.WEBGET_ClanData import WEBGET_ClanData
from wowsstats.wowsstatslogging import setup_logging, debug_logging

def BATCH_PlayersFromClan(clanID,realm):

    logger = logging.getLogger(__name__)
    logger.info("started")

    playerIDs = WEBGET_ClanData(clanID, realm)

    if playerIDs["status"] == "error":

        print("api error requesting clan data, check app ID and clan ID")
        return None

    playerIDs = playerIDs["data"][str(clanID)]["members_ids"] if playerIDs["data"][str(clanID)] else None

    return playerIDs

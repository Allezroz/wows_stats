# wowsstats/functions/BATCH_AddPlayersToPlayers.py

import logging

from wowsstats.functions.WEBGET_Player import WEBGET_Player
from wowsstats.wowsstatslogging import setup_logging, debug_logging

def BATCH_AddPlayersToPlayers(playerIDs, realm):

    logger = logging.getLogger(__name__)
    logger.info("started")
    
    for playerID in playerIDs:
        WEBGET_Player(playerID, realm)

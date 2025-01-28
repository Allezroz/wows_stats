# wowsstats/functions/BATCH_UpdateClans.py

import logging

from wowsstats.functions import SQLGET_ClansToUpdate
from wowsstats.functions import WEBGET_ClanData
from wowsstats.classes.Clan import Clan
from wowsstats.wowsstatslogging import setup_logging, debug_logging

def BATCH_UpdateClans():

    logger = logging.getLogger(__name__)
    logger.info("started")

    clans = SQLGET_ClansToUpdate()
    for clan in clans:

        clanID = clan["clanID"]
        realm = clan["realm"]
        clandata = WEBGET_ClanData(clanID,realm)
        logger.debug("%s started for clan %s", __package__, clan)

        if clandata["status"] == "error":

            print("api error requesting clan data, check app ID and clan ID")
            return None

        elif clandata["status"] == "ok":

            clandata = clandata["data"][str(clanID)]

            if not clandata == None:

                clan = Clan(
                    clanID,
                    clandata["name"],
                    clan['realm'], 							# todo: add realm handling
                    clandata["tag"],
                    clandata["is_clan_disbanded"]
                )

            elif clandata == None:

                clan = Clan(
                    clanID,
                    "",
                    realm,
                    "",
                    1
                )

            clan.load()
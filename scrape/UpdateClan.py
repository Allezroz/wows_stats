# wows_stats/scrape/UpdateClan.py

import logging

from wows_stats.conf import setup_logging, debug_logging, config, ReturnObj
from .GetMethods import APIGet, RealmMap

def LoadClan(ClanID, ClanName, Realm, ClanTag, IsDisbanded):

    logger = logging.getLogger(__name__)
    sql=("CALL usp_UpdateClans(%s,%s,%s,%s,%s)",(ClanID, ClanName, Realm, ClanTag, IsDisbanded))
    logger.debug(sql)
    config.dbcon.execute(sql[0],sql[1])


    return(config.dbcon.fetchone()["Outcome"])

def UpdateClan(ClanID, Realm):

    Realm = RealmMap(Realm)
    logger = logging.getLogger(__name__)
    logger.info("started")
    ret = ReturnObj(__name__, [1])

    url = f"https://api.worldofwarships.{Realm}/wows/clans/info/?application_id={config.appid}&clan_id={ClanID}"
    logger.debug(f"{url}")
    clandata = APIGet(url)
    logger.debug(f"recieved{type(clandata)}")
    

    if clandata["status"] == "error":

            print("api error requesting clan data, check app ID and clan ID")
            ret.Inc('Error')

    elif clandata["status"] == "ok":

        clandata = clandata["data"][str(ClanID)]

        if not clandata == None:
            ret.Inc(LoadClan(
                ClanID,
                clandata["name"],
                'eu',                           # todo: add realm handling
                clandata["tag"],
                clandata["is_clan_disbanded"]
            ))
        elif clandata == None:
            ret.Inc(LoadClan(
                ClanID,
                "",
                "",
                "",
                1))

    return ret

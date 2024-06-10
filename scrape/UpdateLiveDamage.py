# wows_stats/scrape/UpdateLiveDamage.py

import logging, datetime

from wows_stats.conf import setup_logging, debug_logging, config, ReturnObj
from .GetMethods import APIGet, RealmMap

def LoadLiveDamage(ClanID, PlayerID, Games, Damage, Frags, LastBattleTime, Season):

    logger = logging.getLogger(__name__)
    sql=("CALL usp_UpdateLiveDamage(%s,%s,%s,%s,%s,%s,%s)",(ClanID, PlayerID, Games, Damage, Frags, LastBattleTime, Season))
    logger.debug(sql)
    config.dbcon.execute(sql[0],sql[1])
    return(config.dbcon.fetchone()["Outcome"])

def UpdateLiveDamage(ClanID, Realm, Season):

    Realm = RealmMap(Realm)
    logger = logging.getLogger(__name__)
    logger.info("started")

    url = f"https://clans.worldofwarships.{Realm}/api/members/{ClanID}/?battle_type=cvc&season={Season}"
    logger.debug(f"{url}") 
    players = APIGet(url)
    ret = ReturnObj(__name__, players["items"])

    for player in players["items"]:
        if not player["is_hidden_statistics"]:
            ret.Inc(LoadLiveDamage(
                ClanID,
                player["id"],
                player["battles_count"],
                player["damage_per_battle"],
                player["frags_per_battle"],
                datetime.datetime.fromtimestamp(player["last_battle_time"]).strftime("%Y-%m-%d %H:%M:%S"),
                Season))
    return(ret)
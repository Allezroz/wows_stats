 # wows_stats/scrape/UpdatePlayerRandomStats.py

import logging

from wows_stats.conf import setup_logging, debug_logging, config, ReturnObj
from .GetMethods import APIGet, RealmMap

def LoadPlayerRandomStats(PlayerID, ShipID, Games, WR, Surv, Frags, Dam, Spot, Tank, XP, MatchType):
    logger = logging.getLogger(__name__)
    sql=("CALL usp_UpdatePlayerRandomStats(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(PlayerID, ShipID, Games, WR, Surv, Frags, Dam, Spot, Tank, XP, MatchType))
    logger.debug(sql)
    config.dbcon.execute(sql[0],sql[1])
    ret = config.dbcon.fetchone()["Outcome"]
    return(ret)

def UpdatePlayerRandomStats(PlayerID, Realm):

    Realm = RealmMap(Realm)

    logger = logging.getLogger(__name__)
    logger.info("started")

    url = (
            f"https://api.worldofwarships.{Realm}/wows/ships/stats/"
            f"?application_id={config.appid}"
            f"&account_id={PlayerID}"
            f"&extra=pvp_solo%2C+rank_solo"
            f"&fields=ship_id%2Cpvp.battles%2Cpvp.xp%2Cpvp_solo.xp%2Crank_solo.xp%2Cpvp_solo.battles%2Crank_solo.battles%2C"
            f"pvp.wins%2Cpvp_solo.wins%2Crank_solo.wins%2Cpvp.losses%2Cpvp_solo.losses%2Crank_solo.losses%2C"
            f"pvp.draws%2Cpvp_solo.draws%2Crank_solo.draws%2Cpvp.damage_scouting%2Cpvp_solo.damage_scouting%2Crank_solo.damage_scouting%2C"
            f"pvp.survived_battles%2Cpvp_solo.survived_battles%2Crank_solo.survived_battles%2Cpvp.frags%2Cpvp_solo.frags%2Crank_solo.frags%2C"
            f"pvp.damage_dealt%2Cpvp_solo.damage_dealt%2Crank_solo.damage_dealt%2Crank_solo.art_agro%2Crank_solo.torpedo_agro%2C"
            f"pvp_solo.art_agro%2Cpvp_solo.torpedo_agro%2Cpvp.art_agro%2Cpvp.torpedo_agro"
        )
    logger.debug(f"Requesting URL: {url}") 
    ships = APIGet(url)

    playerShips = []

    # TODO: check for status !

    r = APIGet(url)['data']
    
    ret = ReturnObj(__name__, [])

    if not r == {}:
        r = r[list(r.keys())[0]]
        if not r == None:
            ret = ReturnObj(__name__, r)
            logger.info("Fetched {0} records from API".format(ret.Fetched))
            
            for q in r:      
                if q['rank_solo']['battles'] != 0:
                    outcome = LoadPlayerRandomStats(PlayerID,
                        q['ship_id'],
                        q['rank_solo']['battles'],
                        q['rank_solo']['wins'],
                        q['rank_solo']['survived_battles']/q['rank_solo']['battles'],
                        q['rank_solo']['frags']/q['rank_solo']['battles'],
                        round(q['rank_solo']['damage_dealt'] /
                              q['rank_solo']['battles'], 0),
                        round(q['rank_solo']['damage_scouting'] /
                              q['rank_solo']['battles'], 0),
                        round((q['rank_solo']['art_agro']+q['rank_solo']
                              ['torpedo_agro'])/q['rank_solo']['battles'], 0),
                        q['rank_solo']['xp']/q['rank_solo']['battles'],
                        'ranked')  
                    ret.Inc(outcome)
                    if outcome == 'Error':
                        sid = q['ship_id']
                        logger.warn(f"Error: Player:{PlayerID}, Ship: {sid}, Type: Ranked")


                if q['pvp']['battles'] != 0:
                    outcome = LoadPlayerRandomStats(
                        PlayerID,
                        q['ship_id'],
                        q['pvp']['battles'],
                        q['pvp']['wins'],
                        q['pvp']['survived_battles']/q['pvp']['battles'],
                        q['pvp']['frags']/q['pvp']['battles'],
                        round(q['pvp']['damage_dealt']/q['pvp']['battles'], 0),
                        round(q['pvp']['damage_scouting']/q['pvp']['battles'], 0),
                        round((q['pvp']['art_agro']+q['pvp']
                              ['torpedo_agro'])/q['pvp']['battles'], 0),
                        q['pvp']['xp']/q['pvp']['battles'],
                        'random'
                    )
                    ret.Inc(outcome)
                    if outcome == 'Error':
                        sid = q['ship_id']
                        logger.warn(f"Error: Player:{PlayerID}, Ship: {sid}, Type: Random")

                if q['pvp_solo']['battles'] != 0:
                    outcome = LoadPlayerRandomStats(
                        PlayerID,
                        q['ship_id'],
                        q['pvp_solo']['battles'],
                        q['pvp_solo']['wins'],
                        q['pvp_solo']['survived_battles']/q['pvp_solo']['battles'],
                        q['pvp_solo']['frags']/q['pvp_solo']['battles'],
                        round(q['pvp_solo']['damage_dealt'] /
                              q['pvp_solo']['battles'], 0),
                        round(q['pvp_solo']['damage_scouting'] /
                              q['pvp_solo']['battles'], 0),
                        round((q['pvp_solo']['art_agro']+q['pvp_solo']
                              ['torpedo_agro'])/q['pvp_solo']['battles'], 0),
                        q['pvp_solo']['xp']/q['pvp_solo']['battles'],
                        'solo')
                    ret.Inc(outcome)
                    if outcome == 'Error':
                        sid = q['ship_id']
                        logger.warn(f"Error: Player:{PlayerID}, Ship: {sid}, Type: Solo")
            return ret
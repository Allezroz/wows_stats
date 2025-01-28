 # wowsstats/functions/WEBGET_PlayerRandomStats.py

import logging

from wowsstats.classes import PlayerRandomStats
from wowsstats.functions.WEBGET_API import WEBGET_API
from wowsstats.wowsstatslogging import setup_logging, debug_logging
from wowsstats.config import config

def WEBGET_PlayerRandomStats(playerID,realm):
    RealmMap = {"eu":"eu", "us":"com", "ru":"ru", "sg":"asia"} 
    Realm = RealmMap[realm]

    logger = logging.getLogger(__name__)
    logger.info("started")

    url = (
            f"https://api.worldofwarships.{Realm}/wows/ships/stats/"
            f"?application_id={config.appid}"
            f"&account_id={playerID}"
            f"&extra=pvp_solo%2C+rank_solo"
            f"&fields=ship_id%2Cpvp.battles%2Cpvp.xp%2Cpvp_solo.xp%2Crank_solo.xp%2Cpvp_solo.battles%2Crank_solo.battles%2C"
            f"pvp.wins%2Cpvp_solo.wins%2Crank_solo.wins%2Cpvp.losses%2Cpvp_solo.losses%2Crank_solo.losses%2C"
            f"pvp.draws%2Cpvp_solo.draws%2Crank_solo.draws%2Cpvp.damage_scouting%2Cpvp_solo.damage_scouting%2Crank_solo.damage_scouting%2C"
            f"pvp.survived_battles%2Cpvp_solo.survived_battles%2Crank_solo.survived_battles%2Cpvp.frags%2Cpvp_solo.frags%2Crank_solo.frags%2C"
            f"pvp.damage_dealt%2Cpvp_solo.damage_dealt%2Crank_solo.damage_dealt%2Crank_solo.art_agro%2Crank_solo.torpedo_agro%2C"
            f"pvp_solo.art_agro%2Cpvp_solo.torpedo_agro%2Cpvp.art_agro%2Cpvp.torpedo_agro"
        )
    logger.debug(f"Requesting URL: {url}") 
    ships = WEBGET_API(url)

    playerShips = []

    # TODO: check for status !

    r = WEBGET_API(url)['data']

    if not r == {}:
        r = r[list(r.keys())[0]]
        if not r == None:
            for q in r:
        
                if q['rank_solo']['battles'] != 0:
                    stats_ranked = PlayerRandomStats(
                        playerID,
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
                        'ranked'
                    )
                    stats_ranked.load()    
                    playerShips.append(stats_ranked)

                if q['pvp']['battles'] != 0:
                    stats_random = PlayerRandomStats(
                        playerID,
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
                    stats_random.load()    
                    playerShips.append(stats_random)

                if q['pvp_solo']['battles'] != 0:

                    stats_solo = PlayerRandomStats(
                        playerID,
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
                        'solo'
                    )
                    stats_solo.load()    
                    playerShips.append(stats_solo)

            return playerShips
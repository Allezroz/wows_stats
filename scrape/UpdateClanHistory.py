# /wows_stats/scrape/UpdateClanHistory.py

# 1 appID call

import datetime
import logging

from wows_stats.conf import setup_logging, debug_logging, config, ReturnObj
from .GetMethods import APIGet, RealmMap, WG_APIGet
from .CheckSQL import CheckCurrentSeason


def LoadClanHistory(clanID, battles_count, league, max_position_public_rating, 
            max_position_division_rating, max_position_league, max_position_division, 
            wins_count, initial_public_rating, is_best_season_rating, 
            team_number, is_qualified, rating_id, current_winning_streak, status, 
            season_number, division_rating_max, realm, division_rating, longest_winning_streak, 
            max_public_rating, public_rating, last_win_at, division):      

    logger = logging.getLogger(__name__)
    sql=("CALL usp_UpdateClanRatings(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (clanID, battles_count, league, max_position_public_rating, 
            max_position_division_rating, max_position_league, max_position_division, 
            wins_count, initial_public_rating, is_best_season_rating, 
            team_number, is_qualified, rating_id, current_winning_streak, status, 
            season_number, division_rating_max, realm, division_rating, longest_winning_streak, 
            max_public_rating, public_rating, last_win_at, division))
    logger.debug(sql)
    config.dbcon.execute(sql[0],sql[1])


    return(config.dbcon.fetchone()["Outcome"])

def UpdateClanHistory(ClanID, Realm):

    Realm = RealmMap(Realm)
    logger = logging.getLogger(__name__)
    logger.info("started")

    url = f"https://clans.worldofwarships.{Realm}/api/clanbase/{ClanID}/claninfo/"
    logger.debug(f"{url}") 
    seasons = WG_APIGet(url)
    ret = ReturnObj(__name__, seasons["clanview"]["wows_ladder"]["ratings"])
    for rating in seasons["clanview"]["wows_ladder"]["ratings"]:
        ret.Inc(LoadClanHistory(
            ClanID,
            rating["battles_count"],
            rating["league"],
            rating["max_position"]["public_rating"],
            rating["max_position"]["division_rating"],
            rating["max_position"]["league"],
            rating["max_position"]["division"],
            rating["wins_count"],
            rating["initial_public_rating"],
            rating["is_best_season_rating"],
            rating["team_number"],
            rating["is_qualified"],
            rating["id"],
            rating["current_winning_streak"],
            rating["status"],
            rating["season_number"],
            rating["division_rating_max"],
            rating["realm"],
            rating["division_rating"],
            rating["longest_winning_streak"],
            rating["max_public_rating"],
            rating["public_rating"],
            rating["last_win_at"],
            rating["division"]
        ))
    return(ret)
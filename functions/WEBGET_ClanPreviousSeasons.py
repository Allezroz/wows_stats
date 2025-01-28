# wowsstats/functions/WEBGET_ClanPreviousSeasons.py

import datetime
import json
import logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging
from wowsstats.functions.WEBGET_API import WEBGET_API
from wowsstats.functions.WEBGET_API_IMPROPER import WEBGET_API_IMPROPER
from wowsstats.classes.LiveDamage import LiveDamage
from wowsstats.classes.ClanRating import ClanRating

def WEBGET_ClanPreviousSeasons(clanID):

    logger = logging.getLogger(__name__)
    logger.info("started")

    url = f"https://clans.worldofwarships.eu/api/clanbase/{clanID}/claninfo/"
    logger.debug(f"{url}") 
    seasons = WEBGET_API_IMPROPER(url)

    def print_json_keys(data, indent=4):
        def process_level(data, indent):
            if isinstance(data, dict):
                for key, value in data.items():
                    print(f'{indent}{" " * indent}{key}')
                    process_level(value, indent + 2)
            elif isinstance(data, list):
                for item in data:
                    process_level(item, indent + 2)
    
        process_level(data, indent)

    #print_json_keys(seasons["clanview"]["wows_ladder"]["ratings"])

    for rating in seasons["clanview"]["wows_ladder"]["ratings"]:
        clanRating = ClanRating(
            clanID,
            rating["battles_count"],
            rating["league"],
            rating["max_position"]["public_rating"],
            rating["max_position"]["division_rating"],
            rating["max_position"]["league"],
            rating["max_position"]["division"],
            rating["wins_count"],
            rating["initial_public_rating"],
            rating["is_best_season_rating"],
            rating["stage"],
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
        )
        clanRating.load()
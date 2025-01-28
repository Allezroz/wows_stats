# wowsstats/classes/ClanRating.py

import logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging

from wowsstats.functions.SqlWrap import SqlWrap

from wowsstats.config import config

class ClanRating():
    def __init__(
        self,
        clanID,
        battles_count,
        league,
        max_position_public_rating,
        max_position_division_rating,
        max_position_league,
        max_position_division,
        wins_count,
        initial_public_rating,
        is_best_season_rating,
        stage,
        team_number,
        is_qualified,
        rating_id,
        current_winning_streak,
        status,
        season_number,
        division_rating_max,
        realm,
        division_rating,
        longest_winning_streak,
        max_public_rating,
        public_rating,
        last_win_at,
        division
        ):

        self.clanID = int(clanID)
        self.battles_count = int(battles_count)
        self.league = int(league)
        self.max_position_public_rating = int(max_position_public_rating)
        self.max_position_division_rating = int(max_position_division_rating)
        self.max_position_league = int(max_position_league)
        self.max_position_division = int(max_position_division)
        self.wins_count = int(wins_count)
        self.initial_public_rating = int(initial_public_rating)
        self.is_best_season_rating = bool(is_best_season_rating)
        self.stage = stage
        self.team_number = int(team_number)
        self.is_qualified = bool(is_qualified)
        self.rating_id = int(rating_id)
        self.current_winning_streak = int(current_winning_streak)
        self.status = status
        self.season_number = int(season_number)
        self.division_rating_max = int(division_rating_max)
        self.realm = realm
        self.division_rating = int(division_rating)
        self.longest_winning_streak = int(longest_winning_streak)
        self.max_public_rating = int(max_public_rating)
        self.public_rating = int(public_rating)
        self.last_win_at = last_win_at
        self.division = int(division)

    def __str__(self):
        return f"{self.clanID} | {self.battles_count} | {self.league} | {self.max_position_public_rating} | {self.max_position_division_rating} | {self.max_position_league} | {self.max_position_division} | {self.wins_count} | {self.initial_public_rating} | {self.is_best_season_rating} | {self.stage} | {self.team_number} | {self.is_qualified} | {self.rating_id} | {self.current_winning_streak} | {self.status} | {self.season_number} | {self.division_rating_max} | {self.realm} | {self.division_rating} | {self.longest_winning_streak} | {self.max_public_rating} | {self.public_rating} | {self.last_win_at} | {self.division}"

    def load(self):
            
        sql = ("CALL usp_UpdateClanRatings(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
               (self.clanID, self.battles_count, self.league, self.max_position_public_rating, 
                self.max_position_division_rating, self.max_position_league, self.max_position_division, 
                self.wins_count, self.initial_public_rating, self.is_best_season_rating, 
                self.team_number, self.is_qualified, self.rating_id, self.current_winning_streak, self.status, 
                self.season_number, self.division_rating_max, self.realm, self.division_rating, self.longest_winning_streak, 
                self.max_public_rating, self.public_rating, self.last_win_at, self.division))

        logger = logging.getLogger(__name__)
        logger.debug(sql)

        config.dbcon.execute("CALL usp_UpdateClanRatings(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (self.clanID, self.battles_count, self.league, self.max_position_public_rating, 
                self.max_position_division_rating, self.max_position_league, self.max_position_division, 
                self.wins_count, self.initial_public_rating, self.is_best_season_rating, 
                self.team_number, self.is_qualified, self.rating_id, self.current_winning_streak, self.status, 
                self.season_number, self.division_rating_max, self.realm, self.division_rating, self.longest_winning_streak, 
                self.max_public_rating, self.public_rating, self.last_win_at, self.division))
        return(config.dbcon.fetchone()["Outcome"])


def GetClans():

    config.dbcon.execute(f"CALL usp_getClanRatings")
    ret = []
    for t in config.dbcon:
        ret.append(t)
    return(ret)
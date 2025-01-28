# wowsstats/functions/WEBGET_CBGames.py

import datetime, requests, logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging
from wowsstats.functions.WEBGET_SCRAPE import WEBGET_SCRAPE
from wowsstats.functions.SQLGET_TrackedClans import SQLGET_TrackedClans
from wowsstats.classes.cbGame import cbGame
from wowsstats.classes.cbTeam import cbTeam
from wowsstats.classes.cbPlayer import cbPlayer

def WEBGET_CBGames():

    logger = logging.getLogger(__name__)
    logger.info("started")
    RealmMap = {"eu":"eu", "us":"com", "ru":"ru", "sg":"asia"} 
    
    for clan in SQLGET_TrackedClans():
        Realm = RealmMap[clan['clanRealm']]
        ratings = [1, 2]

        for rating in ratings:

            cookies = {'wsauth_token': clan['token']}
            url = f"https://clans.worldofwarships.{Realm}/api/ladder/battles/?team={rating}"
            logger.debug(f"{url}")
            games = WEBGET_SCRAPE(url, cookies)
            rating = {1: 'A', 2: 'B'}[rating]
            if len(games) > 0:
                for game in games[0]:

                    cbgame = cbGame(
                        game["id"],
                        game["map_id"],
                        game["season_number"],
                        game["cluster_id"],
                        game["arena_id"],
                        # strip timezone info off the end of string, then convert to mysql datetime format
                        datetime.datetime.strptime(
                            game["finished_at"][:-6], "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                    )

                    tst = cbgame.load()
                    if tst != "Exists":
                        for team in game["teams"]:

                            cbteam = cbTeam(
                                game["id"],     # game ID
                                team["id"],     # team ID
                                team["clan_id"],
                                team["claninfo"]["realm"],
                                rating,
                                team["league"],
                                team["division"],
                                team["division_rating"],
                                team["rating_delta"],
                                # assumption: 0 == defeat, 1 == victory
                                {'defeat': 0, 'victory': 1}[team["result"]]
                            )

                            cbteam.load()

                            for player in team["players"]:

                                cbplayer = cbPlayer(
                                    team["id"],
                                    player["spa_id"],
                                    player["vehicle_id"],
                                    # assumption: 0 == died, 1 == survived
                                    {False: 0, True: 1}[player["survived"]],
                                    team["claninfo"]["realm"]
                                )

                                cbplayer.load()
# wows_stats/scrape/UpdateCBGames.py

import logging, datetime

from wows_stats.conf import setup_logging, debug_logging, config, ReturnObj
from .GetMethods import WebGet, RealmMap
from .CheckSQL import CheckTrackedClans

def LoadCBGame(gameID, mapID, season, clusterID, arenaID, finishedAt):

    logger = logging.getLogger(__name__)
    sql = ("CALL usp_UpdateCBGames(%s,%s,%s,%s,%s,%s)",(gameID, mapID, season, clusterID, arenaID, finishedAt))
    logger.debug(sql)
    config.dbcon.execute(sql[0],sql[1])
    tst = config.dbcon.fetchone()
    return(tst['Outcome'])

def LoadCBTeam(gameID, teamID, clanID, realm, teamAB, league, division, rating, rating_delta, result):
    sql = ("CALL usp_UpdateCBTeams(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(gameID, teamID, clanID, realm, teamAB, league, division, rating, rating_delta, result))
    logger = logging.getLogger(__name__)
    logger.debug(sql)
    config.dbcon.execute(sql[0],sql[1])
    return(config.dbcon.fetchone()["Outcome"])

def LoadCBPlayer(teamID, playerID, shipID, Survived, realm):

    sql = ("CALL usp_UpdateCBPlayers(%s,%s,%s,%s,%s)",(teamID, playerID, shipID, Survived, realm))
    logger = logging.getLogger(__name__)
    logger.debug(sql)
    config.dbcon.execute(sql[0],sql[1])
    return(config.dbcon.fetchone()["Outcome"])

def UpdateCBGames(): # Really we should pass in a ClanID and a Realm...

    logger = logging.getLogger(__name__)
    logger.info("started")
    ret = ReturnObj(__name__,[])

    for clan in CheckTrackedClans():
        ratings = [1, 2]

        for rating in ratings:

            cookies = {'wsauth_token': clan['token']}
            url = f"https://clans.worldofwarships.eu/api/ladder/battles/?team={rating}"
            logger.debug(f"{url}")
            games = WebGet(url, cookies)
            rating = {1: 'A', 2: 'B'}[rating]

            if len(games) > 0:
                ret.Fetched += len(games)
                for game in games[0]:
                    tst=(LoadCBGame(
                        game["id"],
                        game["map_id"],
                        game["season_number"],
                        game["cluster_id"],
                        game["arena_id"],
                        # strip timezone info off the end of string, then convert to mysql datetime format
                        datetime.datetime.strptime(
                            game["finished_at"][:-6], "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                    ))
                    ret.Inc(tst)

                    if tst != "Exists":
                        for team in game["teams"]:

                            LoadCBTeam(
                                game["id"],     # game ID
                                team["id"],     # team ID
                                team["clan_id"],
                                game["realm"],
                                rating,
                                team["league"],
                                team["division"],
                                team["division_rating"],
                                team["rating_delta"],
                                # assumption: 0 == defeat, 1 == victory
                                {'defeat': 0, 'victory': 1}[team["result"]]
                            )

                            for player in team["players"]:

                                LoadCBPlayer(
                                    team["id"],
                                    player["spa_id"],
                                    player["vehicle_id"],
                                    # assumption: 0 == died, 1 == survived
                                    {False: 0, True: 1}[player["survived"]],
                                    game["realm"]
                                )

    return(ret)
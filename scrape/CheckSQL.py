# wows_stats/scrape/CheckSQL.py

# All SQL check processes return lists of dict

import logging

from wows_stats.conf import setup_logging, debug_logging, config

def CheckCurrentSeason():

    logger = logging.getLogger(__name__)
    logger.info("started")
    
    config.dbcon.execute(f"CALL usp_CurrentSeason")
    ret = config.dbcon.fetchone()
    return(ret['Season'])

def CheckWatchedClans():

    logger = logging.getLogger(__name__)
    logger.info("started")

    config.dbcon.execute(f"CALL usp_getWatchedClans")
    ret = []
    for t in config.dbcon:
        ret.append(t)
    return(ret)

def CheckTrackedClans():

    logger = logging.getLogger(__name__)
    logger.info("started")

    config.dbcon.execute(f"CALL usp_getTrackedClans")
    ret = []
    for t in config.dbcon:
        ret.append(t)
    return(ret)

def CheckCBStats():

    logger = logging.getLogger(__name__)
    logger.info("started RECHECK")

    sql = f"CALL usp_StatsRecheck"
    logger = logging.getLogger(__name__)
    logger.debug(f"{sql}")
    config.dbcon.execute(sql)
    ret = []
    for t in config.dbcon:
        ret.append(t)

    logger.debug(f"{ret}")

    return(ret)

def CheckRandomStatsToUpdate():

    logger = logging.getLogger(__name__)
    logger.info("started")

    config.dbcon.execute(f"CALL usp_GetPlayersToUpdateRandomStats")
    ret = []
    for t in config.dbcon:
        ret.append(t)
    return(ret)

def CheckPlayersToUpdate():

    logger = logging.getLogger(__name__)
    logger.info("started")

    config.dbcon.execute(f"CALL usp_GetPlayersToUpdate")
    ret = []
    for t in config.dbcon:
        ret.append(t)
    return(ret)

def CheckMissingHistoryClans():

    logger = logging.getLogger(__name__)
    logger.info("started")

    season = CheckCurrentSeason()

    config.dbcon.execute("CALL usp_GetMissingHistoryClans(%s)", (season))
    ret = []
    for t in config.dbcon:
        ret.append(t['ClanID'])
    return(ret)

def CheckPlayersWithNewCBs():

    logger = logging.getLogger(__name__)
    logger.info("started")

    sql = f"CALL usp_GetPlayersWithNewCBs"
    logger = logging.getLogger(__name__)
    logger.debug(f"{sql}")
    config.dbcon.execute(sql)
    ret = []
    for t in config.dbcon:
        ret.append(t)

    logger.debug(f"{ret}")

    return(ret)

def CheckCurrentSeasonClans():

    logger = logging.getLogger(__name__)
    logger.info("started")

    season = CheckCurrentSeason()
        
    config.dbcon.execute("CALL usp_GetAllCurrentClans(%s)", (season))
    ret = []
    for t in config.dbcon:
        ret.append(t['ClanID'])
    return(ret)

def CheckClansToUpdate():
    
    logger = logging.getLogger(__name__)
    logger.info("started")

    config.dbcon.execute(f"CALL usp_GetClansToUpdate")
    ret = []
    for t in config.dbcon:
        ret.append(t)
    return(ret)
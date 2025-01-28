# wowsstats/processes/CSV_GetStats.py

import logging, pandas as pd

from wowsstats.wowsstatslogging import setup_logging, debug_logging

from wowsstats.config import config

def CSV_GetStats():

    logger = logging.getLogger(__name__)
    logger.info("started")
    
    config.dbcon.execute(f"CALL usp_GetLineups('AONO',26)")
    Lineups = []
    for t in config.dbcon:
        Lineups.append(t)

    df = pd.DataFrame(Lineups)
    df.to_csv('Lineups.csv', index=False)

    config.dbcon.execute(f"CALL usp_GetLivedamageAVG('AONO',26)")
    AvgDam = []
    for t in config.dbcon:
        AvgDam.append(t)

    df = pd.DataFrame(AvgDam)
    df.to_csv('AvgDam.csv', index=False)
    
    config.dbcon.execute(f"CALL usp_GetLivedamage(26)")
    LiveDam = []
    for t in config.dbcon:
        LiveDam.append(t)

    df = pd.DataFrame(LiveDam)
    df.to_csv('LiveDam.csv', index=False)

    config.dbcon.execute(f"CALL usp_GetMapWinrates('AONO',26)")
    MapWinrates = []
    for t in config.dbcon:
        MapWinrates.append(t)
    
    df = pd.DataFrame(MapWinrates)
    df.to_csv('MapWinrates.csv', index=False)
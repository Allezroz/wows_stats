# wowsstats/processes/SCRAPE_CBClanHistory.py

from wowsstats.functions import SQLGET_MissingHistoryClans, WEBGET_ClanPreviousSeasons

def SCRAPE_CBClanHistory():
    clans = SQLGET_MissingHistoryClans()
    for c in clans:
        WEBGET_ClanPreviousSeasons(c)
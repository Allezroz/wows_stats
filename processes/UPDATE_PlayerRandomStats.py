# wowsstats/processes/UPDATE_PlayerRandomStats.py

from wowsstats.functions import SQLGET_RandomPlayersToUpdate, WEBGET_PlayerRandomStats

def UPDATE_PlayerRandomStats():
    tst = SQLGET_RandomPlayersToUpdate()
    for p in tst:
        stat = WEBGET_PlayerRandomStats(p['PlayerID'],p['realm'])
# wowsstats/processes/UPDATE_TrackedClans.py

from wowsstats.functions import SQLGET_TrackedClans, BATCH_PlayersFromClan, BATCH_AddPlayersToPlayers

def UPDATE_TrackedClans():

	clans = SQLGET_TrackedClans()
	for c in clans:
	    pl = BATCH_PlayersFromClan(c['clanId'],c['clanRealm'])
	    BATCH_AddPlayersToPlayers(pl,c['clanRealm'])
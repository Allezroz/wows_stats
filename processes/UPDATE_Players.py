# wowsstats/processes/UPDATE_Players.py

from wowsstats.functions import SQLGET_PlayersToUpdate, WEBGET_Player

def UPDATE_Players():

	players = SQLGET_PlayersToUpdate()
	for p in players:
		print(p)
		WEBGET_Player(p['playerID'],p['realm'])
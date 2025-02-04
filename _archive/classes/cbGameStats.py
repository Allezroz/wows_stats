# wowsstats/classes/cbGameStats.py

import logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging

from wowsstats.config import config

class cbGameStats():

    def __init__(
        self,
        PlayerID,
        GameTime,
        Season,
        mainBatteryFrags,
        mainBatteryHits,
        mainBatteryShots,
        artAgro,
        shipsSpotted,
        secondBatteryFrags,
        secondBatteryHits,
        secondBatteryShots,
        survivedBattles,
        droppedCapturePoints,
        torpedoAgro,
        draws,
        controlCapturedPoints,
        planesKilled,
        battles,
        survivedWins,
        frags,
        damageScouting,
        capturePoints,
        rammingFrags,
        torpedoesFrags,
        torpedoesHits,
        torpedoesShots,
        aircraftFrags,
        teamCapturePoints,
        controlDroppedPoints,
        wins,
        losses,
        damageDealt,
        teamDroppedCapturePoints,
        Priority
    ):

        self.PlayerID = int(PlayerID)
        self.GameTime = GameTime
        self.Season = int(Season)
        self.mainBatteryFrags = int(mainBatteryFrags)
        self.mainBatteryHits = int(mainBatteryHits)
        self.mainBatteryShots = int(mainBatteryShots)
        self.artAgro = int(artAgro)
        self.shipsSpotted = int(shipsSpotted)
        self.secondBatteryFrags = int(secondBatteryFrags)
        self.secondBatteryHits = int(secondBatteryHits)
        self.secondBatteryShots = int(secondBatteryShots)
        self.survivedBattles = int(survivedBattles)
        self.droppedCapturePoints = int(droppedCapturePoints)
        self.torpedoAgro = int(torpedoAgro)
        self.draws = int(draws)
        self.controlCapturedPoints = int(controlCapturedPoints)
        self.planesKilled = int(planesKilled)
        self.battles = int(battles)
        self.survivedWins = int(survivedWins)
        self.frags = int(frags)
        self.damageScouting = int(damageScouting)
        self.capturePoints = int(capturePoints)
        self.rammingFrags = int(rammingFrags)
        self.torpedoesFrags = int(torpedoesFrags)
        self.torpedoesHits = int(torpedoesHits)
        self.torpedoesShots = int(torpedoesShots)
        self.aircraftFrags = int(aircraftFrags)
        self.teamCapturePoints = int(teamCapturePoints)
        self.controlDroppedPoints = int(controlDroppedPoints)
        self.wins = int(wins)
        self.losses = int(losses)
        self.damageDealt = int(damageDealt)
        self.teamDroppedCapturePoints = int(teamDroppedCapturePoints)
        self.Priority = int(Priority)

    def __str__(self):

        return (
            f"{self.PlayerID} | "
            f"{self.GameTime} | "
            f"{self.Season} | "
            f"{self.mainBatteryFrags} | "
            f"{self.mainBatteryHits} | "
            f"{self.mainBatteryShots} | "
            f"{self.artAgro} | "
            f"{self.shipsSpotted} | "
            f"{self.secondBatteryFrags} | "
            f"{self.secondBatteryHits} | "
            f"{self.secondBatteryShots} | "
            f"{self.survivedBattles} | "
            f"{self.droppedCapturePoints} | "
            f"{self.torpedoAgro} | "
            f"{self.draws} | "
            f"{self.controlCapturedPoints} | "
            f"{self.planesKilled} | "
            f"{self.battles} | "
            f"{self.survivedWins} | "
            f"{self.frags} | "
            f"{self.damageScouting} | "
            f"{self.capturePoints} | "
            f"{self.rammingFrags} | "
            f"{self.torpedoesFrags} | "
            f"{self.torpedoesHits} | "
            f"{self.torpedoesShots} | "
            f"{self.aircraftFrags} | "
            f"{self.teamCapturePoints} | "
            f"{self.controlDroppedPoints} | "
            f"{self.wins} | "
            f"{self.losses} | "
            f"{self.damageDealt} | "
            f"{self.teamDroppedCapturePoints} | "
            f"{self.Priority}"
        )

    def load(self):

        sql = (
            f"CALL usp_UpdateCBGameStats("
            f"{self.PlayerID}, "
            f"'{self.GameTime}', "
            f"{self.Season}, "
            f"{self.battles}, "
            f"{self.wins}, "
            f"{self.losses}, "
            f"{self.draws}, "
            f"{self.survivedBattles}, "
            f"{self.survivedWins}, "
            f"{self.damageDealt}, "
            f"{self.frags}, "
            f"{self.mainBatteryFrags}, "
            f"{self.secondBatteryFrags}, "
            f"{self.torpedoesFrags}, "
            f"{self.aircraftFrags}, "
            f"{self.rammingFrags}, "
            f"{self.mainBatteryShots}, "
            f"{self.secondBatteryShots}, "
            f"{self.torpedoesShots}, "         
            f"{self.mainBatteryHits}, "
            f"{self.secondBatteryHits}, "
            f"{self.torpedoesHits}, "     
            f"{self.artAgro}, "
            f"{self.torpedoAgro}, "
            f"{self.shipsSpotted}, "
            f"{self.damageScouting}, "
            f"{self.planesKilled}, "           
            f"{self.droppedCapturePoints}, "
            f"{self.capturePoints}, "
            f"{self.controlCapturedPoints}, "
            f"{self.controlDroppedPoints}, "         
            f"{self.teamCapturePoints}, "
            f"{self.teamDroppedCapturePoints},"
            f"{self.Priority}"
            f")"
            )

        logger = logging.getLogger(__name__)
        logger.debug(sql)
        config.dbcon.execute(sql)
        return config.dbcon.fetchone()["Outcome"]
        
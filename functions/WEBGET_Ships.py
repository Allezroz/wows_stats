# wowsstats/functions/WEBGET_Ships.py

# 1 single non-appID API call

import logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging
from wowsstats.functions.WEBGET_API import WEBGET_API
from wowsstats.classes import Ship

def WEBGET_Ships():

    logger = logging.getLogger(__name__)
    logger.info("started")

    ship_class_mapping = {
        "Destroyer": "DD",
        "Cruiser": "CA",
        "Battleship": "BB",
        "Submarine": "SS",
        "AirCarrier": "CV"
    }

    url = "http://vortex.worldofwarships.eu/api/encyclopedia/en/vehicles/"
    logger.debug(f"Requesting URL: {url}") 
    ships = WEBGET_API(url)
    ships = ships["data"]
    logger.info(f"Fetched {len(ships)} ships from API")
    for SID in ships:
        ship = Ship(
            int(SID),  # ID
            ships[SID]["localization"]["mark"]["en"],  # name
            ships[SID]["localization"]["shortmark"]["en"],  # shortname
            int(ships[SID]["level"]),  # Tier
            ship_class_mapping.get(ships[SID]["tags"][0], "Unknown"),  # class
            ships[SID]["nation"]  # nation
        )

        ship.load()

    return ship

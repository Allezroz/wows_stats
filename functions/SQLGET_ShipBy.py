# wowsstats/functions/SQLGET_ShipBy.py

import logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging

from wowsstats.classes.Ship import Ship

from wowsstats.config import config

def SQLGET_ShipBy(by, val):

    logger = logging.getLogger(__name__)
    logger.info("started")

    assert by in ("id", "name"), "'by' must be 'id' or 'name'"

    if by == "id":

        try:
            val = int(val)
        except ValueError:
            print("id must be numeric")
        config.dbcon.execute(f"CALL usp_SQLGET_ShipByByID({val})")

    elif by == "name":

        try:
            val = str(val)
        except ValueError:
            print("name must be a string")
        # not sure how robust this is. We need a universal string escape solution i think ?
        val = val.replace("'", "''")
        config.dbcon.execute(f"CALL usp_SQLGET_ShipByByName({val})")

    tmp = config.dbcon.fetchone()

    if not bool(tmp):

        print(f"Ship {by} {val} not found")
        ret = Ship(-1, -1, -1, -1, -1, -1)

    else:

        ret = Ship(tmp["shipID"], tmp["shipName"], tmp["shortName"],
                   tmp["Tier"], tmp["Class"], tmp["Nation"])

    return(ret)
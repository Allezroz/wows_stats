# wowsstats/processes/SCHED_Weekly.py

import logging

from wowsstats.processes import UPDATE_TrackedClans
from wowsstats.wowsstatslogging import setup_logging, debug_logging

def SCHED_Weekly():

    logger = logging.getLogger(__name__)
    logger.info("started")

    UPDATE_TrackedClans()
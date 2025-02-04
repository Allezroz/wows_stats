# wowsstats/functions/WEBGET_IMPROPER.py


import urllib3, logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging

# improper API call
# does seem to give "status error" on wrong query but no status "ok" on correct query
def WEBGET_API_IMPROPER(url):

    logger = logging.getLogger(__name__)
    logger.debug(f"{url}")

    result = urllib3.request("GET",url).json()

    # todo: add error handling
    # additional information: no status key on OK return, only status key on error (thx WG)
    
    return result
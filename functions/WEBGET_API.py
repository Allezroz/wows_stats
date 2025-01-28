# wowsstats/functions/WEBGET_API.py

import urllib3, logging

from wowsstats.wowsstatslogging import setup_logging, debug_logging

# proper API call
# always gives status "ok" or "error"
def WEBGET_API(url):

    logger = logging.getLogger(__name__)
    logger.debug(f"{url}")
    #result = requests.get(url,headers={"Connection":"close"}).json()
    result = urllib3.request("GET",url).json()
    if result["status"] == "ok":
        logger.debug(f"recieved json with keys {list(result.keys())} 'status': ok")
    elif result["status"] == "error":
        logger.error(f"recieved json with error - {result}")  
    elif result == {}:
        logger.debug(f"recieved empty json")
    return result
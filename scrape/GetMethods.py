# /wows_stats/scrape/GetMethods.py

import urllib3, logging, requests as req

from wows_stats.conf import setup_logging, debug_logging

# proper API call
# always gives status "ok" or "error"

def APIGet(url):

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

# improper API call
# does seem to give "status error" on wrong query but no status "ok" on correct query
def WG_APIGet(url):

    logger = logging.getLogger(__name__)
    logger.debug(f"{url}")

    result = urllib3.request("GET",url).json()

    # todo: add error handling
    # additional information: no status key on OK return, only status key on error (thx WG)
    
    return result

def WebGet(url, cookies):

    logger = logging.getLogger(__name__)
    logger.debug(f"{url}")

    try:
        result = req.get(url, cookies=cookies).json()
    except:
        result = {}
        logger.debug(f"No games at {url}")
    return [result]

def RealmMap(Realm):
    RealmMap = {"eu":"eu", "us":"com", "ru":"ru", "sg":"asia"} # I can't remember if asia is SEA or asia or what.
    return(RealmMap[Realm])
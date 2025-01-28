# wowsstats/functions/SqlWrap.py

from wowsstats.wowsstatslogging import setup_logging, debug_logging

def SqlWrap(f):
    if f is None:
        return('NULL')
    if type(f) == str:
        return("'" + str(f) + "'")
    else:
        return(f)
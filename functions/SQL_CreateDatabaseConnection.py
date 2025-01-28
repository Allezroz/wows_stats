# wowsstats/functions/SQL_CreateDatabaseConnection.py

import pymysql
from pathlib import Path

from wowsstats.agentcreds import environment
from wowsstats.config import config

def CreateDatabaseConnection():
    creds = environment[config.env]
    conn = pymysql.connect(host=creds["IP"],
                           user=creds["user"],
                           password=creds["password"],
                           database=creds["database"],
                           cursorclass=pymysql.cursors.DictCursor)
    return(conn.cursor())
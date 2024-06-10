# wows_stats/conf/CreateDatabaseConnection.py

import pymysql
from pathlib import Path

def CreateDatabaseConnection(creds):
    conn = pymysql.connect(host=creds["IP"],
                           user=creds["user"],
                           password=creds["password"],
                           database=creds["database"],
                           cursorclass=pymysql.cursors.DictCursor)
    return(conn.cursor())
# wows_stats/wowsstats_logging.py

import pymysql
import json

from pydantic import TypeAdapter
from typing import Union,List

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
from fastapi.requests import Request
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.wsgi import WSGIMiddleware

from web import dash_app
from config import GameResult, CBGame, Clan, CBMapStats, environment, Ship

import urllib3


'''
    Maps

'''

http = urllib3.PoolManager()

tags_metadata = [
    {
        "name": "Clans",
        "description": "Data pertaining to see and specifically tracked clans.",
    },
    {
        "name": "CB Data",
        "description": "Data pertaining to Clan Battle games.",
    },
    
    {
        "name" : "WG API",
        "description" : "Gateway setup for vendor API"

    }
]

exceptions_map = {
    400 : "Bad Request",
    401 : "Unauthorised",
    403 : "Forbidden",
    404 : "Not Found",
    409 : "Resource Exists"
    }

RealmMap = {
    "eu":"eu", 
    "us":"com", 
    "ru":"ru", 
    "sg":"asia"
    }

'''
    API

'''

app = FastAPI(
    title="WoWS Stats",
    version="0.1.n",
    openapi_tags=tags_metadata)

def CreateConn():
    creds = environment["dev"]
    conn = pymysql.connect(host=creds["IP"],
                           user=creds["user"],
                           password=creds["password"],
                           database=creds["database"],
                           cursorclass=pymysql.cursors.DictCursor)
    return(conn)

appID = environment['dev']['appid']

def HandleExcept(num : int, detail):
    raise HTTPException(
            status_code = num,
            detail = str(detail),
            headers = {"status": exceptions_map.get(num,"Unknown Code")},
        )

'''
    Endpoints
'''

@app.get("/", include_in_schema=False)
def main():
    return RedirectResponse(url="/docs")

'''
    CB Info
'''

@app.put("/cb/game", tags = ["CB Data"])
def Write_CBGame(game:CBGame):
    conn=CreateConn()
    db = conn.cursor()

    try:
        db.execute("CALL usp_UpdateCBGames(%s,%s,%s,%s,%s,%s)", (game.GameID, game.MapID, game.Season, game.ClusterID, game.ArenaID, game.FinishedAt))
    except pymysql.Error as e:
        conn.close()
        HandleExcept(400, e)

    content = db.fetchall()
    conn.close()

    if content[0]["Outcome"]=="Exists":
        HandleExcept(409, ("Record Exists : " + str(game)))    
    else:
        headers = {"status":"OK"}
        return JSONResponse(status_code=201, content=jsonable_encoder(content), headers=headers)

@app.get("/cb/mapstats", response_model=List[CBMapStats], tags = ["CB Data"])
def Read_CBMapStats(ClanTag:str,
                        Season:int):
    conn=CreateConn()
    db = conn.cursor()
    try:
        db.execute("CALL usp_GetMapWinrates(%s, %s)",(ClanTag, Season))
    except pymysql.Error as e:
        conn.close()
        HandleExcept(400, e)

    content = db.fetchall()
    conn.close()

    if len(content) == 0:
        HandleExcept(204, ("Returned no content"))
    else:
        ta = TypeAdapter(List[CBMapStats])
        ret = ta.validate_python(content)
        headers = {"status":"OK", "records":str(len(ret))}
        return JSONResponse(status_code=200, content=jsonable_encoder(ret), headers=headers)

@app.get("/cb/gamelist",response_model=List[GameResult], tags = ["CB Data"])
def Read_CBGameList(ClanTag:str, Season:int):
    conn=CreateConn()
    db = conn.cursor()
    try:
        db.execute("CALL usp_GetGameList(%s, %s)",(ClanTag, Season))
    except pymysql.Error as e:
        conn.close()
        HandleExcept(400, e)
    content = db.fetchall()
    conn.close()

    if len(content) == 0:
        HandleExcept(204, ("Returned no content"))
    else:
        ta = TypeAdapter(List[GameResult])
        ret = ta.validate_python(content)
        headers = {"status":"OK", "records":str(len(ret))}
        return JSONResponse(status_code=200, content=jsonable_encoder(ret), headers=headers)


'''
    Clan Info
'''

@app.get("/clans/tracked", response_model=List[Clan], include_in_schema=False, tags = ["Clans"])
def Read_TrackedClans():
    conn = CreateConn()
    db = conn.cursor()
    try:
        db.execute("CALL usp_getTrackedClans")
    except pymysql.Error as e:
        conn.close()
        HandleExcept(400, e)

    content = db.fetchall()
    conn.close()

    if len(content) == 0:
        HandleExcept(204, ("Returned no content"))
    else:
        ta = TypeAdapter(List[TrackedClan])
        ret = ta.validate_python(content)
        headers = {"status":"OK", "records":str(len(ret))}
        return JSONResponse(status_code=200, content=jsonable_encoder(ret), headers=headers)

@app.get("/clans/watched", response_model=List[Clan], tags = ["Clans"])
def Read_WatchedClans():
    conn=CreateConn()
    db = conn.cursor()
    try:
        db.execute("CALL usp_getWatchedClans")
    except pymysql.Error as e:
        conn.close()
        HandleExcept(400, e)
        
    content = db.fetchall()
    conn.close()

    if len(content) == 0:
        HandleExcept(204, ("Returned no content"))
    else:
        ta = TypeAdapter(List[Clan])
        ret = ta.validate_python(content)
        headers = {"status":"OK", "records":str(len(ret))}
        return JSONResponse(status_code=200, content=jsonable_encoder(ret), headers=headers)

@app.get("/clans/toupdate", response_model=List[Clan], tags = ["Clans"])
def Read_ClansToUpdate():
    conn=CreateConn()
    db = conn.cursor()
    try:
        db.execute("CALL usp_GetClansToUpdate")
    except pymysql.Error as e:
        conn.close()
        HandleExcept(400, e)
        
    content = db.fetchall()
    conn.close()

    if len(content) == 0:
        HandleExcept(204, ("Returned no content"))
    else:
        ta = TypeAdapter(List[Clan])
        ret = ta.validate_python(content)
        headers = {"status":"OK", "records":str(len(ret))}
        return JSONResponse(status_code=200, content=jsonable_encoder(ret), headers=headers)


'''
    External API Passthrough
'''

@app.get("/wg/ships", response_model = List[Ship], tags=["WG API"])
def WG_ShipData():
    ship_class_mapping = {
        "Destroyer": "DD",
        "Cruiser": "CA",
        "Battleship": "BB",
        "Submarine": "SS",
        "AirCarrier": "CV"
    }

    url = "http://vortex.worldofwarships.eu/api/encyclopedia/en/vehicles/"
    
    try:
        req = http.request("GET",url)
        content = req.json()["data"]
    except:
        HandleExcept(400, ("API Error at : "+url))
        
    if len(content) == 0:
        HandleExcept(204, (url + " returned no content"))
    
    ret = []
    for SID in content:
        ship = Ship(
            ShipID = int(SID),  # ID
            ShipName = content[SID]["localization"]["mark"]["en"],  # name
            ShortName = content[SID]["localization"]["shortmark"]["en"],  # shortname
            Tier = int(content[SID]["level"]),  # Tier
            Class = ship_class_mapping.get(content[SID]["tags"][0], "Unknown"),  # class
            Nation = content[SID]["nation"]  # nation
        )
        ret.append(ship)

    headers = {"status":"OK", "records":str(len(ret))}
    return JSONResponse(status_code=200, content=jsonable_encoder(ret), headers=headers)


@app.get("/wg/clanbattles", response_model=List[CBGame], tags=["WG API"])
def WG_ClanBattle(tag : str):

    conn=CreateConn()
    db = conn.cursor()
    try:
        db.execute("CALL usp_GetToken(%s)", tag)
    except pymysql.Error as e:
        conn.close()
        HandleExcept(400, e)

    tkn = db.fetchall()
    conn.close()

    if len(tkn) == 0:
        HandleExcept(404, "{tag} Not Tracked")

    token = tkn[0]['Token']

    headers = urllib3.HTTPHeaderDict({
        'Cookie': f'wsauth_token={token}'
    })

    realm = RealmMap[tkn[0]['Realm']]
    ratings = [1, 2]

    ret = []

    for rating in ratings:
        url = f"https://clans.worldofwarships.{realm}/api/ladder/battles/?team={rating}"
        try:
            req = http.request("GET", url, headers=headers)
            response = req.json()

            for game in response:
                ret.append(CBGame.model_validate(game))
        except:
           print("Failure?")
           print(game)

    headers = {"status":"OK", "records":str(len(ret))}
    return JSONResponse(status_code=200, content=jsonable_encoder(ret), headers=headers)
    





'''
    Dashboard Elements
'''

app.mount("/mapStats", WSGIMiddleware(dash_app.server))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

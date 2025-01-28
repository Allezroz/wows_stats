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
from config import GameResult, CBGame, Clan, TrackedClan, CBMapStats, environment


'''
Tags

'''

tags_metadata = [
    {
        "name": "Clans",
        "description": "Data pertaining to see and specifically tracked clans.",
    },
    {
        "name": "CB Data",
        "description": "Data pertaining to Clan Battle games.",
    },
]


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


'''
    Endpoints
'''

@app.get("/", include_in_schema=False)
def main():
    return RedirectResponse(url="/docs")

'''
    CB Info
'''

@app.put("/cb/games", tags = ["CB Data"])
def Write_CB_Games(game:CBGame):
    conn=CreateConn()
    db = conn.cursor()
    try:
        db.execute("CALL usp_UpdateCBGames(%s,%s,%s,%s,%s,%s)", (game.GameID, game.MapID, game.Season, game.ClusterID, game.ArenaID, game.FinishedAt))
    except:
        conn.close()
        raise HTTPException(
            status_code=400,
            detail="Bad Request",
            headers={"status": "Bad Request"},
        )       
    content = db.fetchall()
    conn.close()

    if len(content) == 0:
        raise HTTPException(
            status_code=204,
            detail="No Content",
            headers={"status": "No Content"}
        )
    elif content[0]["Outcome"]=="Exists":
        raise HTTPException(
            status_code=409,
            detail=jsonable_encoder(content),
            headers={"status": "Exists"},
        )        
    else:
        headers = {"status":"OK"}
        return JSONResponse(status_code=201, content=jsonable_encoder(content), headers=headers)

@app.get("/cb/mapstats", response_model=List[CBMapStats], tags = ["CB Data"])
def Read_CB_Map_Stats(ClanTag:str,
                        Season:int):
    conn=CreateConn()
    db = conn.cursor()
    try:
        db.execute("CALL usp_GetMapWinrates(%s, %s)",(ClanTag, Season))
    except:
        conn.close()
        raise HTTPException(
            status_code=400,
            detail="Bad Request",
            headers={"status": "Bad Request"},
        )
    content = db.fetchall()
    conn.close()

    if len(content) == 0:
        raise HTTPException(
            status_code=204,
            detail="No Content",
            headers={"status": "No Content"},
        )
    else:
        ta = TypeAdapter(List[CBMapStats])
        ret = ta.validate_python(content)
        headers = {"status":"OK", "records":str(len(ret))}
        return JSONResponse(status_code=200, content=jsonable_encoder(ret), headers=headers)

@app.get("/cb/gamelist",response_model=List[GameResult], tags = ["CB Data"])
def Read_CB_Game_List(ClanTag:str, Season:int):
    conn=CreateConn()
    db = conn.cursor()
    try:
        db.execute("CALL usp_GetGameList(%s, %s)",(ClanTag, Season))
    except:
        conn.close()
        raise HTTPException(
            status_code=400,
            detail="Bad Request",
            headers={"status": "Bad Request"},
        )
    content = db.fetchall()
    conn.close()

    if len(content) == 0:
        raise HTTPException(
            status_code=204,
            detail="No Content",
            headers={"status": "No Content"},
        )
    else:
        ta = TypeAdapter(List[GameResult])
        ret = ta.validate_python(content)
        headers = {"status":"OK", "records":str(len(ret))}
        return JSONResponse(status_code=200, content=jsonable_encoder(ret), headers=headers)


'''
    Clan Info
'''

@app.get("/clans/tracked", response_model=List[TrackedClan], include_in_schema=False, tags = ["Clans"])
def Read_Tracked_Clans():
    conn=CreateConn()
    db = conn.cursor()
    try:
        db.execute("CALL usp_getTrackedClans")
    except:
        conn.close()
        raise HTTPException(
            status_code=400,
            detail="Bad Request",
            headers={"status": "Bad Request"},
        )
    content = db.fetchall()
    conn.close()

    if len(content) == 0:
        raise HTTPException(
            status_code=204,
            detail="No Content",
            headers={"status": "No Content"},
        )
    else:
        ta = TypeAdapter(List[TrackedClan])
        ret = ta.validate_python(content)
        headers = {"status":"OK", "records":str(len(ret))}
        return JSONResponse(status_code=200, content=jsonable_encoder(ret), headers=headers)

@app.get("/clans/watched", response_model=List[Clan], tags = ["Clans"])
def Read_Watched_Clans():
    conn=CreateConn()
    db = conn.cursor()
    try:
        db.execute("CALL usp_getWatchedClans")
    except:
        conn.close()
        raise HTTPException(
            status_code=400,
            detail="Bad Request",
            headers={"status": "Bad Request"},
        )
    content = db.fetchall()
    conn.close()

    if len(content) == 0:
        raise HTTPException(
            status_code=204,
            detail="No Content",
            headers={"status": "No Content"},
        )
    else:
        ta = TypeAdapter(List[Clan])
        ret = ta.validate_python(content)
        headers = {"status":"OK", "records":str(len(ret))}
        return JSONResponse(status_code=200, content=jsonable_encoder(ret), headers=headers)

@app.get("/clans/toupdate", response_model=List[Clan], tags = ["Clans"])
def Read_Clans_To_Update():
    conn=CreateConn()
    db = conn.cursor()
    try:
        db.execute("CALL usp_GetClansToUpdate")
    except:
        conn.close()
        raise HTTPException(
            status_code=400,
            detail="Bad Request",
            headers={"status": "Bad Request"},
        )
    content = db.fetchall()
    conn.close()

    if len(content) == 0:
        raise HTTPException(
            status_code=204,
            detail="No Content",
            headers={"status": "No Content"},
        )
    else:
        ta = TypeAdapter(List[Clan])
        ret = ta.validate_python(content)
        headers = {"status":"OK", "records":str(len(ret))}
        return JSONResponse(status_code=200, content=jsonable_encoder(ret), headers=headers)
'''
    Dashboard Elements
'''

app.mount("/mapStats", WSGIMiddleware(dash_app.server))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

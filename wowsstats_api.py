# wows_stats/wowsstats_logging.py

import pymysql
import json
import time

from pydantic import TypeAdapter
from typing import Union,List,Literal

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
from fastapi.requests import Request
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.wsgi import WSGIMiddleware

from web import dash_app
from config import GameResult, CBGame, Clan, CBMapStats, environment, Ship, CBTeam, CBPlayer, Map, Season, PlayerRandomStats, Player, LiveDamage, ClanRating, CBPlayerStats

import urllib3

#todo: IP filter middleware on PUTs
#todo: logger logging
#todo: performance management middleware
'''
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
'''

'''
    Maps

'''

http = urllib3.PoolManager()

TagsMetadata = [
    {
        "name": "Clans",
        "description": "Data pertaining to see and specifically tracked clans.",
    },
    {
        "name": "CB Data",
        "description": "Data pertaining to Clan Battle games.",
    },
    {
        "name": "Reference Data",
        "description": "Vendor-sourced lookup/reference data.",        
    },
    {
        "name" : "WG API",
        "description" : "Gateway setup for vendor API"
    }
]

ExceptionsMap = {
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

IPWhitelist = environment['dev']['ip_whitelist']
appID = environment['dev']['appid']

'''
    API

'''

app = FastAPI(
    title="WoWS Stats",
    version="0.1.n",
    openapi_tags=TagsMetadata)

def CreateConn():
    conn = pymysql.connect(host=creds["IP"],
                           user=creds["user"],
                           password=creds["password"],
                           database=creds["database"],
                           cursorclass=pymysql.cursors.DictCursor)
    return(conn)



def HandleExcept(num : int, detail):
    raise HTTPException(
            status_code = num,
            detail = str(detail),
            headers = {"status": ExceptionsMap.get(num,"Unknown Code")},
        )

'''
    Middlewares
'''

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    ip = str(request.client.host)
    if ip not in IPWhitelist:
        data = {
            'message': f'IP {ip} is not allowed to access this resource.'
        }
        return JSONResponse(status_code=400, content=data)
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

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


@app.put("/cb/team", tags = ["CB Data"])
def Write_CBTeam(GameID:int, Team:CBTeam):
    conn=CreateConn()
    db = conn.cursor()

    try:
        db.execute("CALL usp_UpdateCBTeams(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", 
            (GameID, Team.TeamID, Team.ClanID, Team.claninfo.Realm, Team.TeamAB, Team.League, Team.Division, Team.Rating, Team.RatingDelta, Team.Result))
    except pymysql.Error as e:
        conn.close()
        HandleExcept(400, e)

    content = db.fetchall()
    conn.close()

    if content[0]["Outcome"]=="Exists":
        HandleExcept(409, ("Record Exists : " + str(Team)))    
    else:
        headers = {"status":"OK"}
        return JSONResponse(status_code=201, content=jsonable_encoder(content), headers=headers)


@app.put("/cb/player", tags = ["CB Data"])
def Write_CBPlayer(player:CBPlayer, realm:Literal['eu','us','sg','ru']):
    conn=CreateConn()
    db = conn.cursor()

    try:
        db.execute("CALL usp_UpdateCBPlayers(%s,%s,%s,%s,%s)", (player.TeamID, player.PlayerID, player.ShipID, player.Survived, realm))
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
    Reference Tables

     sql = (f"CALL usp_UpdateMaps({self.MapID}, '{self.MapName}', '{self.MapImage}')")
        sql = f"CALL usp_UpdateShip({self.shipID},'{self.shipName}','{self.shortName}',{self.Tier},'{self.Class}','{self.Nation}')"
'''

@app.put("/ref/ships", tags = ["Reference Data"])
def Write_Ship(ship:Ship):
    conn=CreateConn()
    db = conn.cursor()

    try:
        db.execute("CALL usp_UpdateShip(%s,%s,%s,%s,%s, %s)", (ship.ShipID, ship.ShipName, ship.ShortName, ship.Tier, ship.Class, ship.Nation))
    except pymysql.Error as e:
        conn.close()
        HandleExcept(400, e)

    content = db.fetchall()
    conn.close()

    if content[0]["Outcome"]=="Exists":
        HandleExcept(409, ("Record Exists : " + str(ship)))    
    else:
        headers = {"status":"OK"}
        return JSONResponse(status_code=201, content=jsonable_encoder(content), headers=headers)

@app.put("/ref/maps", tags = ["Reference Data"])
def Write_MapData(m:Map):
    conn=CreateConn()
    db = conn.cursor()

    try:
        db.execute("CALL usp_UpdateMaps(%s,%s,%s)", (m.MapID, m.MapName, m.Icon))
    except pymysql.Error as e:
        conn.close()
        HandleExcept(400, e)

    content = db.fetchall()
    conn.close()

    if content[0]["Outcome"]=="Exists":
        HandleExcept(409, ("Record Exists : " + str(m)))    
    else:
        headers = {"status":"OK"}
        return JSONResponse(status_code=201, content=jsonable_encoder(content), headers=headers)

@app.put("/ref/seasons", tags = ["Reference Data"])
def Write_SeasonData(season:Season):
    conn=CreateConn()
    db = conn.cursor()

    try:
        db.execute("CALL usp_UpdateSeasons(%s,%s,%s,%s,%s,%s,%s)", (season.SeasonNumber, season.SeasonName, season.MinTier, season.MaxTier, season.StartDate, season.EndDate, season.DivisionPoints))
    except pymysql.Error as e:
        conn.close()
        HandleExcept(400, e)

    content = db.fetchall()
    conn.close()

    if content[0]["Outcome"]=="Exists":
        HandleExcept(409, ("Record Exists : " + str(m)))    
    else:
        headers = {"status":"OK"}
        return JSONResponse(status_code=201, content=jsonable_encoder(content), headers=headers)

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

@app.get("/wg/seasons", response_model = List[Season], tags=["WG API"])
def WG_SeasonData():

    url = f"https://api.worldofwarships.eu/wows/clans/season/?application_id={appID}"
    
    try:
        req = http.request("GET",url)
        content = req.json()["data"]
    except:
        HandleExcept(400, ("API Error at : "+url))
        
    if len(content) == 0:
        HandleExcept(204, (url + " returned no content"))
    
    ret = []
    for season in content:
        #print(content.get(season))
        ret.append(Season.model_validate(content.get(season)))

    headers = {"status":"OK", "records":str(len(ret))}
    return JSONResponse(status_code=200, content=jsonable_encoder(ret), headers=headers)

@app.get("/wg/maps", response_model = List[Map], tags=["WG API"])
def WG_MapData():

    url = f"https://api.worldofwarships.eu/wows/encyclopedia/battlearenas/?application_id={appID}"
    
    try:
        req = http.request("GET",url)
        content = req.json()["data"]
    except:
        HandleExcept(400, ("API Error at : "+url))
        
    if len(content) == 0:
        HandleExcept(204, (url + " returned no content"))
    
    ret = []
    for m in content:
        ret.append(Map.model_validate(content.get(m)))

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
            content = req.json()

            for game in content:
                ret.append(CBGame.model_validate(game))
        except:
           print("Failure?")
           print(game)

    headers = {"status":"OK", "records":str(len(ret))}
    return JSONResponse(status_code=200, content=jsonable_encoder(ret), headers=headers)
    
@app.get("/wg/randomstats", response_model = List[PlayerRandomStats], tags=["WG API"])
def WG_PlayerRandomStats(PlayerID: int, Realm: Literal['eu','us','sg','ru']):

    Realm = RealmMap[Realm]

    GameTypes = ['pvp','rank_solo','pvp_solo']

    url = (
            f"https://api.worldofwarships.{Realm}/wows/ships/stats/"
            f"?application_id={appID}"
            f"&account_id={PlayerID}"
            f"&extra=pvp_solo%2C+rank_solo"
            f"&fields=ship_id%2Cpvp.battles%2Cpvp.xp%2Cpvp_solo.xp%2Crank_solo.xp%2Cpvp_solo.battles%2Crank_solo.battles%2C"
            f"pvp.wins%2Cpvp_solo.wins%2Crank_solo.wins%2Cpvp.losses%2Cpvp_solo.losses%2Crank_solo.losses%2C"
            f"pvp.draws%2Cpvp_solo.draws%2Crank_solo.draws%2Cpvp.damage_scouting%2Cpvp_solo.damage_scouting%2Crank_solo.damage_scouting%2C"
            f"pvp.survived_battles%2Cpvp_solo.survived_battles%2Crank_solo.survived_battles%2Cpvp.frags%2Cpvp_solo.frags%2Crank_solo.frags%2C"
            f"pvp.damage_dealt%2Cpvp_solo.damage_dealt%2Crank_solo.damage_dealt%2Crank_solo.art_agro%2Crank_solo.torpedo_agro%2C"
            f"pvp_solo.art_agro%2Cpvp_solo.torpedo_agro%2Cpvp.art_agro%2Cpvp.torpedo_agro"
        )
    try:
        req = http.request("GET",url)
        content = req.json()["data"]
    except:
        HandleExcept(400, ("API Error at : " + url))

    if len(content) == 0:
        HandleExcept(204, "API Returned no data for {PlayerID}")
    ret = []
    content = content[str(PlayerID)]
    for ship in content:
        
        for t in GameTypes:
            if ship[t]['battles'] > 0:
                ret.append(PlayerRandomStats(
                    PlayerID = PlayerID,
                    ShipID = ship['ship_id'],
                    Games = ship[t]['battles'],
                    Wins = ship[t]['wins'],
                    Survived = ship[t]['survived_battles'],
                    Frags = ship[t]['frags'],
                    Damage = ship[t]['damage_dealt'],
                    Spotting = ship[t]['damage_scouting'],
                    Tanked = ship[t]['art_agro']+ship[t]['torpedo_agro'],
                    Experience = ship[t]['xp'],
                    MatchType = t
                    ))

    headers = {"status":"OK", "records":str(len(ret))}
    return JSONResponse(status_code=200, content=jsonable_encoder(ret), headers=headers)

# ClanRating
@app.get("/wg/clanratings", response_model=List[ClanRating], tags=["WG API"])
def WG_ClanRating(ClanID: int, Realm: str):

    Realm = RealmMap[Realm]

    url = f"https://clans.worldofwarships.{Realm}/api/clanbase/{ClanID}/claninfo/"

    try:
        req = http.request("GET",url)
        content = req.json()
    except:
        HandleExcept(400, ("API Error at : " + url))

    if len(content) == 0:
        HandleExcept(204, "API Returned no data for {PlayerID}")
    ret = []
    content = content["clanview"]["wows_ladder"]["ratings"]
    
    for rating in content:
        ret.append(ClanRating(
            ClanID = ClanID,
            Battles = rating["battles_count"],
            League = rating["league"],
            MaxPublicRating = rating["max_public_rating"],
            Wins = rating["wins_count"],
            Season = rating["season_number"],
            Rating = rating["public_rating"],
            TeamAB = rating["team_number"],
            IsMaxPosition = rating["is_best_season_rating"]
        ))


    headers = {"status":"OK", "records":str(len(ret))}
    return JSONResponse(status_code=200, content=jsonable_encoder(ret), headers=headers)

# LiveDamage
# CBPlayerStats

# sql = f"CALL usp_UpdatePlayerRandomStats({self.playerID},{self.shipID},{self.Games},{self.WR},{self.Surv},{self.Frags},{self.Dam},{self.Spot},{self.Tank},{self.XP},'{self.MatchType}')"
# config.dbcon.execute(f"CALL usp_UpdatePlayers({self.playerID},{self.clanID},'{self.Nickname}','{self.Realm}',{self.isHidden})")
#sql = (f"CALL usp_UpdateLiveDamage({self.clanID},{self.playerID},{self.Games},{self.Damage},{self.Frags},'{self.last_battle_time}',{self.Season})")

'''
f"CALL usp_UpdateCBGameStats("
            f"{self.PlayerID}, "
            f"'{self.GameTime}', "
            f"{self.Season}, "
            f"{self.battles}, "
            f"{self.wins}, "
            f"{self.losses}, "
            f"{self.draws}, "
            f"{self.survivedBattles}, "
            f"{self.survivedWins}, "
            f"{self.damageDealt}, "
            f"{self.frags}, "
            f"{self.mainBatteryFrags}, "
            f"{self.secondBatteryFrags}, "
            f"{self.torpedoesFrags}, "
            f"{self.aircraftFrags}, "
            f"{self.rammingFrags}, "
            f"{self.mainBatteryShots}, "
            f"{self.secondBatteryShots}, "
            f"{self.torpedoesShots}, "         
            f"{self.mainBatteryHits}, "
            f"{self.secondBatteryHits}, "
            f"{self.torpedoesHits}, "     
            f"{self.artAgro}, "
            f"{self.torpedoAgro}, "
            f"{self.shipsSpotted}, "
            f"{self.damageScouting}, "
            f"{self.planesKilled}, "           
            f"{self.droppedCapturePoints}, "
            f"{self.capturePoints}, "
            f"{self.controlCapturedPoints}, "
            f"{self.controlDroppedPoints}, "         
            f"{self.teamCapturePoints}, "
            f"{self.teamDroppedCapturePoints},"
            f"{self.Priority}"
            f")"
'''


'''
    Dashboard Elements
'''

app.mount("/mapStats", WSGIMiddleware(dash_app.server))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

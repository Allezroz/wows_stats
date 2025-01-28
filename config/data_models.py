# data_models.py

from pydantic import BaseModel
from datetime import datetime
from typing import Literal, Optional

class GameResult(BaseModel):
    Map: str
    Result: int
    Rating: int
    EnemyQuality: str
    EnemyLastLeague: Optional[str] = None
    FinishedAt: datetime
    TeamAB: Literal['A', 'B']

class CBGame(BaseModel):
    GameID : int 
    MapID : int 
    Season : int
    ClusterID : int 
    ArenaID : int
    FinishedAt : datetime

class CBMapStats(BaseModel):
    MapName : str
    ClanTag : str
    TeamAB : Literal['A', 'B']
    Games : int
    Wins : int
    Losses : int
    Winrate : float
    Season : int
    Quality : Literal['Low','Ty1+']

class Clan(BaseModel):
    ClanID : int
    Realm : Literal['eu','us','sg','ru']
    ClanName : Optional[str] = None
    ClanTag : Optional[str] = None

class TrackedClan(BaseModel):
    TrackedClanID : int
    Tag : str
    Realm : Literal['eu','us','sg','ru']
    ClanID : int
    Token : str
    Owner : str
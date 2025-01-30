# data_models.py

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Literal, Optional, List

class GameResult(BaseModel):
    Map: str
    Result: int
    Rating: int
    EnemyQuality: str
    EnemyLastLeague: Optional[str] = None
    FinishedAt: datetime
    TeamAB: Literal['A', 'B']

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
    ClanID : int = Field(alias='id')
    Realm : Literal['eu','us','sg','ru'] = Field(alias='realm')
    ClanName : Optional[str] = Field(None,alias='name')
    ClanTag : Optional[str] = Field(None, alias='tag')

    class Config:
        populate_by_name = True

class Ship(BaseModel):
    ShipID : int
    ShipName : str
    ShortName : str
    Tier : int
    Class : Literal['DD','CV','CA','BB','SS']
    Nation : str

class CBStage(BaseModel):
    type : Literal['promotion','demotion']
    victories_required : int
    battle_result_id : int
    target_public_rating : int
    progress : List[Literal['victory','defeat','draw']]
    target : str
    battles : int
    target_division : int
    target_league : int
    target_division_rating : int
    class Config:
        populate_by_name = True

class CBPlayer(BaseModel):
    PlayerID: int = Field(alias='spa_id')
    nickname: str
    result_id: int
    name: str
    clan_id: int
    survived: bool
    vehicle_id: int
    class Config:
        populate_by_name = True

class CBTeam(BaseModel):
    rating_delta: int
    division_rating: int
    TeamResult: str = Field(alias='result')
    ClanID: int = Field(alias='clan_id')
    claninfo: Clan
    TeamAB: int = Field(alias='team_number')
    League: int = Field(alias='league')
    TeamID: int = Field(alias='id')
    stage: Optional[CBStage] = None
    players: List[CBPlayer]
    Division: int = Field(alias='division')
    class Config:
        populate_by_name = True


class CBGame(BaseModel):
    ArenaID: int = Field(alias='arena_id')
    FinishedAt: datetime = Field(alias='finished_at')
    MapID: int = Field(alias='map_id')
    ClusterID: int = Field(alias='cluster_id')
    Season: int = Field(alias='season_number')
    Teams: List[CBTeam] = Field(alias='teams')
    GameID: int = Field(alias='id')
    GameRealm: str = Field(alias='realm')
    class Config:
        populate_by_name = True

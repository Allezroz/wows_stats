# data_models.py

from pydantic import BaseModel, Field, validator
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
    TeamID : int = Field(alias='result_id')
    Name: str = Field(alias='name')
    clan_id: int
    Survived: bool = Field(alias='survived')
    ShipID: int = Field(alias='vehicle_id')
    class Config:
        populate_by_name = True

class CBTeam(BaseModel):
    RatingDelta: int = Field(alias='rating_delta')
    Rating: int = Field(alias='division_rating')
    TeamResult: str = Field(alias='result')
    Result: int = 0
    ClanID: int = Field(alias='clan_id')
    claninfo: Clan
    TeamAB: int = Field(alias='team_number')
    League: int = Field(alias='league')
    TeamID: int = Field(alias='id')
    stage: Optional[CBStage] = None
    players: List[CBPlayer]
    Division: int = Field(alias='division')

    @validator('Result', pre=True, always=True)
    def set_result_binary(cls, v, values):
        if 'TeamResult' in values:
            return 1 if values['TeamResult'].lower() == 'victory' else 0
        return 0

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

class Map(BaseModel):
    MapID: int = Field(alias='battle_arena_id')
    MapName: str = Field(alias='name')
    Icon: str = Field(alias='icon')

class Season(BaseModel):
    SeasonNumber: int = Field(alias='season_id')
    SeasonName: str = Field(alias='name')
    MinTier: int = Field(alias='ship_tier_min')
    MaxTier: int = Field(alias='ship_tier_max')
    StartDate: datetime = Field(alias='start_time')
    EndDate: datetime = Field(alias='finish_time')
    DivisionPoints: int = Field(alias='division_points')

class PlayerRandomStats(BaseModel):
    PlayerID: int
    ShipID: int
    Games: int
    Wins: int
    Survived: int
    Frags: int
    Damage: int
    Spotting: int
    Tanked: int
    Experience: int
    MatchType: Literal['pvp','rank_solo','pvp_solo']

class Player(BaseModel):
    PlayerID: int
    ClanID: Optional[int] = None
    Nickname: str
    Realm: Literal['eu','us','sg','ru']
    IsHidden: bool
    LastSeen: Optional[datetime] = None

class LiveDamage(BaseModel):
    ClanID: int
    PlayerID: int
    Games: int
    Damage: float
    Frags: float
    LastBattleTime: datetime
    Season: int

class ClanRating(BaseModel):
    ClanID: int
    Battles: int
    League: int
    MaxPublicRating: int
    Wins: int
    Season: int
    Rating: int
    TeamAB: int
    IsMaxPosition: bool

class CBPlayerStats(BaseModel):
    PlayerID: int
    GameTime: datetime
    Season: int
    MBFrags: int
    MBHits: int
    MBShots: int
    MBAggro: int
    ShipsSpotted: int
    SBFrags: int
    SBHits: int
    SBShots: int
    SurvivedBattles: int
    DroppedCapPoints: int
    TorpAggro: int
    Draws: int
    ControlCapturedPoints: int
    PlanesKilled: int
    Battles: int
    SurvivedWins: int
    Frags: int
    SpottingDamage: int
    CapturePoints: int
    RammingFrags: int
    TorpFrags: int
    TorpHits: int
    TorpShots: int
    AircraftFrags: int
    TeamCapturePoints: int
    ControlDroppedPoints: int
    Wins: int
    Losses: int
    DamageDealt: int
    TeamDroppedCapturePoints: int
    Priority: int
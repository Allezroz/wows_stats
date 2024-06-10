create table if not exists CBGameStats
(
    PlayerID          bigint                             null,
    GameTime          datetime                           null,
    Season            int                                null,
    Games             int                                null,
    Wins              int                                null,
    Losses            int                                null,
    Draws             int                                null,
    SurvivedBattles   int                                null,
    SurvivedWins      int                                null,
    Damage            bigint                             null,
    Frags             int                                null,
    MBFrags           int                                null,
    SBFrags           int                                null,
    TorpFrags         int                                null,
    PlaneFrags        int                                null,
    RamFrags          int                                null,
    MBShots           int                                null,
    SBShots           int                                null,
    TorpShots         int                                null,
    MBHits            int                                null,
    SBHits            int                                null,
    TorpHits          int                                null,
    GunTanked         int                                null,
    TorpTanked        int                                null,
    Spots             int                                null,
    SpottingDamage    bigint                             null,
    PlanesKilled      int                                null,
    DroppedCapPts     int                                null,
    CapPts            int                                null,
    ControlCapPts     int                                null,
    ControlDroppedPts int                                null,
    TeamCapPts        int                                null,
    TeamDroppedCapPts int                                null,
    CheckDate         datetime default CURRENT_TIMESTAMP null,
    Priority          int      default 2                 null
);

create index idx_clustered_CBShipStats
    on CBGameStats (PlayerID, Season, Games, GameTime);

create table if not exists CBGames
(
    GameID     bigint                             not null
        primary key,
    MapID      bigint                             null,
    Season     int                                null,
    ClusterID  bigint                             null,
    ArenaID    bigint                             null,
    FinishedAt datetime                           null,
    CheckDate  datetime default CURRENT_TIMESTAMP null
);

create table if not exists CBPlayers
(
    TeamID   bigint     null,
    PlayerID bigint     null,
    ShipID   bigint     null,
    Survived tinyint(1) null,
    Realm    varchar(3) null,
    constraint idx_cbplayers_clustered
        unique (TeamID, PlayerID)
);

create table if not exists CBTeams
(
    GameID      bigint     null,
    TeamID      bigint     not null
        primary key,
    ClanID      bigint     null,
    Realm       varchar(3) null,
    TeamAB      varchar(1) null,
    League      int        null,
    Division    int        null,
    Rating      int        null,
    RatingDelta int        null,
    Result      tinyint(1) null
);

create index idx_cbTeams_clan
    on CBTeams (ClanID);

create index idx_cbTeams_gameid
    on CBTeams (GameID);

create table if not exists ClanHistory
(
    ClanID                    bigint      null,
    Games                     int         null,
    League                    int         null,
    MaxPositionPublicRating   int         null,
    MaxPositionDivisionRating int         null,
    MAXPositionLeague         int         null,
    MAXPositionDivision       int         null,
    Wins                      int         null,
    InitialPublicRating       int         null,
    IsBestSeasonRating        tinyint(1)  null,
    TeamNumber                int         null,
    IsQualified               tinyint(1)  null,
    RatingID                  bigint      null,
    CurrentWinStreak          int         null,
    ActiveStatus              varchar(32) null,
    SeasonNumber              int         null,
    DivisionRatingMax         int         null,
    Realm                     varchar(2)  null,
    DivisionRating            int         null,
    LongestWinningStreak      int         null,
    MaxPublicRating           int         null,
    PublicRating              int         null,
    LastWinAt                 datetime    null,
    Division                  int         null
);

create index idx_clustered_ClanHistory
    on ClanHistory (SeasonNumber, ClanID, RatingID);

create table if not exists Clans
(
    ClanID      bigint unsigned      not null
        primary key,
    ClanName    varchar(256)         null,
    Realm       varchar(3)           null,
    ClanTag     varchar(5)           null,
    IsDisbanded tinyint(1)           null,
    LastUpdated datetime             null,
    LastSeen    datetime             null,
    NeedsUpdate tinyint(1)           null,
    Tracked     tinyint(1) default 0 null
);

create table if not exists LiveDamage
(
    ClanID         bigint                             null,
    PlayerID       bigint                             null,
    Games          int                                null,
    Damage         float                              null,
    Frags          float                              null,
    LastBattleTime datetime                           null,
    CheckTime      datetime default CURRENT_TIMESTAMP not null,
    Season         int                                null
);

create index idx_LiveDamage_clustered
    on LiveDamage (ClanID, PlayerID, Games, LastBattleTime);

create table if not exists Maps
(
    MapID    bigint       null,
    MapName  varchar(64)  null,
    ImageURL varchar(256) null
);

create table if not exists Metas
(
    MetaName varchar(20)     not null
        primary key,
    ShipID   bigint unsigned not null
);

create table if not exists PlayerRandomStats
(
    PlayerID    bigint      not null,
    ShipID      bigint      not null,
    Games       int         null,
    Wins        int         null,
    Survived    int         null,
    Frags       float       null,
    Damage      int         null,
    Spotting    int         null,
    Tanked      int         null,
    XP          int         null,
    MatchType   varchar(16) not null,
    LastUpdated datetime    null,
    primary key (PlayerID, ShipID, MatchType)
);

create table if not exists Players
(
    PlayerID    bigint unsigned not null
        primary key,
    ClanID      bigint unsigned null,
    Nickname    varchar(64)     null,
    Realm       varchar(3)      null,
    IsHidden    tinyint(1)      null,
    LastUpdated datetime        null,
    LastSeen    datetime        null,
    NeedsUpdate tinyint(1)      null
);

create table if not exists Seasons
(
    Season         int         null,
    SeasonName     varchar(64) null,
    MinTier        int         null,
    MaxTier        int         null,
    StartDate      datetime    null,
    EndDate        datetime    null,
    DivisionPoints int         null
);

create table if not exists Sem_NewCBStats
(
    Nickname          varchar(128)   null,
    PlayerClan        varchar(6)     null,
    Season            int            null,
    GameTime          datetime       null,
    GameDay           date           null,
    StatType          varchar(32)    null,
    Games             int            null,
    Wins              int            null,
    Result            decimal(10, 2) null,
    Survived          decimal(10, 2) null,
    Damage            decimal(10, 2) null,
    Frags             decimal(10, 2) null,
    Tanked            decimal(10, 2) null,
    Spots             decimal(10, 2) null,
    Spotting          decimal(10, 2) null,
    MBFrags           decimal(10, 2) null,
    MbShots           decimal(10, 2) null,
    MbHits            decimal(10, 2) null,
    SbFrags           decimal(10, 2) null,
    SbShots           decimal(10, 2) null,
    SbHits            decimal(10, 2) null,
    TorpFrags         decimal(10, 2) null,
    TorpShots         decimal(10, 2) null,
    TorpHits          decimal(10, 2) null,
    RamFrags          decimal(10, 2) null,
    Cappts            decimal(10, 2) null,
    DroppedCappts     decimal(10, 2) null,
    ControlCappts     decimal(10, 2) null,
    ControlDroppedpts decimal(10, 2) null,
    TeamCappts        decimal(10, 2) null,
    TeamDroppedCappts decimal(10, 2) null,
    Priority          int            null,
    PlayerID          bigint         null,
    constraint idx_playerid_season_games_prio_gametime
        unique (PlayerID, Season, Games, Priority, GameTime)
);

create table if not exists ShipList
(
    ShipID    bigint       not null
        primary key,
    ShipName  varchar(128) null,
    ShortName varchar(64)  null,
    Tier      int          null,
    Class     varchar(2)   null,
    Nation    varchar(32)  null
);

create index idx_shiplist_tier
    on ShipList (Tier);

create table if not exists TrackedClans
(
    ClanTag     varchar(64) null,
    ClanRealm   varchar(3)  null,
    ClanID      bigint      null,
    Token       varchar(64) null,
    LastUpdated datetime    null,
    id          int auto_increment
        primary key
);

create table if not exists ViewFilter
(
    FilterName varchar(20)       not null
        primary key,
    StartTier  smallint unsigned null,
    EndTier    smallint unsigned null,
    ClassDD    tinyint(1)        null,
    ClassBB    tinyint(1)        null,
    ClassCV    tinyint(1)        null,
    ClassSS    tinyint(1)        null,
    ClassCA    tinyint(1)        null,
    MinGames   smallint unsigned null
);

create or replace definer = gdog@`%` view sem_GameList as
SELECT
	`dev_wowsStats`.`CBGames`.`Season` AS `Season`
	, `dev_wowsStats`.`CBGames`.`FinishedAt` AS `FinishedAt`
	, `dev_wowsStats`.`TrackedClans`.`ClanTag` AS `ClanTag`
	, `dev_wowsStats`.`CBTeams`.`TeamAB` AS `TeamAB`
	, `Enemy`.`ClanTag` AS `Enemy`
	, `dev_wowsStats`.`Maps`.`MapName` AS `Map`
	, `dev_wowsStats`.`CBTeams`.`Result` AS `Result`
	, (((1000 + `dev_wowsStats`.`CBTeams`.`Rating`) + (100 * (3 - `dev_wowsStats`.`CBTeams`.`Division`)))
			+ (300 * (4 - `dev_wowsStats`.`CBTeams`.`League`))) AS `Rating`
	, `dev_wowsStats`.`CBTeams`.`RatingDelta` AS `RatingDelta`
	, (CASE
		   WHEN (`dev_wowsStats`.`ClanHistory`.`MAXPositionLeague` = 0) THEN 'Hurricane'
		   WHEN (`dev_wowsStats`.`ClanHistory`.`MAXPositionLeague` = 1) THEN 'Typhoon'
		   WHEN (`dev_wowsStats`.`ClanHistory`.`MAXPositionLeague` = 2) THEN 'Storm'
		   WHEN (`dev_wowsStats`.`ClanHistory`.`MAXPositionLeague` = 3) THEN 'Gale'
		   WHEN (`dev_wowsStats`.`ClanHistory`.`MAXPositionLeague` = 4) THEN 'Squall'
		   ELSE 'No History' END) AS `EnemyLastLeague`
	, (CASE
		   WHEN (`dev_wowsStats`.`ClanHistory`.`MaxPositionPublicRating` > 2100) THEN 'Ty1+'
		   ELSE 'Low' END) AS `EnemyQuality`
	, `dev_wowsStats`.`CBGames`.`GameID` AS `GameID`
	, `dev_wowsStats`.`CBTeams`.`TeamID` AS `TeamID`
	, `EnemyTeams`.`TeamID` AS `EnemyTeamID`
	, `dev_wowsStats`.`TrackedClans`.`ClanID` AS `ClanID`
	, `Enemy`.`ClanID` AS `EnemyClanID`
FROM ((((((`dev_wowsStats`.`CBGames` JOIN `dev_wowsStats`.`CBTeams` ON ((`dev_wowsStats`.`CBGames`.`GameID`
		= `dev_wowsStats`.`CBTeams`.`GameID`))) JOIN `dev_wowsStats`.`TrackedClans`
		  ON ((`dev_wowsStats`.`CBTeams`.`ClanID`
				  = `dev_wowsStats`.`TrackedClans`.`ClanID`))) JOIN `dev_wowsStats`.`Maps`
		 ON ((`dev_wowsStats`.`CBGames`.`MapID` = `dev_wowsStats`.`Maps`.`MapID`))) JOIN `dev_wowsStats`.`CBTeams` `EnemyTeams`
		ON (((`dev_wowsStats`.`CBTeams`.`GameID` = `EnemyTeams`.`GameID`)
				AND (`dev_wowsStats`.`CBTeams`.`ClanID` <> `EnemyTeams`.`ClanID`)))) JOIN `dev_wowsStats`.`Clans` `Enemy`
	   ON ((`EnemyTeams`.`ClanID` = `Enemy`.`ClanID`))) LEFT JOIN `dev_wowsStats`.`ClanHistory`
	  ON (((`Enemy`.`ClanID` = `dev_wowsStats`.`ClanHistory`.`ClanID`)
			  AND (`dev_wowsStats`.`ClanHistory`.`SeasonNumber` = (`dev_wowsStats`.`CBGames`.`Season` - 1))
			  AND (`dev_wowsStats`.`ClanHistory`.`IsBestSeasonRating` = 1))))
ORDER BY
	`dev_wowsStats`.`CBGames`.`GameID` DESC;

create or replace definer = gdog@`%` view sem_PlayerPerGame as
SELECT
	`dev_wowsStats`.`Players`.`Nickname` AS `Nickname`
	, `dev_wowsStats`.`Clans`.`ClanTag` AS `PlayerClan`
	, `dev_wowsStats`.`ShipList`.`ShipName` AS `ShipName`
	, `dev_wowsStats`.`ShipList`.`Class` AS `Class`
	, `dev_wowsStats`.`ShipList`.`Tier` AS `Tier`
	, `dev_wowsStats`.`CBPlayers`.`Survived` AS `Survived`
	, `dev_wowsStats`.`CBTeams`.`Result` AS `Result`
	, `dev_wowsStats`.`CBTeams`.`TeamAB` AS `TeamAB`
	, `GameClan`.`ClanTag` AS `GameClan`
	, `dev_wowsStats`.`CBGames`.`GameID` AS `GameID`
	, `dev_wowsStats`.`Players`.`PlayerID` AS `PlayerID`
	, `dev_wowsStats`.`CBTeams`.`TeamID` AS `TeamID`
	, `dev_wowsStats`.`CBGames`.`FinishedAt` AS `GameTime`
FROM ((((((`dev_wowsStats`.`CBPlayers` JOIN `dev_wowsStats`.`Players` ON ((`dev_wowsStats`.`CBPlayers`.`PlayerID`
		= `dev_wowsStats`.`Players`.`PlayerID`))) JOIN `dev_wowsStats`.`ShipList`
		  ON ((`dev_wowsStats`.`CBPlayers`.`ShipID`
				  = `dev_wowsStats`.`ShipList`.`ShipID`))) JOIN `dev_wowsStats`.`Clans`
		 ON ((`dev_wowsStats`.`Players`.`ClanID` = `dev_wowsStats`.`Clans`.`ClanID`))) JOIN `dev_wowsStats`.`CBTeams`
		ON ((`dev_wowsStats`.`CBPlayers`.`TeamID` = `dev_wowsStats`.`CBTeams`.`TeamID`))) JOIN `dev_wowsStats`.`CBGames`
	   ON ((`dev_wowsStats`.`CBGames`.`GameID`
			   = `dev_wowsStats`.`CBTeams`.`GameID`))) JOIN `dev_wowsStats`.`Clans` `GameClan`
	  ON ((`dev_wowsStats`.`CBTeams`.`ClanID` = `GameClan`.`ClanID`)));

create or replace definer = gdog@`%` view vw_CBGameStats as
SELECT
	DENSE_RANK() OVER (ORDER BY `sem`.`GameTime` DESC ) AS `GameNumber`
	, `dev_wowsStats`.`Maps`.`MapName` AS `MapName`
	, `sem`.`Result` AS `Result`
	, ((`dev_wowsStats`.`CBTeams`.`TeamID` % 2) + 1) AS `TeamNumber`
	, `dev_wowsStats`.`Clans`.`ClanTag` AS `GameClan`
	, `sem`.`Nickname` AS `Nickname`
	, `dev_wowsStats`.`ShipList`.`ShipName` AS `ShipName`
	, `dev_wowsStats`.`ShipList`.`Class` AS `Class`
	, `dev_wowsStats`.`ShipList`.`Tier` AS `Tier`
	, `sem`.`PlayerClan` AS `PlayerClan`
	, `sem`.`Season` AS `Season`
	, `sem`.`GameTime` AS `GameTime`
	, `sem`.`GameDay` AS `GameDay`
	, `sem`.`StatType` AS `StatType`
	, `sem`.`Games` AS `Games`
	, `sem`.`Wins` AS `Wins`
	, `sem`.`Survived` AS `Survived`
	, `sem`.`Damage` AS `Damage`
	, `sem`.`Frags` AS `Frags`
	, `sem`.`Tanked` AS `Tanked`
	, `sem`.`Spots` AS `Spots`
	, `sem`.`Spotting` AS `Spotting`
	, `sem`.`MBFrags` AS `MBFrags`
	, `sem`.`MbShots` AS `MbShots`
	, `sem`.`MbHits` AS `MbHits`
	, `sem`.`SbFrags` AS `SbFrags`
	, `sem`.`SbShots` AS `SbShots`
	, `sem`.`SbHits` AS `SbHits`
	, `sem`.`TorpFrags` AS `TorpFrags`
	, `sem`.`TorpShots` AS `TorpShots`
	, `sem`.`TorpHits` AS `TorpHits`
	, `sem`.`RamFrags` AS `RamFrags`
	, `sem`.`Cappts` AS `Cappts`
	, `sem`.`DroppedCappts` AS `DroppedCappts`
	, `sem`.`ControlCappts` AS `ControlCappts`
	, `sem`.`ControlDroppedpts` AS `ControlDroppedpts`
	, `sem`.`TeamCappts` AS `TeamCappts`
	, `sem`.`TeamDroppedCappts` AS `TeamDroppedCappts`
	, `dev_wowsStats`.`CBTeams`.`TeamAB` AS `Rating`
	, `Airstrike`.`HasAirstrike` AS `HasAirstrike`
FROM (((((((`dev_wowsStats`.`Sem_NewCBStats` `sem` JOIN `dev_wowsStats`.`CBGames`
			ON ((`sem`.`GameTime` = `dev_wowsStats`.`CBGames`.`FinishedAt`))) JOIN `dev_wowsStats`.`CBTeams`
		   ON ((`dev_wowsStats`.`CBGames`.`GameID` = `dev_wowsStats`.`CBTeams`.`GameID`))) JOIN `dev_wowsStats`.`Maps`
		  ON ((`dev_wowsStats`.`CBGames`.`MapID` = `dev_wowsStats`.`Maps`.`MapID`))) JOIN `dev_wowsStats`.`CBPlayers`
		 ON (((`dev_wowsStats`.`CBPlayers`.`TeamID` = `dev_wowsStats`.`CBTeams`.`TeamID`)
				 AND (`dev_wowsStats`.`CBPlayers`.`PlayerID` = `sem`.`PlayerID`)))) JOIN `dev_wowsStats`.`ShipList`
		ON ((`dev_wowsStats`.`CBPlayers`.`ShipID` = `dev_wowsStats`.`ShipList`.`ShipID`))) JOIN `dev_wowsStats`.`Clans`
	   ON ((`dev_wowsStats`.`CBTeams`.`ClanID` = `dev_wowsStats`.`Clans`.`ClanID`))) JOIN (SELECT
	MAX((CASE
			 WHEN (`dev_wowsStats`.`CBPlayers`.`ShipID` IN (4179539728,3655218960)) THEN 1
			 ELSE 0 END)) AS `HasAirstrike`
	, `dev_wowsStats`.`CBTeams`.`TeamID` AS `TeamID`
	, `dev_wowsStats`.`CBTeams`.`GameID` AS `gameid`
FROM (`dev_wowsStats`.`CBTeams` JOIN `dev_wowsStats`.`CBPlayers`
	  ON ((`dev_wowsStats`.`CBTeams`.`TeamID` = `dev_wowsStats`.`CBPlayers`.`TeamID`)))
GROUP BY `dev_wowsStats`.`CBTeams`.`TeamID`, `dev_wowsStats`.`CBTeams`.`GameID`) `Airstrike`
	  ON (((`Airstrike`.`gameid` = `dev_wowsStats`.`CBGames`.`GameID`)
			  AND (`Airstrike`.`TeamID` <> `dev_wowsStats`.`CBTeams`.`TeamID`))))
WHERE
	(`sem`.`Season` = 25)
ORDER BY
	`sem`.`GameTime` DESC, `GameClan`;

create or replace definer = gdog@`%` view vw_CBGameStats_avg as
SELECT
	`dev_wowsStats`.`tot`.`Nickname` AS `Nickname`
	, `dev_wowsStats`.`tot`.`ShipName` AS `ShipName`
	, `dev_wowsStats`.`tot`.`Class` AS `Class`
	, `dev_wowsStats`.`tot`.`Season` AS `Season`
	, AVG(`dev_wowsStats`.`tot`.`Result`) AS `Winrate`
	, AVG(`dev_wowsStats`.`tot`.`Survived`) AS `Survival`
	, AVG(`dev_wowsStats`.`tot`.`Damage`) AS `Damage`
	, COALESCE(
			(SUM((CASE WHEN (`dev_wowsStats`.`tot`.`HasAirstrike` = 0) THEN `dev_wowsStats`.`tot`.`Tanked` ELSE 0 END))
					/ (COUNT(0) - SUM(`dev_wowsStats`.`tot`.`HasAirstrike`))), 0) AS `Tanked`
	, AVG(`dev_wowsStats`.`tot`.`Frags`) AS `Frags`
	, AVG(`dev_wowsStats`.`tot`.`Spotting`) AS `SpottingDamage`
	, AVG(`dev_wowsStats`.`tot`.`Spots`) AS `Spots`
	, AVG(`dev_wowsStats`.`tot`.`MbShots`) AS `MBShots`
	, AVG(`dev_wowsStats`.`tot`.`MbHits`) AS `MBHits`
	, (SUM(`dev_wowsStats`.`tot`.`MbHits`) / SUM(`dev_wowsStats`.`tot`.`MbShots`)) AS `MBHitrate`
	, AVG(`dev_wowsStats`.`tot`.`TorpShots`) AS `TorpShots`
	, AVG(`dev_wowsStats`.`tot`.`TorpHits`) AS `TorpHits`
	, (SUM(`dev_wowsStats`.`tot`.`TorpHits`) / SUM(`dev_wowsStats`.`tot`.`TorpShots`)) AS `TorpHitrate`
	, AVG(`dev_wowsStats`.`tot`.`SbShots`) AS `SBShots`
	, AVG(`dev_wowsStats`.`tot`.`SbHits`) AS `SBHits`
	, (SUM(`dev_wowsStats`.`tot`.`SbHits`) / SUM(`dev_wowsStats`.`tot`.`SbShots`)) AS `SBHitrate`
	, COUNT(0) AS `Games`
	, `dev_wowsStats`.`tot`.`GameClan` AS `GameClan`
FROM `dev_wowsStats`.`vw_CBGameStats` `tot`
GROUP BY
	`dev_wowsStats`.`tot`.`Nickname`, `dev_wowsStats`.`tot`.`ShipName`, `dev_wowsStats`.`tot`.`Class`
	, `dev_wowsStats`.`tot`.`Season`, `dev_wowsStats`.`tot`.`GameClan`
ORDER BY
	`dev_wowsStats`.`tot`.`Class`, `dev_wowsStats`.`tot`.`ShipName`, `dev_wowsStats`.`tot`.`Nickname`;

create or replace definer = gdog@`%` view vw_ClanHistory as
SELECT
	`dev_wowsStats`.`Clans`.`ClanTag` AS `ClanTag`
	, `dev_wowsStats`.`Clans`.`ClanName` AS `ClanName`
	, `dev_wowsStats`.`ClanHistory`.`MaxPublicRating` AS `MaxPublicRating`
	, (CASE
		   WHEN (`dev_wowsStats`.`ClanHistory`.`MAXPositionLeague` = 0) THEN 'Hurricane'
		   WHEN (`dev_wowsStats`.`ClanHistory`.`MAXPositionLeague` = 1) THEN 'Typhoon'
		   WHEN (`dev_wowsStats`.`ClanHistory`.`MAXPositionLeague` = 2) THEN 'Storm'
		   WHEN (`dev_wowsStats`.`ClanHistory`.`MAXPositionLeague` = 3) THEN 'Squall'
		   WHEN (`dev_wowsStats`.`ClanHistory`.`MAXPositionLeague` = 4) THEN 'Gale' END) AS `League`
	, `dev_wowsStats`.`ClanHistory`.`MAXPositionDivision` AS `Division`
	, `dev_wowsStats`.`ClanHistory`.`MaxPositionDivisionRating` AS `Rating`
	, (CASE WHEN (`dev_wowsStats`.`ClanHistory`.`TeamNumber` = 1) THEN 'Alpha' ELSE 'Bravo' END) AS `TeamRating`
	, `dev_wowsStats`.`ClanHistory`.`SeasonNumber` AS `SeasonNumber`
FROM (`dev_wowsStats`.`ClanHistory` JOIN `dev_wowsStats`.`Clans`
	  ON ((`dev_wowsStats`.`ClanHistory`.`ClanID` = `dev_wowsStats`.`Clans`.`ClanID`)))
WHERE
	(`dev_wowsStats`.`ClanHistory`.`SeasonNumber` <= 99)
ORDER BY
	`dev_wowsStats`.`Clans`.`ClanTag`, `dev_wowsStats`.`ClanHistory`.`SeasonNumber` DESC
	, `dev_wowsStats`.`ClanHistory`.`MaxPublicRating` DESC;

create or replace definer = gdog@`%` view vw_GameOverview as
SELECT
	`dev_wowsStats`.`CBGames`.`Season` AS `Season`
	, `HomeClans`.`ClanTag` AS `ClanTag`
	, `dev_wowsStats`.`Maps`.`MapName` AS `Map`
	, `dev_wowsStats`.`CBGames`.`FinishedAt` AS `GameTime`
	, `HomeTeam`.`Result` AS `Result`
	, `HomeTeam`.`TeamAB` AS `TeamRating`
	, `HomeTeam`.`Rating` AS `Rating`
	, `HomeTeam`.`Division` AS `Division`
	, (CASE
		   WHEN (`HomeTeam`.`League` = 0) THEN 'Hurricane'
		   WHEN (`HomeTeam`.`League` = 1) THEN 'Typhoon'
		   WHEN (`HomeTeam`.`League` = 2) THEN 'Storm'
		   WHEN (`HomeTeam`.`League` = 3) THEN 'Squall'
		   WHEN (`HomeTeam`.`League` = 4) THEN 'Gale' END) AS `League`
	, (((`HomeTeam`.`Rating` + ((3 - `HomeTeam`.`Division`) * 100)) + ((4 - `HomeTeam`.`League`) * 300))
			+ 1000) AS `Ranking`
	, `EnemyClans`.`ClanTag` AS `EnemyClan`
	, (CASE
		   WHEN (`dev_wowsStats`.`ClanHistory`.`MAXPositionLeague` = 0) THEN 'Hurricane'
		   WHEN (`dev_wowsStats`.`ClanHistory`.`MAXPositionLeague` = 1) THEN 'Typhoon'
		   WHEN (`dev_wowsStats`.`ClanHistory`.`MAXPositionLeague` = 2) THEN 'Storm'
		   WHEN (`dev_wowsStats`.`ClanHistory`.`MAXPositionLeague` = 3) THEN 'Squall'
		   WHEN (`dev_wowsStats`.`ClanHistory`.`MAXPositionLeague` = 4) THEN 'Gale' END) AS `EnemyLastLeague`
	, `dev_wowsStats`.`ClanHistory`.`MAXPositionDivision` AS `EnemyLastDivision`
FROM ((((((`dev_wowsStats`.`CBGames` JOIN `dev_wowsStats`.`CBTeams` `HomeTeam`
		   ON (((`dev_wowsStats`.`CBGames`.`GameID` = `HomeTeam`.`GameID`) AND `HomeTeam`.`ClanID` IN (SELECT
			   `dev_wowsStats`.`TrackedClans`.`ClanID`
		   FROM `dev_wowsStats`.`TrackedClans`)))) JOIN `dev_wowsStats`.`CBTeams` `Enemy`
		  ON (((`dev_wowsStats`.`CBGames`.`GameID` = `Enemy`.`GameID`)
				  AND (`Enemy`.`ClanID` <> `HomeTeam`.`ClanID`)))) JOIN `dev_wowsStats`.`Maps`
		 ON ((`dev_wowsStats`.`CBGames`.`MapID` = `dev_wowsStats`.`Maps`.`MapID`))) LEFT JOIN `dev_wowsStats`.`ClanHistory`
		ON (((`Enemy`.`ClanID` = `dev_wowsStats`.`ClanHistory`.`ClanID`)
				AND (`dev_wowsStats`.`ClanHistory`.`SeasonNumber` = 24)
				AND (`dev_wowsStats`.`ClanHistory`.`IsBestSeasonRating` = 1)))) LEFT JOIN `dev_wowsStats`.`Clans` `HomeClans`
	   ON ((`HomeClans`.`ClanID` = `HomeTeam`.`ClanID`))) LEFT JOIN `dev_wowsStats`.`Clans` `EnemyClans`
	  ON ((`EnemyClans`.`ClanID` = `Enemy`.`ClanID`)));

create or replace definer = gdog@`%` view vw_LiveDamage as
WITH
	`damage` AS (SELECT
		`dev_wowsStats`.`LiveDamage`.`Games` AS `Games`
		, `dev_wowsStats`.`LiveDamage`.`LastBattleTime` AS `lastbattletime`
		, `dev_wowsStats`.`LiveDamage`.`PlayerID` AS `playerid`
		, `dev_wowsStats`.`LiveDamage`.`ClanID` AS `ClanId`
		, `dev_wowsStats`.`Players`.`Nickname` AS `Nickname`
		, (`dev_wowsStats`.`LiveDamage`.`Games` * `dev_wowsStats`.`LiveDamage`.`Damage`) AS `tot_dam`
		, (`dev_wowsStats`.`LiveDamage`.`Games` * `dev_wowsStats`.`LiveDamage`.`Frags`) AS `tot_frags`
		, (CASE
			   WHEN ((`dev_wowsStats`.`LiveDamage`.`Games` - LAG(`dev_wowsStats`.`LiveDamage`.`Games`)
																 OVER (PARTITION BY `dev_wowsStats`.`LiveDamage`.`PlayerID` ORDER BY `dev_wowsStats`.`LiveDamage`.`Games` ))
					   = 1) THEN ((`dev_wowsStats`.`LiveDamage`.`Games` * `dev_wowsStats`.`LiveDamage`.`Damage`)
					   - LAG((`dev_wowsStats`.`LiveDamage`.`Games` * `dev_wowsStats`.`LiveDamage`.`Damage`))
							 OVER (PARTITION BY `dev_wowsStats`.`LiveDamage`.`PlayerID` ORDER BY `dev_wowsStats`.`LiveDamage`.`Games` ))
			   ELSE `dev_wowsStats`.`LiveDamage`.`Damage` END) AS `Damage`
		, (CASE
			   WHEN ((`dev_wowsStats`.`LiveDamage`.`Games` - LAG(`dev_wowsStats`.`LiveDamage`.`Games`)
																 OVER (PARTITION BY `dev_wowsStats`.`LiveDamage`.`PlayerID` ORDER BY `dev_wowsStats`.`LiveDamage`.`Games` ))
					   = 1) THEN ((`dev_wowsStats`.`LiveDamage`.`Games` * `dev_wowsStats`.`LiveDamage`.`Frags`)
					   - LAG((`dev_wowsStats`.`LiveDamage`.`Games` * `dev_wowsStats`.`LiveDamage`.`Frags`))
							 OVER (PARTITION BY `dev_wowsStats`.`LiveDamage`.`PlayerID` ORDER BY `dev_wowsStats`.`LiveDamage`.`Games` ))
			   ELSE `dev_wowsStats`.`LiveDamage`.`Frags` END) AS `Frags`
		, DENSE_RANK() OVER (PARTITION BY `dev_wowsStats`.`LiveDamage`.`ClanID`,CAST(`dev_wowsStats`.`LiveDamage`.`LastBattleTime` AS DATE) ORDER BY `dev_wowsStats`.`LiveDamage`.`LastBattleTime` ) AS `GameNo`
		, (CASE
			   WHEN ((`dev_wowsStats`.`LiveDamage`.`Games` - LAG(`dev_wowsStats`.`LiveDamage`.`Games`)
																 OVER (PARTITION BY `dev_wowsStats`.`LiveDamage`.`PlayerID` ORDER BY `dev_wowsStats`.`LiveDamage`.`Games` ))
					   = 1) THEN 'Accurate'
			   ELSE 'Average' END) AS `StatType`
	FROM ((`dev_wowsStats`.`LiveDamage` JOIN `dev_wowsStats`.`Players`
		   ON ((`dev_wowsStats`.`LiveDamage`.`PlayerID` = `dev_wowsStats`.`Players`.`PlayerID`))) JOIN (SELECT
		`dev_wowsStats`.`LiveDamage`.`LastBattleTime` AS `lastbattletime`
	FROM `dev_wowsStats`.`LiveDamage`
	GROUP BY `dev_wowsStats`.`LiveDamage`.`LastBattleTime`
	HAVING
		(COUNT(0) > 3)) `CB` ON ((`CB`.`lastbattletime` = `dev_wowsStats`.`LiveDamage`.`LastBattleTime`)))
	WHERE
		(`dev_wowsStats`.`LiveDamage`.`LastBattleTime` >= '2024-04-03 00:00:00'))
SELECT
	`damage`.`lastbattletime` AS `BattleStartTime`
	, `dev_wowsStats`.`Clans`.`ClanTag` AS `ClanTag`
	, `damage`.`Nickname` AS `Nickname`
	, ABS(ROUND(`damage`.`Damage`, 0)) AS `Damage`
	, ABS(ROUND(`damage`.`Frags`, 0)) AS `Frags`
	, `damage`.`GameNo` AS `GameNo`
	, `dev_wowsStats`.`ShipList`.`ShipName` AS `shipName`
	, `dev_wowsStats`.`ShipList`.`Class` AS `Class`
	, `games`.`Survived` AS `Survived`
	, `games`.`mapname` AS `MapName`
	, `games`.`result` AS `Result`
	, `damage`.`StatType` AS `StatType`
FROM (((`damage` LEFT JOIN (SELECT
	`dev_wowsStats`.`CBPlayers`.`PlayerID` AS `playerID`
	, `dev_wowsStats`.`CBPlayers`.`ShipID` AS `shipID`
	, `dev_wowsStats`.`CBPlayers`.`Survived` AS `Survived`
	, `dev_wowsStats`.`CBTeams`.`Result` AS `result`
	, `dev_wowsStats`.`Maps`.`MapName` AS `mapname`
	, DENSE_RANK() OVER (PARTITION BY `dev_wowsStats`.`CBTeams`.`ClanID`,CAST(`dev_wowsStats`.`CBGames`.`FinishedAt` AS DATE) ORDER BY `dev_wowsStats`.`CBPlayers`.`TeamID` ) AS `GameNo`
	, `dev_wowsStats`.`CBGames`.`FinishedAt` AS `finishedat`
FROM (((`dev_wowsStats`.`CBPlayers` JOIN `dev_wowsStats`.`CBTeams`
		ON ((`dev_wowsStats`.`CBPlayers`.`TeamID` = `dev_wowsStats`.`CBTeams`.`TeamID`))) JOIN `dev_wowsStats`.`CBGames`
	   ON ((`dev_wowsStats`.`CBTeams`.`GameID` = `dev_wowsStats`.`CBGames`.`GameID`))) JOIN `dev_wowsStats`.`Maps`
	  ON ((`dev_wowsStats`.`Maps`.`MapID` = `dev_wowsStats`.`CBGames`.`MapID`)))
WHERE
	(`dev_wowsStats`.`CBGames`.`FinishedAt` >= '2024-04-03 00:00:00')) `games`
		ON (((`damage`.`GameNo` = `games`.`GameNo`) AND (`damage`.`playerid` = `games`.`playerID`)
				AND (CAST(`damage`.`lastbattletime` AS DATE)
					= CAST(`games`.`finishedat` AS DATE))))) JOIN `dev_wowsStats`.`ShipList`
	   ON ((`games`.`shipID` = `dev_wowsStats`.`ShipList`.`ShipID`))) JOIN `dev_wowsStats`.`Clans`
	  ON ((`dev_wowsStats`.`Clans`.`ClanID` = `damage`.`ClanId`)))
ORDER BY
	`damage`.`lastbattletime` DESC;

create or replace definer = gdog@`%` view vw_livedamage_avg as
WITH
	`damage` AS (SELECT
		`dev_wowsStats`.`LiveDamage`.`Games` AS `Games`
		, `dev_wowsStats`.`LiveDamage`.`LastBattleTime` AS `lastbattletime`
		, `dev_wowsStats`.`LiveDamage`.`PlayerID` AS `playerid`
		, `dev_wowsStats`.`LiveDamage`.`ClanID` AS `ClanId`
		, `dev_wowsStats`.`Players`.`Nickname` AS `Nickname`
		, (`dev_wowsStats`.`LiveDamage`.`Games` * `dev_wowsStats`.`LiveDamage`.`Damage`) AS `tot_dam`
		, (`dev_wowsStats`.`LiveDamage`.`Games` * `dev_wowsStats`.`LiveDamage`.`Frags`) AS `tot_frags`
		, (CASE
			   WHEN ((`dev_wowsStats`.`LiveDamage`.`Games` - LAG(`dev_wowsStats`.`LiveDamage`.`Games`)
																 OVER (PARTITION BY `dev_wowsStats`.`LiveDamage`.`PlayerID` ORDER BY `dev_wowsStats`.`LiveDamage`.`Games` ))
					   = 1) THEN ((`dev_wowsStats`.`LiveDamage`.`Games` * `dev_wowsStats`.`LiveDamage`.`Damage`)
					   - LAG((`dev_wowsStats`.`LiveDamage`.`Games` * `dev_wowsStats`.`LiveDamage`.`Damage`))
							 OVER (PARTITION BY `dev_wowsStats`.`LiveDamage`.`PlayerID` ORDER BY `dev_wowsStats`.`LiveDamage`.`Games` ))
			   ELSE `dev_wowsStats`.`LiveDamage`.`Damage` END) AS `Damage`
		, (CASE
			   WHEN ((`dev_wowsStats`.`LiveDamage`.`Games` - LAG(`dev_wowsStats`.`LiveDamage`.`Games`)
																 OVER (PARTITION BY `dev_wowsStats`.`LiveDamage`.`PlayerID` ORDER BY `dev_wowsStats`.`LiveDamage`.`Games` ))
					   = 1) THEN ((`dev_wowsStats`.`LiveDamage`.`Games` * `dev_wowsStats`.`LiveDamage`.`Frags`)
					   - LAG((`dev_wowsStats`.`LiveDamage`.`Games` * `dev_wowsStats`.`LiveDamage`.`Frags`))
							 OVER (PARTITION BY `dev_wowsStats`.`LiveDamage`.`PlayerID` ORDER BY `dev_wowsStats`.`LiveDamage`.`Games` ))
			   ELSE `dev_wowsStats`.`LiveDamage`.`Frags` END) AS `Frags`
		, DENSE_RANK() OVER (PARTITION BY `dev_wowsStats`.`LiveDamage`.`ClanID`,CAST(`dev_wowsStats`.`LiveDamage`.`LastBattleTime` AS DATE) ORDER BY `dev_wowsStats`.`LiveDamage`.`LastBattleTime` ) AS `GameNo`
		, (CASE
			   WHEN ((`dev_wowsStats`.`LiveDamage`.`Games` - LAG(`dev_wowsStats`.`LiveDamage`.`Games`)
																 OVER (PARTITION BY `dev_wowsStats`.`LiveDamage`.`PlayerID` ORDER BY `dev_wowsStats`.`LiveDamage`.`Games` ))
					   = 1) THEN 'Accurate'
			   ELSE 'Average' END) AS `StatType`
	FROM ((`dev_wowsStats`.`LiveDamage` JOIN `dev_wowsStats`.`Players`
		   ON ((`dev_wowsStats`.`LiveDamage`.`PlayerID` = `dev_wowsStats`.`Players`.`PlayerID`))) JOIN (SELECT
		`dev_wowsStats`.`LiveDamage`.`LastBattleTime` AS `lastbattletime`
	FROM `dev_wowsStats`.`LiveDamage`
	GROUP BY `dev_wowsStats`.`LiveDamage`.`LastBattleTime`
	HAVING
		(COUNT(0) > 3)) `CB` ON ((`CB`.`lastbattletime` = `dev_wowsStats`.`LiveDamage`.`LastBattleTime`)))
	WHERE
		(`dev_wowsStats`.`LiveDamage`.`LastBattleTime` >= '2024-04-03 00:00:00'))
	, `tot` AS (SELECT
		`damage`.`lastbattletime` AS `BattleStartTime`
		, `dev_wowsStats`.`Clans`.`ClanTag` AS `ClanTag`
		, `damage`.`Nickname` AS `Nickname`
		, ABS(ROUND(`damage`.`Damage`, 0)) AS `Damage`
		, ABS(ROUND(`damage`.`Frags`, 0)) AS `Frags`
		, `damage`.`GameNo` AS `GameNo`
		, `dev_wowsStats`.`ShipList`.`ShipName` AS `shipName`
		, `dev_wowsStats`.`ShipList`.`Class` AS `Class`
		, `games`.`Survived` AS `Survived`
		, `games`.`mapname` AS `MapName`
		, `games`.`result` AS `Result`
		, `damage`.`StatType` AS `StatType`
	FROM (((`damage` LEFT JOIN (SELECT
		`dev_wowsStats`.`CBPlayers`.`PlayerID` AS `playerID`
		, `dev_wowsStats`.`CBPlayers`.`ShipID` AS `shipID`
		, `dev_wowsStats`.`CBPlayers`.`Survived` AS `Survived`
		, `dev_wowsStats`.`CBTeams`.`Result` AS `result`
		, `dev_wowsStats`.`Maps`.`MapName` AS `mapname`
		, DENSE_RANK() OVER (PARTITION BY `dev_wowsStats`.`CBTeams`.`ClanID`,CAST(`dev_wowsStats`.`CBGames`.`FinishedAt` AS DATE) ORDER BY `dev_wowsStats`.`CBPlayers`.`TeamID` ) AS `GameNo`
		, `dev_wowsStats`.`CBGames`.`FinishedAt` AS `finishedat`
	FROM (((`dev_wowsStats`.`CBPlayers` JOIN `dev_wowsStats`.`CBTeams` ON ((`dev_wowsStats`.`CBPlayers`.`TeamID`
			= `dev_wowsStats`.`CBTeams`.`TeamID`))) JOIN `dev_wowsStats`.`CBGames`
		   ON ((`dev_wowsStats`.`CBTeams`.`GameID` = `dev_wowsStats`.`CBGames`.`GameID`))) JOIN `dev_wowsStats`.`Maps`
		  ON ((`dev_wowsStats`.`Maps`.`MapID` = `dev_wowsStats`.`CBGames`.`MapID`)))
	WHERE
		(`dev_wowsStats`.`CBGames`.`FinishedAt` >= '2024-04-03 00:00:00')) `games`
			ON (((`damage`.`GameNo` = `games`.`GameNo`) AND (`damage`.`playerid` = `games`.`playerID`)
					AND (CAST(`damage`.`lastbattletime` AS DATE)
						= CAST(`games`.`finishedat` AS DATE))))) JOIN `dev_wowsStats`.`ShipList`
		   ON ((`games`.`shipID` = `dev_wowsStats`.`ShipList`.`ShipID`))) JOIN `dev_wowsStats`.`Clans`
		  ON ((`dev_wowsStats`.`Clans`.`ClanID` = `damage`.`ClanId`))))
SELECT
	`tot`.`Nickname` AS `Nickname`
	, `tot`.`shipName` AS `ShipName`
	, `tot`.`Class` AS `Class`
	, `tot`.`ClanTag` AS `ClanTag`
	, AVG(`tot`.`Damage`) AS `Damage`
	, AVG(`tot`.`Frags`) AS `Frags`
	, AVG(`tot`.`Survived`) AS `Survival`
	, AVG(`tot`.`Result`) AS `Winrate`
	, COUNT(0) AS `Games`
FROM `tot`
WHERE
	(`tot`.`ClanTag` IN (SELECT `dev_wowsStats`.`TrackedClans`.`ClanTag` FROM `dev_wowsStats`.`TrackedClans`)
			AND (`tot`.`StatType` = 'Accurate') AND (`tot`.`Damage` IS NOT NULL))
GROUP BY
	`tot`.`Nickname`, `tot`.`shipName`, `tot`.`Class`, `tot`.`ClanTag`;

create
    definer = gdog@`%` procedure usp_Client_UpdateCBGameStats(IN NewPlayerID bigint, IN NewGameTime datetime,
                                                              IN NewSeason int, IN NewGames int, IN NewWins int,
                                                              IN NewLosses int, IN NewDraws int,
                                                              IN NewSurvivedBattles int, IN NewSurvivedWins int,
                                                              IN NewDamage bigint, IN NewFrags int, IN NewMBFrags int,
                                                              IN NewSBFrags int, IN NewTorpFrags int,
                                                              IN NewPlaneFrags int, IN NewRamFrags int,
                                                              IN NewMBShots int, IN NewSBShots int, IN NewTorpShots int,
                                                              IN NewMBHits int, IN NewSBHits int, IN NewTorpHits int,
                                                              IN NewGunTanked int, IN NewTorpTanked int,
                                                              IN NewSpots int, IN NewSpottingDamage bigint,
                                                              IN NewPlanesKilled int, IN NewDroppedCapPts int,
                                                              IN NewCapPts int, IN NewControlCapPts int,
                                                              IN NewControlDroppedPts int, IN NewTeamCapPts int,
                                                              IN NewTeamDroppedCapPts int)
BEGIN

DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
		 ROLLBACK;
         SELECT 'Error' AS Outcome;
    END;

START TRANSACTION;
	IF NOT EXISTS (
		SELECT
			PlayerID
		FROM
			CBGameStats
		WHERE
			PlayerID = NewPlayerID
   			AND Games = NewGames
   			AND Season = NewSeason)
	THEN
   INSERT INTO CBGameStats (
		PlayerID
		,GameTime
		,Season
		,Games
		,Wins
		,Losses
		,Draws
		,SurvivedBattles
		,SurvivedWins
		,Damage
		,Frags
		,MBFrags
		,SBFrags
		,TorpFrags
		,PlaneFrags
		,RamFrags
		,MBShots
		,SBShots
		,TorpShots
		,MBHits
		,SBHits
		,TorpHits
		,GunTanked
		,TorpTanked
		,Spots
		,SpottingDamage
		,PlanesKilled
		,DroppedCapPts
		,CapPts
		,ControlCapPts
		,ControlDroppedPts
		,TeamCapPts
		,TeamDroppedCapPts
		,Priority)
   VALUES(
		NewPlayerID
		,NewGameTime
		,NewSeason
		,NewGames
		,NewWins
		,NewLosses
		,NewDraws
		,NewSurvivedBattles
		,NewSurvivedWins
		,NewDamage
		,NewFrags
		,NewMBFrags
		,NewSBFrags
		,NewTorpFrags
		,NewPlaneFrags
		,NewRamFrags
		,NewMBShots
		,NewSBShots
		,NewTorpShots
		,NewMBHits
		,NewSBHits
		,NewTorpHits
		,NewGunTanked
		,NewTorpTanked
		,NewSpots
		,NewSpottingDamage
		,NewPlanesKilled
		,NewDroppedCapPts
		,NewCapPts
		,NewControlCapPts
		,NewControlDroppedPts
		,NewTeamCapPts
		,NewTeamDroppedCapPts
		,0);
   		SELECT
   			'Success' AS Outcome;
   ELSE
		SELECT
			'Exists' AS Outcome;
   END IF;
COMMIT;
END;

create
    definer = gdog@`%` procedure usp_CurrentSeason()
SELECT
		Seasons.Season
	FROM
		Seasons
	ORDER BY
		StartDate DESC
	LIMIT 1;

create
    definer = gdog@`%` procedure usp_GetAllCurrentClans(IN chkSeason int)
BEGIN
	SELECT DISTINCT
		CBTeams.ClanID
	FROM
		CBTeams
		INNER JOIN CBGames ON CBGames.GameID=CBTeams.GameID
		INNER JOIN Clans ON CBTeams.ClanID=Clans.ClanID
	WHERE
		CBGames.Season=chkSeason
		AND Clans.IsDisbanded=0;
END;

create
    definer = gdog@`%` procedure usp_GetClansToUpdate()
BEGIN
SELECT
	clanID
    ,realm
FROM
	Clans
WHERE
	NeedsUpdate = 1
    AND (isDisbanded = 0 OR isdisbanded IS NULL);
END;

create
    definer = gdog@`%` procedure usp_GetLineups(IN chkTag varchar(6), IN chkSeason int)
SELECT
	DENSE_RANK() OVER (ORDER BY CBGames.GameID) AS GameNumber
	,Clans.ClanTag AS TeamClan
	,Nickname
	,PlayerClan.ClanTag AS PlayerClan
	,(CBTeams.TeamID % 2) + 1 AS TeamNumber
	,MapName
	,Class
	,ShipName
	,Survived
	,Result
FROM
	CBGames
	INNER JOIN CBTeams ON CBGames.GameID=CBTeams.GameID
	INNER JOIN CBPlayers ON CBTeams.TeamID=CBPlayers.TeamID
	INNER JOIN Players ON CBPlayers.PlayerID=Players.PlayerID
	INNER JOIN Clans AS PlayerClan ON Players.ClanID=PlayerClan.ClanID
	INNER JOIN Maps ON CBGames.MapID=Maps.MapID
	INNER JOIN ShipList ON CBPlayers.ShipID=ShipList.ShipID
	INNER JOIN Clans ON CBTeams.ClanID=Clans.ClanID
	INNER JOIN (SELECT GameID FROM CBTeams INNER JOIN TrackedClans ON CBTeams.ClanID=TrackedClans.ClanID WHERE ClanTag = chkTag OR chkTag IS NULL) AS Clanu ON Clanu.GameID=CBGames.GameID
WHERE
	Season=chkSeason;

create
    definer = gdog@`%` procedure usp_GetLivedamage(IN chkSeason int)
SELECT * FROM vw_CBGameStats WHERE Season = chkSeason;

create
    definer = gdog@`%` procedure usp_GetLivedamageAVG(IN chkTag varchar(6), IN chkSeason int)
SELECT * FROM vw_CBGameStats_avg WHERE Season = chkSeason AND vw_CBGameStats_avg.GameClan=chkTag;

create
    definer = gdog@`%` procedure usp_GetMapWinrates(IN chkTag varchar(6), IN chkSeason int)
SELECT
		MapName
		,TrackedClans.ClanTag
		,CBTeams.TeamAB
		,COUNT(*) AS Games
		,SUM(CASE WHEN Result=1 THEN 1 ELSE 0 END) AS Wins
		,SUM(CASE WHEN Result=0 THEN 1 ELSE 0 END) AS Losses
		,SUM(CASE WHEN Result=1 THEN 1 ELSE 0 END)  / COUNT(*)  AS Winrate
		,Season
		,CASE WHEN Enemy.MaxPublicRating > 2100 THEN 'Ty1+' ELSE 'Low' END AS Quality
	FROM
		CBGames
		INNER JOIN CBTeams ON CBGames.GameID=CBTeams.GameID AND Season=chkSeason
		INNER JOIN TrackedClans ON CBTeams.ClanID=TrackedClans.ClanID AND ClanTag=chkTag
		INNER JOIN Maps ON CBGames.MapID = Maps.MapID
		INNER JOIN (SELECT CBTeams.gameid AS EnemyID, ClanHistory.MaxPublicRating FROM CBTeams LEFT JOIN ClanHistory ON CBTeams.ClanID=ClanHistory.ClanID AND ClanHistory.SeasonNumber = chkSeason-1 AND ClanHistory.IsBestSeasonRating=1 WHERE CBTeams.ClanID NOT IN (SELECT ClanID FROM TrackedClans)) AS Enemy ON Enemy.EnemyID = CBGames.GameID
	GROUP BY
		MapName, TrackedClans.ClanTag, TeamAB, Season,CASE WHEN Enemy.MaxPublicRating > 2100 THEN 'Ty1+' ELSE 'Low' END
	ORDER BY
		CBTeams.TeamAB, MapName, Quality;

create
    definer = gdog@`%` procedure usp_GetMissingHistoryClans(IN chkSeason int)
BEGIN
	SELECT DISTINCT
		CBTeams.ClanID
	FROM
		CBTeams
		INNER JOIN CBGames ON CBGames.GameID=CBTeams.GameID AND CBGames.Season=chkSeason
		INNER JOIN Clans ON CBTeams.ClanID=Clans.ClanID AND Clans.IsDisbanded=0
	WHERE NOT EXISTS (SELECT ClanID FROM ClanHistory WHERE Clans.ClanID=ClanHistory.ClanID AND ClanHistory.SeasonNumber=chkSeason);
END;

create
    definer = gdog@`%` procedure usp_GetPlayerRandomStats(IN chktier int)
WITH tots AS(
		SELECT
			Players.Nickname
			,TrackedClans.ClanTag
			,ShipName
			,Class
			,Tier
			,prs.Damage * Games AS Damage
			,prs.Frags * Games  AS Frags
			,prs.Spotting * Games  AS Spotting
			,prs.tanked * Games  AS Tanked
			,prs.Survived * Games  AS Survived
			,prs.wins AS Wins
			,prs.Wins/Games  AS Winrate
			,prs.XP * Games  AS XP
			,prs.Games AS Games
			,prs.matchtype
		FROM
			Players
			INNER JOIN TrackedClans ON Players.ClanID=TrackedClans.ClanID
			INNER JOIN PlayerRandomStats AS prs ON Players.PlayerID=prs.PlayerID
			INNER JOIN ShipList ON prs.ShipID=ShipList.ShipID AND ShipList.Tier=chktier)
	SELECT
		Nickname
		,ClanTag
		,ShipName
		,Class
		,Tier
		,SUM(CASE WHEN matchtype IN ('random','ranked') THEN Damage ELSE 0 END)/SUM(CASE WHEN matchtype IN ('random','ranked') THEN Games ELSE 0 END) AS Damage
		,SUM(CASE WHEN matchtype IN ('random','ranked') THEN Frags ELSE 0 END)/SUM(CASE WHEN matchtype IN ('random','ranked') THEN Games ELSE 0 END) AS Frags
		,SUM(CASE WHEN matchtype IN ('random','ranked') THEN Spotting ELSE 0 END)/SUM(CASE WHEN matchtype IN ('random','ranked') THEN Games ELSE 0 END) AS Spotting
		,SUM(CASE WHEN matchtype IN ('random','ranked') THEN Tanked ELSE 0 END)/SUM(CASE WHEN matchtype IN ('random','ranked') THEN Games ELSE 0 END) AS Tanked
		,SUM(CASE WHEN matchtype IN ('random','ranked') THEN Survived ELSE 0 END) AS Survived
		,SUM(CASE WHEN matchtype IN ('random','ranked') THEN Wins ELSE 0 END) AS Wins
		,SUM(CASE WHEN matchtype IN ('random','ranked') THEN XP ELSE 0 END)/SUM(CASE WHEN matchtype IN ('random','ranked') THEN Games ELSE 0 END) AS XP
		,MAX(CASE WHEN matchtype = 'random' THEN Games END) AS RandomGames
		,MAX(CASE WHEN matchtype = 'random' THEN Winrate END) AS RandomWinrate
		,MAX(CASE WHEN matchtype = 'solo' THEN Games END) AS SoloGames
		,MAX(CASE WHEN matchtype = 'solo' THEN Winrate END) AS SoloWinrate
		,MAX(CASE WHEN matchtype = 'ranked' THEN Games END) AS RankedGames
		,MAX(CASE WHEN matchtype = 'ranked' THEN Winrate END) AS RankedWinrate
	FROM
		tots
	GROUP BY
		Nickname, ClanTag, ShipName, Class, Tier;

create
    definer = gdog@`%` procedure usp_GetPlayersToUpdate()
BEGIN
SELECT
	playerID
    ,realm
    ,COALESCE(isHidden,1) AS IsHidden
FROM
	Players
WHERE
	NeedsUpdate = 1;
END;

create
    definer = gdog@`%` procedure usp_GetPlayersToUpdateRandomStats()
BEGIN
	SELECT
		Players.PlayerID
		,Players.Realm
	FROM
		Players
		INNER JOIN TrackedClans ON Players.ClanID=TrackedClans.ClanID
		LEFT JOIN (SELECT PlayerID, MAX(PlayerRandomStats.LastUpdated) AS LastUpdated FROM PlayerRandomStats GROUP BY PlayerID) AS NU ON Players.PlayerID=NU.PlayerID
	WHERE
		(IsHidden = 0 OR IsHidden IS NULL)
		AND (NU.LastUpdated <=  DATE_ADD(NOW(), INTERVAL -7 DAY) OR NU.PlayerID IS NULL);
END;

create
    definer = gdog@`%` procedure usp_GetPlayersWithNewCBs()
BEGIN
	SET @LastScrape = (SELECT MAX(CheckDate) FROM CBGameStats WHERE Priority > 0);
	SET @CurrentSeason = (	SELECT
								Seasons.Season
							FROM
								Seasons
							ORDER BY
								StartDate DESC
							LIMIT 1);

		SELECT
			CBPlayers.PlayerID
		    ,CBPlayers.Realm
		    ,MAX(CBGames.FinishedAt) AS Timestamp
		FROM
			CBGames
			INNER JOIN CBTeams ON CBGames.GameID = CBTeams.GameID
			INNER JOIN CBPlayers ON CBTeams.TeamID=CBPlayers.TeamID
		WHERE
			CBGames.CheckDate > @LastScrape OR @LastScrape IS NULL
		GROUP BY
			CBPlayers.PlayerID
		    ,CBPlayers.Realm
		UNION
		SELECT DISTINCT
			LiveDamage.PlayerID
			,Clans.Realm
			,MAX(LiveDamage.LastBattleTime) AS Timestamp
		FROM
			LiveDamage
			INNER JOIN Clans ON LiveDamage.ClanID=Clans.ClanID AND Clans.Tracked=1
		WHERE
			LiveDamage.Games > 0
			AND (LiveDamage.CheckTime > @LastScrape OR @LastScrape IS NULL)
			AND LiveDamage.PlayerID NOT IN(
				SELECT
					CBPlayers.PlayerID
				FROM
					CBGames
					INNER JOIN CBTeams ON CBGames.GameID = CBTeams.GameID
					INNER JOIN CBPlayers ON CBTeams.TeamID=CBPlayers.TeamID
				WHERE
					CBGames.CheckDate > @LastScrape OR @LastScrape IS NULL)
		GROUP BY
			LiveDamage.PlayerID
			,Clans.Realm;
	END;

create
    definer = gdog@`%` procedure usp_HandleClanUpdates(IN NewClanID bigint, IN NewRealm varchar(3))
BEGIN

DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
		ROLLBACK;
        SELECT 'Error' AS Outcome;
    END;

START TRANSACTION;
 IF NOT EXISTS (
		SELECT
			clanid
		FROM
			Clans
		WHERE
			clanid = NewClanID)
	THEN
    INSERT INTO Clans (ClanID, ClanName, Realm, ClanTag, LastSeen, NeedsUpdate)  VALUES(
		NewClanID
        ,'NEW'
        ,NewRealm
        ,'NEW'
        ,NOW()
        ,1);
	ELSE
		UPDATE Clans SET
			LastSeen=NOW()
            ,NeedsUpdate = CASE
				WHEN DATEDIFF((SELECT LastSeen FROM Clans WHERE ClanId=NewClanID),NOW()) >= 7
                THEN 1 ELSE 0 END
		WHERE
			ClanID=NewClanID;
	END IF;
COMMIT;
END;

create
    definer = gdog@`%` procedure usp_HandlePlayerUpdates(IN NewPlayerID bigint, IN NewRealm varchar(3))
BEGIN

DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
		ROLLBACK;
        SELECT 'Error' AS Outcome;
    END;

START TRANSACTION;
IF NOT EXISTS (
		SELECT
			playerID
		FROM
			Players
		WHERE
			playerId = NewPlayerId)
	THEN
   INSERT INTO Players (playerID, Realm, Nickname, LastSeen, NeedsUpdate)  VALUES(
		NewPlayerID
        ,NewRealm
        ,'NEW'
        ,NOW()
        ,1);
	ELSE
	UPDATE Players SET
		LastSeen = NOW()
        ,NeedsUpdate = CASE
				WHEN DATEDIFF((SELECT LastSeen FROM Players WHERE PlayerID=NewPlayerID),NOW()) >= 7
                THEN 1 ELSE 0 END
	WHERE
		PlayerID = NewPlayerID;
	END IF;
COMMIT;
END;

create
    definer = gdog@`%` procedure usp_SetTrackedClans(IN chkRating int, IN chkSeason int)
BEGIN
	UPDATE Clans SET Tracked = 0 WHERE Tracked = 1;
	UPDATE Clans SET Tracked = 1 WHERE ClanID IN (SELECT ClanID FROM TrackedClans);
	UPDATE Clans SET Tracked = 1 WHERE ClanID IN (SELECT ClanID FROM ClanHistory WHERE MaxPublicRating >= chkRating AND SeasonNumber=chkSeason);
END;

create
    definer = gdog@`%` procedure usp_StatsRecheck()
BEGIN
WITH recents AS (
	SELECT
		MAX(GameID) AS GameID
	FROM
		CBTeams
		INNER JOIN TrackedClans ON CBTeams.ClanID=TrackedClans.ClanID
	GROUP BY
		CBTeams.ClanID
		,TeamAB)
SELECT
	PlayerID
	,FinishedAt AS Timestamp
FROM
	CBGames
	INNER JOIN recents ON CBGames.GameID=recents.GameID
	INNER JOIN CBTeams ON CBGames.GameID=CBTeams.GameID
	INNER JOIN CBPlayers ON CBTeams.TeamID=CBPlayers.TeamID
WHERE
	NOT EXISTS (SELECT PlayerID FROM CBGameStats WHERE CBGameStats.PlayerID=CBPlayers.PlayerID AND FinishedAt=GameTime)
	AND CAST(FinishedAt AS DATE) >= CAST(DATE_ADD(NOW(), INTERVAL -1 DAY) AS DATE);
	END;

create
    definer = gdog@`%` procedure usp_UpdateCBGameStats(IN NewPlayerID bigint, IN NewGameTime datetime, IN NewSeason int,
                                                       IN NewGames int, IN NewWins int, IN NewLosses int,
                                                       IN NewDraws int, IN NewSurvivedBattles int,
                                                       IN NewSurvivedWins int, IN NewDamage bigint, IN NewFrags int,
                                                       IN NewMBFrags int, IN NewSBFrags int, IN NewTorpFrags int,
                                                       IN NewPlaneFrags int, IN NewRamFrags int, IN NewMBShots int,
                                                       IN NewSBShots int, IN NewTorpShots int, IN NewMBHits int,
                                                       IN NewSBHits int, IN NewTorpHits int, IN NewGunTanked int,
                                                       IN NewTorpTanked int, IN NewSpots int,
                                                       IN NewSpottingDamage bigint, IN NewPlanesKilled int,
                                                       IN NewDroppedCapPts int, IN NewCapPts int,
                                                       IN NewControlCapPts int, IN NewControlDroppedPts int,
                                                       IN NewTeamCapPts int, IN NewTeamDroppedCapPts int,
                                                       IN NewPriority int)
BEGIN

DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
		 ROLLBACK;
         SELECT 'Error' AS Outcome;
    END;

START TRANSACTION;
	IF NOT EXISTS (
		SELECT
			PlayerID
		FROM
			CBGameStats
		WHERE
			PlayerID = NewPlayerID
   			AND Games = NewGames
   			AND Season = NewSeason)
	THEN
   INSERT INTO CBGameStats (
		PlayerID
		,GameTime
		,Season
		,Games
		,Wins
		,Losses
		,Draws
		,SurvivedBattles
		,SurvivedWins
		,Damage
		,Frags
		,MBFrags
		,SBFrags
		,TorpFrags
		,PlaneFrags
		,RamFrags
		,MBShots
		,SBShots
		,TorpShots
		,MBHits
		,SBHits
		,TorpHits
		,GunTanked
		,TorpTanked
		,Spots
		,SpottingDamage
		,PlanesKilled
		,DroppedCapPts
		,CapPts
		,ControlCapPts
		,ControlDroppedPts
		,TeamCapPts
		,TeamDroppedCapPts
		,Priority)
   VALUES(
		NewPlayerID
		,NewGameTime
		,NewSeason
		,NewGames
		,NewWins
		,NewLosses
		,NewDraws
		,NewSurvivedBattles
		,NewSurvivedWins
		,NewDamage
		,NewFrags
		,NewMBFrags
		,NewSBFrags
		,NewTorpFrags
		,NewPlaneFrags
		,NewRamFrags
		,NewMBShots
		,NewSBShots
		,NewTorpShots
		,NewMBHits
		,NewSBHits
		,NewTorpHits
		,NewGunTanked
		,NewTorpTanked
		,NewSpots
		,NewSpottingDamage
		,NewPlanesKilled
		,NewDroppedCapPts
		,NewCapPts
		,NewControlCapPts
		,NewControlDroppedPts
		,NewTeamCapPts
		,NewTeamDroppedCapPts
		,NewPriority);
   		SELECT
   			'Success' AS Outcome;
   ELSEIF EXISTS (
		SELECT
			PlayerID
		FROM
			CBGameStats
		WHERE
			PlayerID = NewPlayerID
   			AND Games = NewGames
   			AND Season = NewSeason
   			AND NewPriority > Priority)
   		THEN
   		UPDATE CBGameStats
   		SET
   			GameTime=NewGameTime
   			,Priority=NewPriority
   		WHERE
   			PlayerID = NewPlayerID
   			AND Games = NewGames
   			AND Season = NewSeason
   			AND NewPriority > Priority;
		SELECT
			'Update' AS Outcome;
	ELSE
		SELECT
			'Exists' AS Outcome;
   END IF;
COMMIT;
END;

create
    definer = gdog@`%` procedure usp_UpdateCBGames(IN NewgameID bigint, IN NewmapID bigint, IN Newseason int,
                                                   IN NewclusterID bigint, IN NewarenaID bigint,
                                                   IN NewfinishedAt datetime)
BEGIN
	DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
		ROLLBACK;
        SELECT 'Error' AS Outcome;
    END;

    START TRANSACTION;
    IF NOT EXISTS (
		SELECT
			gameid
		FROM
			CBGames
		WHERE
			gameid = newgameid)
		THEN
		INSERT INTO CBGames(
			gameID
			,mapID
			,season
			,clusterID
			,arenaID
			,finishedAt)
		VALUES
			(NewgameID
			,NewmapID
			,Newseason
			,NewclusterID
			,NewarenaID
			,NewfinishedAt);
		SELECT 'Success' AS Outcome;
	ELSE
		SELECT 'Exists' AS Outcome;
	END IF;
	COMMIT;
    END;

create
    definer = gdog@`%` procedure usp_UpdateCBPlayers(IN newteamID bigint, IN newplayerID bigint, IN newshipID bigint,
                                                     IN newSurvived tinyint(1), IN newRealm varchar(3))
BEGIN
	DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
		ROLLBACK;
        SELECT 'Error' AS Outcome;
    END;

    IF NOT EXISTS (
		SELECT
			teamid
		FROM
			CBPlayers
		WHERE
			teamid = newteamid
			AND playerid = newplayerid)
		THEN
		START TRANSACTION;
		INSERT INTO CBPlayers(
			teamID
			,playerID
			,shipID
			,Survived
            ,realm)
		VALUES
			(newteamID
			,newplayerID
			,newshipID
			,newSurvived
            ,newrealm);
        COMMIT;
        CALL usp_HandlePlayerUpdates(NewPlayerID,NewRealm);
		SELECT 'Success' AS Outcome;
	ELSE
		SELECT 'Exists' AS Outcome;
	END IF;
END;

create
    definer = gdog@`%` procedure usp_UpdateCBTeams(IN newgameID bigint, IN newteamID bigint, IN newclanID bigint,
                                                   IN newrealm varchar(3), IN newteamAB varchar(1), IN newleague int,
                                                   IN newdivision int, IN newrating int, IN newratingdelta int,
                                                   IN newresult tinyint(1))
BEGIN
	DECLARE EXIT HANDLER FOR SQLEXCEPTION
	BEGIN
		SELECT 'Error' AS Outcome;
	END;

	IF NOT EXISTS (
		SELECT
			teamid
		FROM
			CBTeams
		WHERE
			teamid = newteamid)
		THEN
		START TRANSACTION;
		INSERT INTO CBTeams(
			gameID
			,teamID
			,clanID
			,realm
			,teamAB
			,league
			,division
			,rating
			,ratingdelta
			,result)
		VALUES
			(newgameID
			,newteamID
			,newclanID
			,newrealm
			,newteamAB
			,newleague
			,newdivision
			,newrating
			,newratingdelta
			,newresult);
		COMMIT;
		CALL usp_HandleClanUpdates(NewClanID,NewRealm);
		SELECT 'Success' AS Outcome;
	ELSE
		SELECT 'Exists' AS Outcome;
	END IF;
END;

create
    definer = gdog@`%` procedure usp_UpdateClanRatings(IN NewClanID bigint, IN NewGames int, IN NewLeague int,
                                                       IN NewMaxPositionPublicRating int,
                                                       IN NewMaxPositionDivisionRating int, IN NewMAXPositionLeague int,
                                                       IN NewMAXPositionDivision int, IN NewWins int,
                                                       IN NewInitialPublicRating int,
                                                       IN NewIsBestSeasonRating tinyint(1), IN NewTeamNumber int,
                                                       IN NewIsQualified tinyint(1), IN NewRatingID bigint,
                                                       IN NewCurrentWinStreak int, IN NewActiveStatus varchar(32),
                                                       IN NewSeasonNumber int, IN NewDivisionRatingMax int,
                                                       IN NewRealm varchar(2), IN NewDivisionRating int,
                                                       IN NewLongestWinningStreak int, IN NewMaxPublicRating int,
                                                       IN NewPublicRating int, IN NewLastWinAt datetime,
                                                       IN NewDivision int)
BEGIN
	DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
		ROLLBACK;
        SELECT 'Error' AS Outcome;
    END;

	START TRANSACTION;
	IF NOT EXISTS (
		SELECT
			ClanID
		FROM
			ClanHistory
		WHERE
			ClanID = NewClanID
			AND SeasonNumber=NewSeasonNumber
			AND TeamNumber=NewTeamNumber)
		THEN
		INSERT INTO ClanHistory(
			ClanID
			,Games
			,League
			,MaxPositionPublicRating
			,MaxPositionDivisionRating
			,MAXPositionLeague
			,MAXPositionDivision
			,Wins
			,InitialPublicRating
			,IsBestSeasonRating
			,TeamNumber
			,IsQualified
			,RatingID
			,CurrentWinStreak
			,ActiveStatus
			,SeasonNumber
			,DivisionRatingMax
			,Realm
			,DivisionRating
			,LongestWinningStreak
			,MaxPublicRating
			,PublicRating
			,LastWinAt
			,Division)
		VALUES
			(NewClanID
			,NewGames
			,NewLeague
			,NewMaxPositionPublicRating
			,NewMaxPositionDivisionRating
			,NewMaxPositionLeague
			,NewMaxPositionDivision
			,NewWins
			,NewInitialPublicRating
			,NewIsBestSeasonRating
			,NewTeamNumber
			,NewIsQualified
			,NewRatingID
			,NewCurrentWinStreak
			,NewActiveStatus
			,NewSeasonNumber
			,NewDivisionRatingMax
			,NewRealm
			,NewDivisionRating
			,NewLongestWinningStreak
			,NewMaxPublicRating
			,NewPublicRating
			,NewLastWinAt
			,NewDivision);
		SELECT 'Success' AS Outcome;
	ELSE
	UPDATE ClanHistory SET
		ClanID = NewClanID
		,Games = NewGames
		,League = NewLeague
		,MaxPositionPublicRating = NewMaxPositionPublicRating
		,MaxPositionDivisionRating = NewMaxPositionDivisionRating
		,MaxPositionLeague = NewMaxPositionLeague
		,MaxPositionDivision = NewMaxPositionDivision
		,Wins = NewWins
		,InitialPublicRating = NewInitialPublicRating
		,IsBestSeasonRating = NewIsBestSeasonRating
		,TeamNumber = NewTeamNumber
		,IsQualified = NewIsQualified
		,RatingID = NewRatingID
		,CurrentWinStreak = NewCurrentWinStreak
		,ActiveStatus = NewActiveStatus
		,SeasonNumber = NewSeasonNumber
		,DivisionRatingMax = NewDivisionRatingMax
		,Realm = NewRealm
		,DivisionRating = NewDivisionRating
		,LongestWinningStreak = NewLongestWinningStreak
		,MaxPublicRating = NewMaxPublicRating
		,PublicRating = NewPublicRating
		,LastWinAt = NewLastWinAt
		,Division = NewDivision
	WHERE
		ClanID = NewClanID
		AND SeasonNumber=NewSeasonNumber
		AND TeamNumber=NewTeamNumber;
	SELECT 'Update' AS Outcome;
	END IF;
	COMMIT;
END;

create
    definer = gdog@`%` procedure usp_UpdateClans(IN NewClanID bigint unsigned, IN NewClanName varchar(256),
                                                 IN NewRealm varchar(3), IN NewClanTag varchar(5),
                                                 IN NewIsDisbanded tinyint)
BEGIN
	DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
		ROLLBACK;
        SELECT 'Error' AS Outcome;
    END;

	START TRANSACTION;
	IF NOT EXISTS (
		SELECT
			clanId
		FROM
			Clans
		WHERE
			clanId = newclanId)
		THEN
		INSERT INTO Clans(
			ClanID
			,ClanName
			,Realm
			,ClanTag
			,IsDisbanded
            ,LastUpdated
            ,LastSeen
            ,NeedsUpdate)
		VALUES
			(NewClanID
			,NewClanName
			,NewRealm
			,NewClanTag
			,NewIsDisbanded
            ,NOW()
            ,NOW()
            ,0);
        SELECT 'Success' AS Outcome;
	ELSE
	UPDATE Clans SET
		ClanID = NewClanID
		,ClanName = NewClanName
		,Realm = NewRealm
		,ClanTag = NewClanTag
		,IsDisbanded = NewIsDisbanded
        ,LastUpdated = NOW()
        ,NeedsUpdate=0
	WHERE
		clanId = NewclanId;
	SELECT 'Update' AS Outcome;
	END IF;
	COMMIT;
END;

create
    definer = gdog@`%` procedure usp_UpdateLiveDamage(IN NewClanID bigint, IN NewPlayerID bigint, IN NewGames int,
                                                      IN NewDamage float, IN NewFrags float,
                                                      IN Newlastbattletime datetime, IN NewSeason int)
BEGIN
	DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
    	ROLLBACK;
		SELECT 'Success' AS Outcome;
    END;


	IF NOT EXISTS (
		SELECT
			playerid
		FROM
			LiveDamage
		WHERE
			playerid = newplayerid
            AND Games = NewGames
            AND Season = NewSeason
            AND NewGames IS NOT NULL)

		THEN
		START TRANSACTION;
		INSERT INTO LiveDamage(
			ClanID
			,PlayerID
			,Games
			,Damage
			,Frags
			,lastbattletime
			,Season)
		VALUES
			(NewClanID
			,NewPlayerID
			,NewGames
			,NewDamage
			,NewFrags
			,Newlastbattletime
			,NewSeason);
		COMMIT;
		SELECT 'Success' AS Outcome;
	ELSE
		SELECT 'Exists' AS Outcome;
	END IF;
END;

create
    definer = gdog@`%` procedure usp_UpdateMaps(IN NewMapID bigint, IN NewMapName varchar(64), IN Icon varchar(256))
BEGIN
	DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
		ROLLBACK;
        SELECT 'Error' AS Outcome;
    END;

    START TRANSACTION;
    IF NOT EXISTS (
		SELECT
			MapId
		FROM
			Maps
		WHERE
			MapId = newMapId)
		THEN
		INSERT INTO Maps(
			MapID
            ,MapName
		    ,ImageURL)
		VALUES
			(NewMapID
			,NewMapName
			,Icon);
		SELECT 'Success' AS Outcome;
 	ELSE
		UPDATE Maps SET
			MapID = NewMapId
            ,MapName = NewMapName
		    ,ImageURL = Icon
		WHERE
			MapID=NewMapID;
		SELECT 'Update' AS Outcome;
	END IF;
    COMMIT;

END;

create
    definer = gdog@`%` procedure usp_UpdatePlayerRandomStats(IN NewplayerID bigint, IN NewshipID bigint,
                                                             IN NewGames int, IN NewWins int, IN NewSurvived int,
                                                             IN NewFrags float, IN NewDamage int, IN NewSpotting int,
                                                             IN NewTanked int, IN NewXP int,
                                                             IN NewMatchType varchar(16))
BEGIN
	DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
		ROLLBACK;
        SELECT 'Error' AS Outcome;
    END;

    START TRANSACTION;
    IF NOT EXISTS (
		SELECT
			ShipID
		FROM
			PlayerRandomStats
		WHERE
			PlayerID = NewPlayerID
            AND ShipID=NewShipID
            AND MatchType=NewMatchType)
		THEN
		INSERT INTO PlayerRandomStats(
			playerID
			,shipID
			,Games
			,Wins
			,Survived
			,Frags
			,Damage
			,Spotting
			,Tanked
			,XP
			,MatchType
			,LastUpdated)
		VALUES
			(NewplayerID
			,NewshipID
			,NewGames
			,NewWins
			,NewSurvived
			,NewFrags
			,NewDamage
			,NewSpotting
			,NewTanked
			,NewXP
			,NewMatchType
            ,NOW());
        SELECT 'Success' AS Outcome;
	ELSEIF EXISTS (
		SELECT
			ShipID
		FROM
			PlayerRandomStats
		WHERE
			ShipID=NewShipID
            AND PlayerID=NewPlayerID
            AND MatchType=NewMatchType
            AND Games < NewGames)
		THEN
		SET @ActionType = 'Update';
		UPDATE PlayerRandomStats SET
			 Games = NewGames
			,Wins = NewWins
			,Survived = NewSurvived
			,Frags = NewFrags
			,Damage = NewDamage
			,Spotting = NewSpotting
			,Tanked = NewTanked
			,XP = NewXP
            ,MatchType=NewMatchType
			,LastUpdated = NOW()
		WHERE
			PlayerID = NewPlayerID
			AND shipID = NewShipID
            AND Games < NewGames;
		SELECT 'Update' AS Outcome;
	ELSE
		SELECT 'Exists' AS Outcome;
	END IF;
    COMMIT;
END;

create
    definer = gdog@`%` procedure usp_UpdatePlayers(IN NewplayerID bigint unsigned, IN NewclanID bigint unsigned,
                                                   IN NewNickname varchar(64), IN NewRealm varchar(3),
                                                   IN NewisHidden tinyint)
BEGIN
	DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
		ROLLBACK;
        SELECT 'Error' AS Outcome;
    END;


	START TRANSACTION;
	IF NOT EXISTS (
		SELECT
			playerid
		FROM
			Players usp_UpdateCBTeams
		WHERE
			playerid = newplayerid)
		THEN
		INSERT INTO Players(
			`playerID`,
			`clanID`,
			`Nickname`,
			`Realm`,
			`isHidden`,
			`LastSeen`
            ,LastUpdated
            ,NeedsUpdate)
		VALUES
			(NewPlayerID
            ,NewclanID
            ,NewNickname
            ,NewRealm
            ,NewisHidden
            ,NOW()
            ,NOW()
            ,0);
        SELECT 'Success' AS Outcome;
	ELSE
	UPDATE Players SET
		playerID = NewPlayerID
		,clanID =NewclanID
		,Nickname =NewNickname
		,Realm =NewRealm
		,isHidden = NewisHidden
		,LastUpdated = NOW()
		,NeedsUpdate = 0
	WHERE
		playerID = NewPlayerID;
	SELECT 'Update' AS Outcome;
	END IF;
	COMMIT;
    CALL usp_HandleClanUpdates(NewClanID, NewRealm);
END;

create
    definer = gdog@`%` procedure usp_UpdateSeasons(IN NewSeason int, IN NewSeasonName varchar(64), IN NewMinTier int,
                                                   IN NewMaxTier int, IN NewStartDate datetime, IN NewEndDate datetime,
                                                   IN NewDivisionPoints int)
BEGIN
DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
		ROLLBACK;
        SELECT 'Error' AS Outcome;
    END;

    START TRANSACTION;
    IF NOT EXISTS (
		SELECT
			Season
		FROM
			Seasons
		WHERE
			Season = NewSeason)
		THEN
		INSERT INTO Seasons(
			Season
			,SeasonName
			,MinTier
			,MaxTier
			,StartDate
			,EndDate
			,DivisionPoints)
		VALUES
			(NewSeason
			,NewSeasonName
			,NewMinTier
			,NewMaxTier
			,NewStartDate
			,NewEndDate
			,NewDivisionPoints);
		SELECT 'Success' AS Outcome;
	ELSE
		UPDATE Seasons SET
			Season = NewSeason
			,SeasonName = NewSeasonName
			,MinTier = NewMinTier
			,MaxTier = NewMaxTier
			,StartDate = NewStartDate
			,EndDate = NewEndDate
			,DivisionPoints = NewDivisionPoints
		WHERE
			Season=NewSeason;
	SELECT 'Update' AS Outcome;
	END IF;
    COMMIT;
END;

create
    definer = gdog@`%` procedure usp_UpdateShip(IN NewShipID bigint, IN NewShipName varchar(128),
                                                IN NewShortName varchar(64), IN NewTier int, IN NewClass varchar(2),
                                                IN NewNation varchar(32))
BEGIN
	DECLARE EXIT HANDLER FOR SQLEXCEPTION
	BEGIN
		ROLLBACK;
		SELECT 'Error' AS Outcome;
	END;

	START TRANSACTION;
	IF NOT EXISTS (SELECT ShipID FROM ShipList WHERE ShipID=NewShipID) THEN
		INSERT INTO ShipList(
			shipID
			,shipName
			,shortName
			,Tier
			,Class
			,Nation)
		VALUES
			(NewshipID
			,NewshipName
			,NewshortName
			,NewTier
			,NewClass
			,NewNation);
	SELECT 'Success' AS Outcome;
	ELSEIF EXISTS (SELECT ShipID FROM ShipList WHERE ShipID=NewShipID) THEN
		UPDATE ShipList SET
			shipID = NewShipID
			,shipName = NewShipName
			,shortName = NewShortName
			,Tier = NewTier
			,Class = NewClass
			,Nation = NewNation
		WHERE
			shipID = NewShipID;
		SELECT 'Update' AS Outcome;
	ELSE
		SELECT 'Exists' AS Outcome;
	END IF;
	COMMIT;

END;

create
    definer = gdog@`%` procedure usp_Update_Sem_NewCBStats()
BEGIN
	DROP TABLE IF EXISTS sem;
	CREATE TEMPORARY TABLE sem AS
		SELECT
			PlayerID
			,Season
			,MAX(Games) AS Games
		FROM
			Sem_NewCBStats
		GROUP BY
			PlayerID
			,Season;

	INSERT INTO Sem_NewCBStats
		SELECT
			Players.Nickname
			,ClanTag AS PlayerClan
			,cur.Season
			,cur.GameTime
			,CAST(cur.GameTime AS DATE) AS GameDay
			,CASE WHEN prev.Damage IS NULL THEN 'Average' ELSE 'Precise' END AS StatType
			,cur.Games
			,cur.Wins
			,COALESCE(cur.wins - prev.wins, cur.wins/cur.games) AS Result # Have to allow NULL if unknowable
			,COALESCE(cur.SurvivedBattles-prev.SurvivedBattles, cur.survivedbattles/cur.games) AS Survived
			,COALESCE(cur.Damage-prev.Damage, cur.Damage/cur.Games) AS Damage
			,COALESCE(cur.Frags-prev.Frags, cur.Frags/cur.Games) AS Frags
			,COALESCE(cur.GunTanked-prev.GunTanked, cur.GunTanked/cur.Games) AS Tanked
			,COALESCE(cur.Spots-prev.Spots, cur.Spots/cur.Games) AS Spots
			,COALESCE(cur.SpottingDamage-prev.SpottingDamage, cur.SpottingDamage/cur.Games) AS Spotting
			,COALESCE(cur.MBFrags-prev.MBFrags, cur.MBFrags/cur.Games) AS MBFrags
			,COALESCE(cur.mbshots-prev.mbshots, cur.mbshots/cur.Games) AS MbShots
			,COALESCE(cur.mbhits-prev.mbhits, cur.mbhits/cur.Games) AS MbHits
			,COALESCE(cur.sbfrags-prev.sbfrags, cur.sbfrags/cur.Games) AS SbFrags
			,COALESCE(cur.sbshots-prev.sbshots, cur.sbshots/cur.Games) AS SbShots
			,COALESCE(cur.sbhits-prev.sbhits, cur.sbhits/cur.Games) AS SbHits
			,COALESCE(cur.torpfrags-prev.torpfrags, cur.torpfrags/cur.Games) AS TorpFrags
			,COALESCE(cur.torpshots-prev.torpshots, cur.torpshots/cur.Games) AS TorpShots
			,COALESCE(cur.torphits-prev.torphits, cur.torphits/cur.Games) AS TorpHits
			,COALESCE(cur.ramfrags-prev.ramfrags, cur.ramfrags/cur.Games) AS RamFrags
			,COALESCE(cur.cappts-prev.cappts, cur.cappts/cur.Games) AS Cappts
			,COALESCE(cur.droppedcappts-prev.droppedcappts, cur.droppedcappts/cur.Games) AS DroppedCappts
			,COALESCE(cur.controlcappts-prev.controlcappts, cur.controlcappts/cur.Games) AS ControlCappts
			,COALESCE(cur.controldroppedpts-prev.controldroppedpts, cur.controldroppedpts/cur.Games) AS ControlDroppedpts
			,COALESCE(cur.teamcappts-prev.teamcappts, cur.teamcappts/cur.Games) AS TeamCappts
			,COALESCE(cur.teamdroppedcappts-prev.teamdroppedcappts, cur.teamdroppedcappts/cur.Games) AS TeamDroppedCappts
			,cur.Priority
			,cur.PlayerID
		FROM
			CBGameStats as cur
			LEFT JOIN CBGameStats as prev ON cur.PlayerID=prev.PlayerID AND cur.Season=prev.Season AND cur.Games-1=prev.Games
			INNER JOIN Players ON cur.PlayerID=Players.PlayerID
			INNER JOIN Clans ON Players.ClanID=Clans.ClanID
			LEFT JOIN sem ON cur.playerid = sem.PlayerID AND cur.season = sem.Season
		WHERE
			cur.Games > sem.Games OR sem.Games IS NULL;

	UPDATE
		Sem_NewCBStats
		INNER JOIN CBGameStats as cur ON Sem_NewCBStats.PlayerID=cur.PlayerID AND Sem_NewCBStats.Season=cur.Season AND Sem_NewCBStats.Games = cur.Games AND Sem_NewCBStats.Priority < cur.Priority
	SET
		Sem_NewCBStats.GameTime = cur.GameTime
		,Sem_NewCBStats.GameDay = CAST(cur.GameTime AS DATE)
		,Sem_NewCBStats.Priority = cur.Priority
	WHERE
		Sem_NewCBStats.PlayerID=cur.PlayerID AND Sem_NewCBStats.Season=cur.Season AND Sem_NewCBStats.Games = cur.Games AND Sem_NewCBStats.Priority < cur.Priority;
	END;

create
    definer = gdog@`%` procedure usp_getTrackedClans()
BEGIN
	SELECT
		clanTag
        ,clanRealm
        ,clanId
        ,token
	FROM
		TrackedClans;
END;

create
    definer = gdog@`%` procedure usp_getWatchedClans()
BEGIN
	SELECT
		clanTag
        ,Realm
        ,clanId
	FROM
		Clans
	WHERE Tracked=1;
END;


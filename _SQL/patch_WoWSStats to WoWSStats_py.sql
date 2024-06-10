USE dev_wowsStats;

DROP PROCEDURE IF EXISTS  usp_LogError;
DROP PROCEDURE IF EXISTS  SystemdLog;
DROP TABLE IF EXISTS  ErrorLog;
DROP TABLE IF EXISTS systemd;
DROP PROCEDURE IF EXISTS usp_GetCBGames;
DROP PROCEDURE IF EXISTS usp_GetCBGamesList;
DROP PROCEDURE IF EXISTS usp_GetClanByID;
DROP PROCEDURE IF EXISTS usp_GetClanByTag;
DROP PROCEDURE IF EXISTS usp_GetShip;
DROP PROCEDURE IF EXISTS usp_GetShipByID;
DROP PROCEDURE IF EXISTS usp_GetShipByName;

DROP PROCEDURE IF EXISTS usp_UpdateCBGameStats;

CREATE PROCEDURE usp_UpdateCBGameStats(IN NewPlayerID BIGINT,IN NewGameTime DATETIME,IN NewSeason INT,
													   IN NewGames INT,IN NewWins INT,IN NewLosses INT,IN NewDraws INT,
													   IN NewSurvivedBattles INT,IN NewSurvivedWins INT,
													   IN NewDamage BIGINT,IN NewFrags INT,IN NewMBFrags INT,
													   IN NewSBFrags INT,IN NewTorpFrags INT,IN NewPlaneFrags INT,
													   IN NewRamFrags INT,IN NewMBShots INT,IN NewSBShots INT,
													   IN NewTorpShots INT,IN NewMBHits INT,IN NewSBHits INT,
													   IN NewTorpHits INT,IN NewGunTanked INT,IN NewTorpTanked INT,
													   IN NewSpots INT,IN NewSpottingDamage BIGINT,
													   IN NewPlanesKilled INT,IN NewDroppedCapPts INT,IN NewCapPts INT,
													   IN NewControlCapPts INT,IN NewControlDroppedPts INT,
													   IN NewTeamCapPts INT,IN NewTeamDroppedCapPts INT,
													   IN NewPriority INT)
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

DROP PROCEDURE IF EXISTS usp_Client_UpdateCBGameStats;
CREATE PROCEDURE usp_Client_UpdateCBGameStats(IN NewPlayerID BIGINT,IN NewGameTime DATETIME,
															  IN NewSeason INT,IN NewGames INT,IN NewWins INT,
															  IN NewLosses INT,IN NewDraws INT,
															  IN NewSurvivedBattles INT,IN NewSurvivedWins INT,
															  IN NewDamage BIGINT,IN NewFrags INT,IN NewMBFrags INT,
															  IN NewSBFrags INT,IN NewTorpFrags INT,
															  IN NewPlaneFrags INT,IN NewRamFrags INT,IN NewMBShots INT,
															  IN NewSBShots INT,IN NewTorpShots INT,IN NewMBHits INT,
															  IN NewSBHits INT,IN NewTorpHits INT,IN NewGunTanked INT,
															  IN NewTorpTanked INT,IN NewSpots INT,
															  IN NewSpottingDamage BIGINT,IN NewPlanesKilled INT,
															  IN NewDroppedCapPts INT,IN NewCapPts INT,
															  IN NewControlCapPts INT,IN NewControlDroppedPts INT,
															  IN NewTeamCapPts INT,IN NewTeamDroppedCapPts INT)
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

DROP PROCEDURE IF EXISTS usp_HandleClanUpdates;

CREATE PROCEDURE usp_HandleClanUpdates(IN NewClanID BIGINT,IN NewRealm VARCHAR(3))
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

DROP PROCEDURE IF EXISTS usp_HandlePlayerUpdates;
CREATE PROCEDURE usp_HandlePlayerUpdates(IN NewPlayerID BIGINT,IN NewRealm VARCHAR(3))
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

DROP PROCEDURE IF EXISTS usp_UpdateCBGames;
CREATE PROCEDURE usp_UpdateCBGames(IN NewgameID BIGINT,IN NewmapID BIGINT,IN Newseason INT,
												   IN NewclusterID BIGINT,IN NewarenaID BIGINT,
												   IN NewfinishedAt DATETIME)
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

DROP PROCEDURE IF EXISTS usp_UpdateCBGameStats;

CREATE PROCEDURE usp_UpdateCBGameStats(IN NewPlayerID BIGINT,IN NewGameTime DATETIME,IN NewSeason INT,
													   IN NewGames INT,IN NewWins INT,IN NewLosses INT,IN NewDraws INT,
													   IN NewSurvivedBattles INT,IN NewSurvivedWins INT,
													   IN NewDamage BIGINT,IN NewFrags INT,IN NewMBFrags INT,
													   IN NewSBFrags INT,IN NewTorpFrags INT,IN NewPlaneFrags INT,
													   IN NewRamFrags INT,IN NewMBShots INT,IN NewSBShots INT,
													   IN NewTorpShots INT,IN NewMBHits INT,IN NewSBHits INT,
													   IN NewTorpHits INT,IN NewGunTanked INT,IN NewTorpTanked INT,
													   IN NewSpots INT,IN NewSpottingDamage BIGINT,
													   IN NewPlanesKilled INT,IN NewDroppedCapPts INT,IN NewCapPts INT,
													   IN NewControlCapPts INT,IN NewControlDroppedPts INT,
													   IN NewTeamCapPts INT,IN NewTeamDroppedCapPts INT,
													   IN NewPriority INT)
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

DROP PROCEDURE IF EXISTS usp_UpdateCBPlayers;
CREATE PROCEDURE usp_UpdateCBPlayers(IN newteamID BIGINT,IN newplayerID BIGINT,IN newshipID BIGINT,
													 IN newSurvived TINYINT(1),IN newRealm VARCHAR(3))
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

DROP PROCEDURE IF EXISTS usp_UpdateCBTeams;
CREATE PROCEDURE usp_UpdateCBTeams(IN newgameID BIGINT,IN newteamID BIGINT,IN newclanID BIGINT,
												   IN newrealm VARCHAR(3),IN newteamAB VARCHAR(1),IN newleague INT,
												   IN newdivision INT,IN newrating INT,IN newratingdelta INT,
												   IN newresult TINYINT(1))
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

DROP PROCEDURE IF EXISTS usp_UpdateClanRatings;
CREATE PROCEDURE usp_UpdateClanRatings(IN NewClanID BIGINT,IN NewGames INT,IN NewLeague INT,
													   IN NewMaxPositionPublicRating INT,
													   IN NewMaxPositionDivisionRating INT,IN NewMAXPositionLeague INT,
													   IN NewMAXPositionDivision INT,IN NewWins INT,
													   IN NewInitialPublicRating INT,
													   IN NewIsBestSeasonRating TINYINT(1),IN NewTeamNumber INT,
													   IN NewIsQualified TINYINT(1),IN NewRatingID BIGINT,
													   IN NewCurrentWinStreak INT,IN NewActiveStatus VARCHAR(32),
													   IN NewSeasonNumber INT,IN NewDivisionRatingMax INT,
													   IN NewRealm VARCHAR(2),IN NewDivisionRating INT,
													   IN NewLongestWinningStreak INT,IN NewMaxPublicRating INT,
													   IN NewPublicRating INT,IN NewLastWinAt DATETIME,
													   IN NewDivision INT)
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

DROP PROCEDURE IF EXISTS usp_UpdateClans;
CREATE PROCEDURE usp_UpdateClans(IN NewClanID BIGINT UNSIGNED,IN NewClanName VARCHAR(256),
												 IN NewRealm VARCHAR(3),IN NewClanTag VARCHAR(5),
												 IN NewIsDisbanded TINYINT)
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

DROP PROCEDURE IF EXISTS usp_UpdateLiveDamage;

CREATE PROCEDURE usp_UpdateLiveDamage(IN NewClanID BIGINT,IN NewPlayerID BIGINT,IN NewGames INT,
													  IN NewDamage FLOAT,IN NewFrags FLOAT,
													  IN Newlastbattletime DATETIME,IN NewSeason INT)
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


DROP PROCEDURE IF EXISTS usp_UpdateMaps;
CREATE PROCEDURE usp_UpdateMaps(IN NewMapID BIGINT,IN NewMapName VARCHAR(64),IN Icon VARCHAR(256))
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

DROP PROCEDURE usp_UpdatePlayerRandomStats;
CREATE PROCEDURE usp_UpdatePlayerRandomStats(IN NewplayerID BIGINT,IN NewshipID BIGINT,IN NewGames INT,
															 IN NewWins INT,IN NewSurvived INT,IN NewFrags FLOAT,
															 IN NewDamage INT,IN NewSpotting INT,IN NewTanked INT,
															 IN NewXP INT,IN NewMatchType VARCHAR(16))
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

DROP PROCEDURE usp_UpdatePlayers;
CREATE PROCEDURE usp_UpdatePlayers(IN NewplayerID BIGINT UNSIGNED,IN NewclanID BIGINT UNSIGNED,
												   IN NewNickname VARCHAR(64),IN NewRealm VARCHAR(3),
												   IN NewisHidden TINYINT)
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

DROP PROCEDURE IF EXISTS usp_UpdateSeasons;
CREATE PROCEDURE usp_UpdateSeasons(IN NewSeason INT,IN NewSeasonName VARCHAR(64),IN NewMinTier INT,
												   IN NewMaxTier INT,IN NewStartDate DATETIME,IN NewEndDate DATETIME,
												   IN NewDivisionPoints INT)
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

DROP PROCEDURE IF EXISTS usp_UpdateShip;
CREATE PROCEDURE usp_UpdateShip(IN NewShipID BIGINT,IN NewShipName VARCHAR(128),
												IN NewShortName VARCHAR(64),IN NewTier INT,IN NewClass VARCHAR(2),
												IN NewNation VARCHAR(32))
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
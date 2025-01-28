# wowsstats/functions/__init__.py

# fetch data from web "wrappers" with 3 different methods
from .WEBGET_API import WEBGET_API
from .WEBGET_API_IMPROPER import WEBGET_API_IMPROPER
from .WEBGET_SCRAPE import WEBGET_SCRAPE

# fetch actual data thru the 3 wrappers
from .WEBGET_Maps import WEBGET_Maps
from .WEBGET_Ships import WEBGET_Ships
from .WEBGET_Player import WEBGET_Player
from .WEBGET_CBGames import WEBGET_CBGames
from .WEBGET_ClanData import WEBGET_ClanData
from .WEBGET_CBGamestats import WEBGET_CBGamestats
from .WEBGET_PlayerRandomStats import WEBGET_PlayerRandomStats
from .WEBGET_ClanBattleSeasons import WEBGET_ClanBattleSeasons
from .WEBGET_CaptureIncrementalDamage import WEBGET_CaptureIncrementalDamage
from .WEBGET_ClanPreviousSeasons import WEBGET_ClanPreviousSeasons

# create DB connection
from .SQL_CreateDatabaseConnection import CreateDatabaseConnection

# fetch data from DB
from .SQLGET_WatchedClans import SQLGET_WatchedClans
from .SQLGET_ShipBy import SQLGET_ShipBy
from .SQLGET_Seasons import SQLGET_Seasons
from .SQLGET_CurrentSeason import SQLGET_CurrentSeason
from .SQLGET_TrackedClans import SQLGET_TrackedClans
from .SQLGET_ClansToUpdate import SQLGET_ClansToUpdate
from .SQLGET_PlayersToUpdate import SQLGET_PlayersToUpdate
from .SQLGET_GetPlayersWithNewCBs import SQLGET_GetPlayersWithNewCBs
from .SQLGET_RecheckCBStats import SQLGET_RecheckCBStats
from .SQLGET_RandomPlayersToUpdate import SQLGET_RandomPlayersToUpdate
from .SQLGET_CurrentSeasonClans import SQLGET_CurrentSeasonClans
from .SQLGET_MissingHistoryClans import SQLGET_MissingHistoryClans
from .SQLGET_TestResults import SQLGET_TestResults

# purge DB
from .SQLPUT_PurgeDb import SQLPUT_PurgeDb

# batch processes calling multiple this from above
from .BATCH_UpdateClans import BATCH_UpdateClans
from .BATCH_PlayersFromClan import BATCH_PlayersFromClan
from .BATCH_AddPlayersToPlayers import BATCH_AddPlayersToPlayers
from .BATCH_CaptureIncDmgFromAllClans import BATCH_CaptureIncDmgFromAllClans
from .BATCH_GetAllCBGamestats import BATCH_GetAllCBGamestats

# convert Python None type to SQL NULL type
from .SqlWrap import SqlWrap

# logging (duh)
#from .Logging import setup_logging, debug_logging
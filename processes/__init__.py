# wowsstats/processes/__init__.py

from .UPDATE_PlayerRandomStats import UPDATE_PlayerRandomStats
from .UPDATE_Players import UPDATE_Players
from .UPDATE_Clans import UPDATE_Clans
from .UPDATE_TrackedClans import UPDATE_TrackedClans

from .SCRAPE_CBStats import SCRAPE_CBStats
from .SCRAPE_CBGames import SCRAPE_CBGames
from .SCRAPE_CBClanHistory import SCRAPE_CBClanHistory

from .CSV_GetStats import CSV_GetStats

from .SCHED_Random import SCHED_Random
from .SCHED_Monthly import SCHED_Monthly
from .SCHED_Weekly import SCHED_Weekly
from .SCHED_Hourly import SCHED_Hourly
from .SCHED_Daily import SCHED_Daily
from .SCHED_4m import SCHED_4m
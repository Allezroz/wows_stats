# /wows_stats/__main__.py

# run with python -m wows_stats as a module

# python modules
import sys, argparse, logging

# config functions
from wows_stats.conf import setup_logging, debug_logging, credentials, config, CreateDatabaseConnection


# parse command line arguments
parser = argparse.ArgumentParser(prog='wows_stats', description='Helpful text here')

parser.add_argument('--log-level', type=str, default='INFO', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], help='logging level output')
parser.add_argument('--env', type=str, default='dev', choices=['test', 'dev', 'prod'], help='SQL database environment')
parser.add_argument('--run', type=str, required=True, choices=['TEST_FULL', 'SCHED_4m', 'SCHED_Hourly', 'SCHED_Daily', 'SCHED_Weekly', 'SCHED_Monthly', 'SCHED_All', 'SCHED_Random', 'CLIENT', 'TEST_CBStats', 'panel','CSV_GetStats'], help='process to run')

# show help only if no args provided and abort
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

args = parser.parse_args()
# import order is important for fancy config import to work, else imported config has uninitialized values
config.env = args.env


# set up appid
creds = credentials[config.env]
config.appid = creds["appid"]

#open connection
config.dbcon = CreateDatabaseConnection(creds)  # Initialize config.dbcon

# Setup logging configuration with the cmd line specified log level
setup_logging(args.log_level)

# log start of module
logger = logging.getLogger(__name__)
logger.info(f"Started {__package__}")
logger.info(f"Running on {config.env} Environment, log level is {args.log_level}")

if args.run == 'TEST_FULL':
    logger = logging.getLogger("TEST_FULL")
    from wows_stats.scrape import UpdateShips, UpdateMaps, UpdatePlayerRandomStats, UpdatePlayer, UpdateClan, UpdateClanHistory, UpdateSeasons, UpdateCBGameStats, UpdateLiveDamage, UpdateCBGames

    logger.info(f"Running {args.run}")

    UpdateShips = UpdateShips()
    UpdateMaps = UpdateMaps()
    UpdatePlayerRandomStats = UpdatePlayerRandomStats(556002838,"eu")
    UpdatePlayer=UpdatePlayer(556002838,"eu")
    UpdateClan=UpdateClan(500142948, "eu")
    UpdateClanHistory = UpdateClanHistory(500142948, "eu")
    UpdateSeasons=UpdateSeasons()
    UpdateCBGameStats=UpdateCBGameStats(556002838,"eu",25,'2024-06-10',0)
    UpdateLiveDamage=UpdateLiveDamage(500142948,"eu",25)
    UpdateCBGames=UpdateCBGames()

    logger.info(' ')
    logger.info(f"Finished {args.run }")
    logger.info("*********************")
    logger.info("Individual Module Results")
    logger.info("*********************")

    logger.info(UpdateShips)
    logger.info(UpdateMaps)
    logger.info(UpdateSeasons)
    logger.info(UpdatePlayerRandomStats)
    logger.info(UpdatePlayer)
    logger.info(UpdateClan)
    logger.info(UpdateClanHistory)
    logger.info(UpdateCBGameStats)
    logger.info(UpdateLiveDamage)
    logger.info(UpdateCBGames)
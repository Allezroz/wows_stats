# wowsstats/__main__.py

# run with python -m wowsstats as a module

# python modules
import time, datetime, sys, argparse, logging

# our logging config file
import logging.config

# logging functions
from wowsstats.wowsstatslogging import setup_logging, debug_logging

# parse command line arguments
parser = argparse.ArgumentParser(prog='wowsstats', description='Helpful text here')

parser.add_argument('--log-level', type=str, default='INFO', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], help='logging level output')
parser.add_argument('--env', type=str, required=True, choices=['test', 'dev', 'prod'], default='dev', help='SQL database environment')
parser.add_argument('--run', type=str, default='panel',  required=True, choices=['TEST_FULL', 'SCHED_4m', 'SCHED_Hourly', 'SCHED_Daily', 'SCHED_Weekly', 'SCHED_Monthly', 'SCHED_All', 'SCHED_Random', 'CLIENT', 'TEST_CBStats'], help='process to run')

# show help only if no args provided and abort
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

args = parser.parse_args()

# set up appid
from wowsstats.agentcreds import environment
creds = environment[config.env]
config.appid = creds["appid"]

# Setup logging configuration with the cmd line specified log level
setup_logging(args.log_level)

# log start of module
logger = logging.getLogger(__name__)
logger.info(f"Started {__package__}")
logger.info(f"Running on {config.env} Environment, log level is {args.log_level}")

# Execute the appropriate function based on the user's choice
def full_run():
    from wows_stats.processes import SCHED_4m
    from wows_stats.processes import SCHED_Daily
    from wows_stats.processes import SCHED_Hourly
    from wows_stats.processes import SCHED_Weekly
    from wows_stats.processes import SCHED_Monthly
    from wows_stats.processes import SCHED_Random
    # ordering needs to be in this order
    SCHED_Monthly()
    SCHED_Weekly()
    SCHED_Hourly()
    SCHED_Daily()
    SCHED_4m()
    SCHED_Random()

if args.run == 'SCHED_4m':

    from wowsstats.processes import SCHED_4m
    SCHED_4m()

elif args.run == 'SCHED_Daily':

    from wowsstats.processes import SCHED_Daily
    SCHED_Daily()

elif args.run == 'SCHED_Hourly':

    from wowsstats.processes import SCHED_Hourly
    SCHED_Hourly()

elif args.run == 'SCHED_Weekly':

    from wowsstats.processes import SCHED_Weekly
    SCHED_Weekly()

elif args.run == 'SCHED_Monthly':

    from wowsstats.processes import SCHED_Monthly
    # currently takes about 22 minutes to run
    SCHED_Monthly()

elif args.run == 'SCHED_All':

    full_run()

elif args.run == 'TEST_ALL':
    from wowsstats.functions import SQLPUT_PurgeDb
    SQLPUT_PurgeDb()

    full_run()

elif args.run == 'SCHED_Random':
    from wowsstats.processes import SCHED_Random
    SCHED_Random()

elif args.run == 'CLIENT':
    from wowsstats.wowsstats_client import client
    client()

elif args.run == 'TEST_CBStats':
    from wowsstats.functions import BATCH_GetAllCBGamestats
    BATCH_GetAllCBGamestats([{"PlayerID":556002838,"Realm":'eu',"Timestamp":'1950-01-01'}], 24, 1) 

elif args.run == 'CSV_GetStats':
    from wowsstats.processes import CSV_GetStats
    CSV_GetStats()

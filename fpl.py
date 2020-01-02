import json
import csv
import logging
import sys
import requests
import argparse
from tqdm import tqdm

MAIN_URL = "https://fantasy.premierleague.com/api/"
LOGIN_URL = "https://users.premierleague.com/accounts/login/"
USER_SUMMARY_SUBURL = "element-summary/"
TEAM_ENTRY_SUBURL = "entry/"
PLAYERS_INFO_SUBURL = "bootstrap-static/"

'''
Note: After /drf to /api, env is required for API to work
USERNAME = ###
PASSWORD = ###
'''



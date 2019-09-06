#!/usr/bin/env python
"""This script reads the API credentials from a file
and initializes Twython with them"""

from twython import Twython

with open('/twitter_bot/twitter-creds') as api_creds:
    lines = api_creds.read().splitlines()

api = Twython(*lines)

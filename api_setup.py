#!/usr/bin/env python
"""This script reads the API credentials from a file
and initializes Twython with them"""

from twython import Twython

with open('/twitter_bot/twitter-creds') as f:
    lines = f.read().splitlines()

api = Twython(*lines)

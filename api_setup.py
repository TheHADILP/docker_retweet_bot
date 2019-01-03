#!/usr/bin/env python
import sys
from twython import Twython, TwythonError

with open('/twitter_bot/twitter-creds') as f:
    lines = f.read().splitlines()

api = Twython(*lines)

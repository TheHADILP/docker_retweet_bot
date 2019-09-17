#!/usr/bin/env python
# coding: utf8
"""This script checks tweets of defined users for defined hashtags in random order.
When a suitable tweet is found, which wasn't previously retweeted, it gets retweeted"""

import random
import time
from twython import TwythonError

import api_setup

while True:
    with open('/twitter_bot/users') as user_list:
        users = user_list.read().splitlines()

    while True:
        try:
            if users:
                selected = users[random.randint(0, len(users))-1]
                users.remove(selected)
                print(str(selected) + ':')

                try:
                    timeline = api_setup.api.get_user_timeline(
                        screen_name=selected,
                        count=1,
                        exclude_replies='true',
                        include_rts='true')
                except TwythonError as e:
                    print(e)

                for tweet in timeline:
                    nId = tweet['id_str']

                    with open('/twitter_bot/buzzwords') as buzzword_list:
                        buzzwords = buzzword_list.read().splitlines()

                    if any(n in tweet['text'] for n in buzzwords):

                        if nId not in open('/twitter_bot/retweet-blacklist').read():
                            print('    ID: ' + nId)
                            print('')
                            print(tweet['text'])
                            print('')
                            print('    Tweeted!!!')
                            with open('/twitter_bot/retweet-blacklist', 'a') as blacklist:
                                blacklist.write('\n' + nId)

                            api_setup.api.retweet(id=nId)
                            time.sleep(900)
                        else:
                            print('    Duplicate tweet found')
                            time.sleep(2)
                            break
                    else:
                        print('    No matching tweet found')
                        time.sleep(2)
                        break
            else:
                print('User list empty, starting over...')
                time.sleep(5)
                break
        except TwythonError as e:
            print(e)

#!/usr/bin/env python
# coding: utf8

import api_setup

import random
import time
from twython import TwythonError

while True:
    #checks if it contains certain hashtags + goes on until suitable tweet is found + checks if not previously retweeted by me
    with open('/twitter_bot/users') as f:
        users = f.read().splitlines()

    while True:
        try:
            if len(users) > 0:
                selected = users[random.randint(0,len(users))-1]
                users.remove(selected)
                print (selected)

                try:
                    timeline = api_setup.api.get_user_timeline(screen_name=selected, count=1, exclude_replies='true', include_rts='true')
                except TwythonError as e:
                    print (e)

                for tweet in timeline:
                    nId = tweet['id_str']

                    with open('/twitter_bot/buzzwords') as f:
                        buzzwords = f.read().splitlines()

                    if any(n in tweet['text'] for n in buzzwords):

                        if nId not in open('/twitter_bot/retweet-blacklist').read():
                            print ('nId: ' + nId)
                            print (tweet['text'].encode('utf-8'))
                            print ('     TWEETED!!! (NEW ON MY PROFILE)                  #####')
                            print ('')
                            with open('/twitter_bot/retweet-blacklist', 'a') as file:
                                file.write('\n' + nId)

                            api_setup.api.retweet(id = nId)
                            time.sleep(900)
                        else:
                            print ('     DUPLICATE FOUND')
                            time.sleep(2)
                            break
                    else:
                         print ('     NOTHING FOUND YET')
                         time.sleep(2)
                         break
            else:
                print ('EMPTY, RESTARTING SCRIPT...')
                time.sleep(5)
                break
        except TwythonError as e:
            print (e)


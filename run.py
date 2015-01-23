#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import tweepy
from tweepy.error import TweepError
# import random
# import json
# from replies import replies_dict, nothing_found

API_KEY = os.getenv('API_KEY', '')
API_SECRET = os.getenv('API_SECRET', '')
CLIENT_TOKEN = os.getenv('CLIENT_TOKEN', '')
CLIENT_SECRET = os.getenv('CLIENT_SECRET', '')
USER_LIST = ['asmaps']

try:
    from credentials import API_KEY
except ImportError:
    pass

try:
    from credentials import API_SECRET
except ImportError:
    pass

try:
    from credentials import CLIENT_TOKEN
except ImportError:
    pass

try:
    from credentials import CLIENT_SECRET
except ImportError:
    pass

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(CLIENT_TOKEN, CLIENT_SECRET)
api = tweepy.API(auth)

print('Hello world')

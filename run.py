#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import tweepy
from tweepy.error import TweepError
# import random
# import json
# from replies import replies_dict, nothing_found

API_KEY = os.environ('API_KEY')
API_SECRET = os.environ('API_SECRET')
CLIENT_TOKEN = os.environ('CLIENT_TOKEN')
CLIENT_SECRET = os.environ('CLIENT_SECRET')
USER_LIST = ['asmaps']


auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(CLIENT_TOKEN, CLIENT_SECRET)
api = tweepy.API(auth)

print('Hello world')

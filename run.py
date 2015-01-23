#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import tweepy
from tweepy.error import TweepError
# import random
import json
import time

# from replies import replies_dict, nothing_found

API_KEY = os.getenv('API_KEY', '')
API_SECRET = os.getenv('API_SECRET', '')
CLIENT_TOKEN = os.getenv('CLIENT_TOKEN', '')
CLIENT_SECRET = os.getenv('CLIENT_SECRET', '')

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


class StdOutListener(tweepy.streaming.StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    last_own_tweet = 0
    questions = []

    def on_data(self, data):
        data = json.loads(data)
        username = data.get('user').get('screen_name')
        text = data.get('text')
        import pprint
        if not data.get('in_reply_to_screen_name') and\
                not data.get('in_reply_to_status_id') and\
                not data.get('in_reply_to_user_id') and\
                self.last_own_tweet + 5 < time.time():
            if text[-1:] == '?' and text.lower().startswith('why'):
                self.questions.append({
                    'username': username,
                    'id': data.get('id'),
                    'text': text
                })
            elif 'because' in text.lower() and len(self.questions) > 0:
                answer = text[text.lower().find('because'):]
                qdata = self.questions.pop()
                print("Answering: " + qdata['text'])
                print(answer)
                print('####################')
                status = u'@{user} {answer}'.format(user=qdata['username'], answer=answer)
                if len(status) <= 140:
                    api.update_status(
                        status=status,
                        in_reply_to_status_id=qdata['id'])
                    self.last_own_tweet = time.time()
        if str(data.get('in_reply_to_screen_name')).lower() == 'kakarubot':
            answer = "I'm a bot automatically answering to all questions on twitter. Sorry for confusion! {t}".\
                format(t=str(time.time()))
            print('####################')
            print('Got answer from @{user}: {answer}'.format(user=username, answer=text))
            print('Replying: ' + answer)
            print('####################')
            api.update_status(
                status=u'@{user} {answer}'.format(user=username, answer=answer),
                in_reply_to_status_id=data.get('id'))

        return True

    def on_error(self, status):
        print(status)

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(CLIENT_TOKEN, CLIENT_SECRET)
api = tweepy.API(auth)

l = StdOutListener()
stream = tweepy.Stream(auth, l)

while True:
    try:
        stream.filter(track=["why", "Because", "@KakaruBot"],
                      languages=['de', 'en'],
                      follow=[])
    except TweepError as e:
        print(str(e))

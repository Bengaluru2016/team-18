#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys

argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'eLHaFLZtPFLvKMil82EP8R7ut'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'QlEiwAN1ttEBFhsM7JaOZfzm6H1AtOyoE6hZ8voqMJUAUE0lda'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '707149018376241154-kPIvw0jULdJ3icIPUWTfM24pjuy7CyX'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'KgzE9XjWtowzTgp1OjIgVaS4hynv3IH7ETjzJVzkX9yKg'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(900)#Tweet every 15 minutes


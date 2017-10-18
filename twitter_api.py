# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 20:44:14 2017

@author: roby
"""
#api twitter

from twython import Twython

CONSUMER_KEY='XbLF8p1CGupK0nP6FFldRdrtL'
CONSUMER_SECRET='aprahPY5oG9w2WSjhkLXmbaXBIlt3Vd8VGnCOPjRn7hTXrFsay'
twitter=Twython(CONSUMER_KEY,CONSUMER_SECRET)

for status in twitter.search(q='"data science"')["statuses"]:
    user=status["user"]["screen_name"].encode('utf-8')
    text=status["text"].encode('utf-8')
    print user,":",text
    print
    

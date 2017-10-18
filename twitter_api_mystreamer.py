# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 23:15:06 2017

@author: roby
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 20:44:14 2017

@author: roby
"""
#api twitter versione 2
#invoco la classe TwythonStreamer e faccio l'override del metodo on success
#trovo solo i tweet in inglese e solo i primi 1000

from twython import TwythonStreamer
from collections import Counter

CONSUMER_KEY='XbLF8p1CGupK0nP6FFldRdrtL'
CONSUMER_SECRET='aprahPY5oG9w2WSjhkLXmbaXBIlt3Vd8VGnCOPjRn7hTXrFsay'
ACCESS_TOKEN='181748607-hqYCpnnxLJ52VWFdOkNUjIFeVkuXbDcPPhEF4I2e'
ACCESS_TOKEN_SECRET='M8UH8OcgVlA6KTVhUump1czcQ0SN8VfZIruxCMdyU6Sn9'

tweets=[]

class MyStreamer(TwythonStreamer):
    def on_success(self,data):
        if data['lang']=='en':
            tweets.append(data)
            #print "received tweet #", len(tweets)
            
        if len(tweets)>=100:
            self.disconnect()
            
    def on_error(self,status_code,data):
        print status_code,data
        self.disconnect()


stream=MyStreamer(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
stream.statuses.filter(track='data')

top_hashtags=Counter(hashtag['text'].lower() for tweet in tweets for hashtag in tweet["entities"]["hashtags"])
print top_hashtags.most_common(5)



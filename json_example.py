# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 21:57:01 2017

@author: roby
"""
#uso del json per serializzare e deserializzare dati
from dateutil.parser import parse
import json, requests, collections

serialized="""{ "title":"data science book", 
                "author":"joel",
                "year":2014,
                "topics":["data","science","data science"]}"""

deserialized=json.loads(serialized)
if "data science" in deserialized["title"]:
    print deserialized
    
#importo una api non autenticata 
endpoint="https://api.github.com/users/joelgrus/repos"
#carico la lista dei dict presenti nell'api 
repos=json.loads(requests.get(endpoint).text)
#print(str(repos[0]))
dates=[parse(repo["created_at"]) for repo in repos]
month_counts=collections.Counter(date.month for date in dates)
weekday_counts=collections.Counter(date.weekday() for date in dates)


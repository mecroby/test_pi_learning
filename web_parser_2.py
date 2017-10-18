# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 21:50:58 2017

@author: roby
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 21:13:58 2017

@author: roby
"""
#web parser
from bs4 import BeautifulSoup
import requests

url="http://shop.oreilly.com/category/browse-subject/data.do?sortby=pubblicationDate&page=1"

soup=BeautifulSoup(requests.get(url).text,'html5lib')
tds=soup('td','thumbtext')
print len(tds)

def is_video(td):
    pricelabels=td('span','pricelabel')
    return (len(pricelabels)==1 and pricelabels[0].text.strip().startswith("Video"))
print len([td for td in tds if not is_video(td)])


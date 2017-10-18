# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 21:13:58 2017

@author: roby
"""
#web parser
from bs4 import BeautifulSoup
import requests
html=requests.get("http://www.example.com").text
soup=BeautifulSoup(html,'html5lib')
#trova il primo elemento tag p ed il suo contenuto
first_par=soup.find('p')
#trova il primo testo del tag p e lo splitta parola per parola
first_par_text=soup.find('p').text
first_par_words=soup.find('p').text.split()

first_par_id=soup.find('p').get('id')
#first_par_id_2=soup.p['id']

 #per trovare tutti i p
all_phar=soup.find_all('p')
all_phar_id=[p for p in soup('p') if p.get('id')]

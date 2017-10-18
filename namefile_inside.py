# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 21:20:06 2017

@author: roby
"""
#apertura del file direttamente da dentro il codice
import re
import sys 
#importo la libreria reguar expression

try:
    lettera_inizio=str(sys.argv[1])
except:
     print "inserire la lettera da cercare"
     sys.exit(1)
    
start_with_ash=0
with open('mastro.txt','r') as f:
    for line in f:
        if re.match(lettera_inizio,line):
                    start_with_ash+=1
                    
sys.stdout.write("linee che iniziano con ")
sys.stdout.write(lettera_inizio)
sys.stdout.write("\t")
sys.stdout.write(str(start_with_ash))
sys.stdout.write("\n")
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 20:33:49 2017

@author: roby
"""
#dato un numero n, restituisce le prime n parole più usate
import sys 
from collections import Counter

try:
    num_words=int(sys.argv[1])
except:
    print "usage: nomefile.py numero_parole"
    sys.exit(1)
    
counter= Counter(word.lower() for line in sys.stdin for word in line.strip().split() if word)

for  word, count in counter.most_common(num_words):
    sys.stdout.write(str(count))
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write("\n")
    
    
        

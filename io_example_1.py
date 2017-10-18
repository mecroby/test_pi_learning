# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 12:43:17 2017

@author: roby
"""
#esempio stdin /stdout
import sys, re
nome=sys.argv[0]
regex=sys.argv[1]

for line in sys.stdin:
    if re.search(regex,line):
        sys.stdout.write(line)
        

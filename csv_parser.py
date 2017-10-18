# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 21:10:52 2017

@author: roby
"""
#data parsing di file csv con valori errati
import dateutil.parser
import csv

def parse_row(input_row, parsers):
    
    #return [parser(value) if parser is not None else value for value, parser in zip(input_row,parsers)]
     return [try_or_none(parser)(value) if parser is not None else value for value, parser in zip(input_row,parsers)]

def parse_rows_with(reader,parsers):
    for row in reader:
        yield parse_row(row,parsers)

def try_or_none(f):
    def f_or_none(x):
        try: return f(x)
        except: return None
    return f_or_none
    
data=[]
with open("data_bad.txt","rb") as f:
    reader=csv.reader(f)
    for line in parse_rows_with(reader,[dateutil.parser.parse, None, float]):
        data.append(line)
#stampo solo la riga che contiene un valore none ==>non è stato parserizzato
for row in data:
    if any(x is None for x in row):
        print row


def try_parse_field(field_name,value,parser_dict):
    parser=parser_dict.get(field_name)
    if parser is not None:
        return try_or_none(parser)(value)
    else:
        return value

def parse_dict(input_dict,parser_dict):
    return {field_name:try_parse_field(field_name,value.parser_dict)
            for field_name, value in input_dict.iteritems()}
    
    
    
#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import numpy as np
import sys

def mapper():
	arr = []
	word = ""

	for line in sys.stdin:
	    line=line.strip()
	    word=line.split(',')
	    arr.append([word[0],word[1]])

	df=pd.DataFrame(data=arr, columns=['userid','placeid']) 
	df['count'] = 1
	counter = []

	for i in range(len(df['userid'])):
	    counter.append(df[(df['userid'] == df['userid'][i]) & (df['placeid'] == df['placeid'][i])]['count'].sum())

	data = {'userid':df['userid'], 'placeid':df['placeid'], 'count':counter}
	df = pd.DataFrame(data)

	count = 0
	for i in range(len(df['userid'])):
	    print(df['userid'][i] , "," , df['placeid'][i] , "," , df['count'][i])
mapper()
	    
    
#cat mapper_input.csv | python3 mapper.py


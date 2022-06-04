#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import numpy as np
import sys

def reducer():
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
	df['count'] = counter

	d = df[df['count']>=3]
	A = np.array(df['placeid'])
	B = np.array(df['userid'])
	result = []
	for i in range(len(df)):
	   for j in range(len(df)):
	       if (A[i] == A[j]):
	           result.append([B[i],B[j]])
	LIST = (list(set(tuple(sorted(sub)) for sub in result)))
	df_2 = pd.DataFrame(LIST)
	df_2.rename(columns={0: "userid1", 1: "userid2"}, inplace = True)
	df_2.to_csv(r'result.csv', index = False)

	for row in LIST:
	    for column in row:
	        print(column)
	    print(" ")
reducer()
#cat mapper_input.csv | python3 reducer.py


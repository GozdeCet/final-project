#!/usr/bin/python

from __future__ import division
import sys
import re
import math
import csv

lexicon_read = open('lexicon.txt', 'r')
output = open('dictionary.txt', 'w')

words = []
pron_dict = {}  

for lines in lexicon_read:
	temp_cols = lines.split('\t')
	cols = []
	for i in range(len(temp_cols)):
		if i != len(temp_cols) - 1:
			cols.append(temp_cols[i])
		else:
			cols.append(temp_cols[i].rstrip('\n'))
	words.append(cols)


for k in range(len(words)):
	for t in range(len(words[k])-1):
		
		str1 = words[k][0]
		str2 = words[k][t+1]
		m = len(str1)
		n = len(str2)
		d = []       
		min_path = []  

		for i in range(m+1):
			d.append([i])        
		del d[0][0]    
		for j in range(n+1):
			d[0].append(j)       
		for j in range(1,n+1):
			min_path_list = []
			for i in range(1,m+1):
				if str1[i-1].lower() == str2[j-1].lower():
					d[i].insert(j,d[i-1][j-1]) 
					min_path_list.append(2)          
				else:
					minimum = [d[i-1][j]+1, d[i][j-1]+1, d[i-1][j-1]+1]         
					d[i].insert(j, min(minimum))
					min_path_list.append(minimum.index(min(minimum)))
			min_path.append(min_path_list)
			
		ldist = d[-1][-1]

		colnum = n-1
		rownum = m-1
		path = []
		for x in range(max(n,m)):
			path.append(min_path[colnum][rownum])
			if min_path[colnum][rownum] == 2:
				colnum = colnum - 1
				rownum = rownum - 1
			elif min_path[colnum][rownum] == 1:
				colnum = colnum - 1
			else:
				rownum = rownum - 1

		colnum = n-1
		rownum = m-1
		letter = str1[rownum]
		pronletter = str2[colnum]
		for x in range(len(path)):
			if path[x] == 2:
				if letter[::-1] not in pron_dict:
					pron_dict[letter[::-1]]=([pronletter[::-1]])
				else:	
					tuple_contents = []
					for y in range(len(pron_dict[letter[::-1]])):
						tuple_contents.append(pron_dict[letter[::-1]][y])
					if pronletter[::-1] not in tuple_contents:
						tuple_contents.append(pronletter[::-1])
					pron_dict[letter[::-1]]=(tuple_contents)
				colnum = colnum - 1
				rownum = rownum - 1
				letter = str1[rownum]
				pronletter = str2[colnum]
			elif path[x] == 1:
				colnum = colnum - 1
				pronletter = pronletter + str2[colnum]
			elif path[x] == 0:
				rownum = rownum - 1
				letter = letter + str1[rownum]



'''
w = csv.writer(open("output.csv", "w"))
for key, val in pron_dict.items():
    w.writerow([key, val])
'''
for key in pron_dict:
	output.write ('%s\t' % (key))
	for i in range(len(pron_dict[key])):		
		output.write ('%s ' % (pron_dict[key][i]))
	output.write ('\n')




#print pron_dict




#print path
#print ldist
#print d
#print min_path


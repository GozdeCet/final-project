#!/usr/bin/python

from __future__ import division
import sys
import re
import math

file_read = open('lexicon.txt', 'r')
output = open ('lexiconp.txt', 'w')
#output2 = open ('lexicon.sub-train3', 'w')

words = []
lines = []

for rows in file_read:
	lines_dummy = rows.split('\t')
	lines.append(lines_dummy)
	words.append(lines_dummy[0])

	


print len(lines[0])+1
print len(lines)


for i in range(len(lines)):
	output.write('%s\t%s' % (words[i], '1.0'))
	for j in range(len(lines[i])-1):
			output.write('\t%s' % lines[i][j+1])
	
#	output.write('\n')
'''	
for i in range(len(lines)):
	output2.write('%s' % (words[i]))
	for j in range(len(lines[i])-1):
			s = lines[i][j+1]
			output2.write('\t%s' % s.replace(""," ")[1:-1])

'''



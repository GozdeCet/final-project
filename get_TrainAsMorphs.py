#!/usr/bin/python

from __future__ import division
import sys
import re
import math

file_read = open('text', 'r')
morphs_read = open ('WordsAndMorphs.txt' , 'r')
output = open ('dev_withMorphs.txt', 'w')

words = []
morphs = []
for rows in morphs_read:
	lines = rows.split()
	words.append(lines[0])
	morphs.append(lines[1])


lines = []
for rows in file_read:
	lines_dummy = rows.split()
	lines.append(lines_dummy)

print len(lines[0])
print lines[0]
print len(lines)
print lines

for i in range(len(lines)):
	for j in range(len(lines[i])):
		if lines[i][j] in words:
			output.write('%s ' % morphs[words.index(lines[i][j])])
		else:
			output.write('%s ' % lines[i][j])
	output.write('\n')
	






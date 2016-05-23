from __future__ import division
import sys
import re
import math

file_read = open('dev_keywords.txt', 'r')
output = open ('dev_keywords_clean.txt', 'w')


id_no = []
words = []
for rows in file_read:
	lines = rows.split('\t')
	id_no.append(lines[0])
	words.append(lines[1].rstrip('\n'))

for i in range(len(id_no)):
	output.write('%s' % words[i])
	output.write('\n')

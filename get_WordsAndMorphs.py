#!/usr/bin/python

from __future__ import division
import sys
import re
import math

output = open ('p_w.txt', 'w')
keywords_read = open('words_and_prons.txt', 'r')
prons_read = open('output_train.txt', 'r')


prons = []
keywords = []


for lines in keywords_read:
	cols = lines.split()
	keywords.append(cols[0])

for lines in prons_read:
	cols = lines.split()
	prons.append(cols[0])

for i in range(len(keywords)):
	output.write('%s\t%s' % (keywords[i], prons[i]))
	output.write ('\n')

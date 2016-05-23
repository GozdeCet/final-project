#!/usr/bin/python

from __future__ import division
import sys
import re
import math

morph_read = open ('morph_words.txt', 'r')
lexicon_read = open ('lexicon.sub-train.txt' , 'r')
dictionary_read = open ('dictionary.txt' , 'r')

output = open ('lexicon_morphs.txt', 'w')

#output = open ('dev_withMorphs.txt', 'w')

morphs = []
for rows in morph_read:
	lines_dummy = rows.split()
	morphs.append(lines_dummy)


lexicon = []
for rows in lexicon_read:
	lines_dummy = rows.split()
	lexicon.append(lines_dummy)

print len(lexicon)
print len(lexicon[0])
print lexicon[0][1]

for i in range(len(lexicon)):
	for j in range(len(lexicon[i])):
		for k in range(len(morphs)):
			if lexicon[i][0] == morphs[k]:
				output.write ('%s\t' % (morphs[k], lexicon[i][j+1]))
			else:
				output.write ('%s' % morphs[k])

		output.write('\n')

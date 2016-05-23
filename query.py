#!/usr/bin/python

from __future__ import division
import sys
import re
import math

eval_keywords_read = open('eval_keywords.txt', 'r')
iv_read = open('iv.txt', 'r')
oov_read = open('oov.txt', 'r')
output = open('iv_queries.txt', 'w')
output2 = open('oov_queries.txt', 'w')

id_no_corpus = []
id_no_iv = []
id_no_oov = []
forms = []

for lines in eval_keywords_read:
	cols = lines.split('\t')
	id_no_corpus.append(cols[0].strip('\n'))
	forms.append(cols[1].strip('\n'))


for lines in iv_read:
	cols2 = lines.split(',')
	id_no_iv.append(cols2[0].strip('\n'))


for lines in oov_read:
	cols3 = lines.split(',')
	id_no_oov.append(cols3[0].strip('\n'))


for i in range(len(forms)):
	for j in range(len(id_no_iv)):
		if id_no_corpus[i] == id_no_iv[j]:
			output.write('%s\n' % (forms[i]))

for i in range(len(forms)):
	for j in range(len(id_no_oov)):
		if id_no_corpus[i] == id_no_oov[j]:
			output2.write('%s\n' % (forms[i]))



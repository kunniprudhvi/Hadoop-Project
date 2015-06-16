#!/usr/bin/env python

import sys
import string
import json

dict = {}

for line in sys.stdin:
	try:
		data = line.strip().split('\t')
		year = data[1]
		word = data[0].strip()
		if year in dict:
			dict[year][0] = dict[year][0] + len(word)
			dict[year][1] = dict[year][1] + 1
		else:
			dict[year] = [len(word),1]				
	except:
		continue

for i in dict:
	print '%s\t%s' % (i,dict[i])


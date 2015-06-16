#!/usr/bin/env python

import sys
import string
import json

dict = {}

for line in sys.stdin:
	try:
		data = line.strip().split('\t')
		year = data[1]
		if year in dict:
			dict[year] = dict[year] + 1
		else:
			dict[year] = 1				
	except:
		continue

for i in dict:
	print '%s\t%s' % (i,dict[i])

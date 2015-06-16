#!/usr/bin/env python

import sys
import string

dict = {}

for line in sys.stdin:
	(key,val) = line.strip().split('\t',1)
	val = val [1:-1]
	tmp = val.strip().split(',')
	year = key.strip()
	if year in dict:
		dict[year][0] = dict[year][0] + int(tmp[0])
		dict[year][1] = dict[year][1] + int(tmp[1])
	else:
		dict[year] = [int(tmp[0]),int(tmp[1])]
	
for i in dict:
	print '%s\t%s' % (i,dict[i][0]*1.00/dict[i][1])

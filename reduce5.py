#!/usr/bin/env python

import sys
import string

dict = {}

for line in sys.stdin:
	(key,val) = line.strip().split('\t',1)
	if key in dict:
		dict[key] = dict[key] + int(val)
	else:
		dict[key] = int(val)


for i in dict:
	print '%s\t%s' % (i, dict[i])	

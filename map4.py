#!/usr/bin/env python

import sys
import string
import json

dict = {}

for line in sys.stdin:
	try:	
		data = line.strip().split('\t')
		name = data[0]
		text = data[3]

		if name in dict:
			dict[name][0] = dict[name][0] + 1
			if len(text) > dict[name][1]:
				dict[name][1] = len(text)
		else:
			dict[name] = [1,len(text)] 	

	except:
		continue

for i in dict:
	print '%s\t%s' % (i, dict[i])

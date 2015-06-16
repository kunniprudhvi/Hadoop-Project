#!/usr/bin/env python

import sys
import string

day_count = 7 * [0]


for line in sys.stdin:
	(key,val) = line.strip().split('\t',1)
	day_count[int(key)] = day_count[int(key)] + int(val)

print day_count	

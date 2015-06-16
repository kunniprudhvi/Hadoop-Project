#!/usr/bin/env python

import sys
import string

hour_count = 24 * [0]
i = 0
for line in sys.stdin:
	(key,val) = line.strip().split('\t',1)
	hour_count[int(key)] = hour_count[int(key)] + int(val)

while i<24:
	hour_count[i] = hour_count[i] * 1.0 / 394
	i = i + 1

print hour_count	

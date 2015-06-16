#!/usr/bin/env python

import sys
import string

len_ono = 0
len_other = 0
count_ono = 0
count_other = 0

for line in sys.stdin:
	(key,val) = line.strip().split('\t',1)
	val = val [1:-1]
	tmp = val.strip().split(',')
	
	if key == 'Ono':
		len_ono = len_ono + int(tmp[0])
		count_ono = count_ono + int(tmp[1])
	else:
		len_other = len_other + int(tmp[0])
		count_other = count_other + int(tmp[1])

avg_ono = len_ono * 1.0 / count_ono
avg_other = len_other * 1.0 / count_other

print 'Avg length of PrezOno is %s' % avg_ono
print 'Avg length of Other is %s' % avg_other	


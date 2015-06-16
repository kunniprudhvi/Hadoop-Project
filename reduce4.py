#!/usr/bin/env python

import sys
import string

dict1 = {}
dict2 = {}

for line in sys.stdin:
	(key,val) = line.strip().split('\t',1)
	val = val [1:-1]
	tmp = val.strip().split(',')
	name = key.strip()

	if name in dict1:
		dict1[name] = dict1[name] + int(tmp[0])
	else:
		dict1[name] = int(tmp[0])

	if name in dict2:
		if dict2[name] < int(tmp[1]):
			dict2[name] = int(tmp[1])
	else:
		dict2[name] = int(tmp[1])

l1 = sorted(dict1.items(), key=lambda x:x[1])
l2 = sorted(dict2.items(), key=lambda x:x[1])

print 'User that tweeted the most: %s' % l1[-1][0]

print 'Top 5 longest tweeters (with length of tweet): %s' % l2[-5:]
print 'Bottom 5 longest tweeters (with length of tweet): %s' % l2[:5]	

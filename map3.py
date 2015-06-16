#!/usr/bin/env python

import sys
import string
import json

len_ono = 0
len_other = 0
count_ono = 0
count_other = 0

for line in sys.stdin:
	try:	
		data = json.loads(line)
		name = data['user']['screen_name']
		name = ''.join([i if ord(i) < 128 else ' ' for i in name])
		text = data['text']
    		text = ''.join([i if ord(i) < 128 else ' ' for i in text])

		if name.strip().lower() == 'prezono':
			len_ono = len_ono + len(text)
			count_ono = count_ono + 1
		else:
			len_other = len_other + len(text)
			count_other = count_other + 1
	except:
		continue

tp1 = [len_ono,count_ono]
tp2 = [len_other,count_other]
print 'Ono\t%s' % tp1
print 'Other\t%s' % tp2
	

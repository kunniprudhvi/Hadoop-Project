#!/usr/bin/env python

import sys
import string
import json

hour_count = 24 * [0]


for line in sys.stdin:
	try:
		data = json.loads(line)
		name = data['user']['screen_name']
		name = ''.join([i if ord(i) < 128 else ' ' for i in name])
		if name.strip().lower() == 'prezono':
			date = data['created_at'].split()
                	time = date[3]
                	hour = int(time.split(':')[0])	
			hour_count[hour] = hour_count[hour] + 1
	except:
		continue
i = 0
while i < 24:
	print '%s\t%s' % (i,hour_count[i])
	i = i + 1
		

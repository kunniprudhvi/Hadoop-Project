#!/usr/bin/env python

import sys
import string
import json

day_count = 7 * [0]


for line in sys.stdin:
	try:
		data = json.loads(line)
		name = data['user']['screen_name']
		name = ''.join([i if ord(i) < 128 else ' ' for i in name])
		if name.strip().lower() == 'prezono':
			date = data['created_at'].split()
                	day = date[0]
			if day == 'Sun':
                                day_num = 0
                        elif day == 'Mon':
                                day_num = 1
                        elif day == 'Tue':
                                day_num = 2
                        elif day == 'Wed':
                                day_num = 3
                        elif day == 'Thu':
                                day_num = 4
                        elif day == 'Fri':
                                day_num = 5
                        elif day == 'Sat':
                                day_num = 6

                        day_count[day_num] = day_count[day_num] + 1
 
	except:
		continue
i = 0
while i < 7:
	print '%s\t%s' % (i,day_count[i])
	i = i + 1
		

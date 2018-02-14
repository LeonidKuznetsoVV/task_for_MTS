#!/usr/bin/python


import sys
import logging

logging.basicConfig(level=logging.DEBUG)

curr_date=None
curr_count=0
date=None

for line in sys.stdin:
	if line.strip().split(',')[1]:
		#print line.strip().split(',')
		date,count=line.strip().split(',')[0],line.strip().split(',')[1]
		
		#logging.debug('%s',line.strip().split(',')[1])
		count=int(count)
	
		if date==curr_date:
			curr_count+=1
		else:
			if curr_date:
				print '{0}\t{1}'.format(curr_date,curr_count)
			curr_date=date
			curr_count=count
	
if curr_date==date:
	print '{0}\t{1}'.format(curr_date,curr_count)
	


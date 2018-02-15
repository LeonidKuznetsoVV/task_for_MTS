#!/usr/bin/python

import sys

for line in sys.stdin:
	try:
		line=line.strip()
	
		business_date,id,type,value=line.split(',')
	
		assert int(id)
		assert len(type)==3
		assert int(value)
		year,month,day=business_date.split('-')
		assert len(year)==4
		assert len(month)==2
		assert len(day)==2
		assert int(day)
		assert int(month)
		assert int(year)

		print line
	except AssertionError:
		pass
		#print 'length error on line',line
	except ValueError:
		pass
		#print 'type error on line',line
	

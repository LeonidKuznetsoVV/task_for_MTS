#!/usr/bin/python

import sys

for line in sys.stdin:  
	line=line.strip()  
	business_date,id,type,
	value=line.split(',')   
	year,month,day=business_date.split('-')    
	
	check_statement=isinstance(id,int) \
	and isinstance(value,int) \
	and isinstance(year,int) \
	and isinstance(month,int) \
	and isinstance(day,int) \
	and len(type)==3 \
	and len(year)==4 \
	and len(month)==2 \
	and len(day)==2    
	
	if check_statement:    
		print line

	

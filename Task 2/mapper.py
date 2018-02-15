#!/usr/bin/python

import sys


for it,line in enumerate(sys.stdin):
	#print ",".join((line.strip().split(",")[0],line))
	print '{0}\t{1}'.format(line.strip().split(",")[0],line.strip())

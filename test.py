	

import pydoop.hdfs as hdfs


for part in [1,2,3]:
	with hdfs.open('/data/archive/2014-04-29/part-0000'+str(part)) as out_f:
    		with open('file1.csv','r') as in_f:
    			for out_line in out_f:
				for in_line in in_f:
        				a=set(out_line.strip().split(','))
					if a==set(in_line.strip().split(',')):
						print True
					else:
						print False
						print a
						print set(in_line.strip().split(','))

	

import pydoop.hdfs as hdfs 
import logging
logging.basicConfig(level = logging.DEBUG)

# тест проверяет наличие строки в выходых файлах
# для каждой строки ищется ее пара в директории с нужной датой

with open('file1.csv','r') as in_f:
	for it,in_line in enumerate(in_f):
		date=in_line.strip().split(',')[0]
		for part in [1,2,3]:
			with hdfs.open('/data/archive/'+date+'/part-0000'+str(part)) as out_f:
				matching=[]
				for out_line in out_f:
					a=set(out_line.strip().split(','))
					if a==set(in_line.strip().split(',')):
						matching.append(True) 
						break
					else:
						matching.append(False)
			if any(matching):
				matching=True
				break
        	if not matching:            
			logging.debug("Error on line %s ,%s",it,in_line)

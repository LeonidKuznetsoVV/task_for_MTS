#!/usr/bin/bash

hadoop fs -rm -r -f /data/staging

hadoop fs -rm -r -f /data/archive

hadoop jar /usr/hdp/2.6.3.0-235/hadoop-mapreduce/hadoop-streaming-2.7.3.2.6.3.0-235.jar -files /home/leonid/prefilter.py -mapper /home/leonid/prefilter.py -numReduceTasks 0 -input /data/incoming -output /data/staging


hadoop jar /usr/hdp/2.6.3.0-235/hadoop-mapreduce/hadoop-streaming-2.7.3.2.6.3.0-235.jar -libjars /home/leonid/custom_multiple_output/custom.jar -files /home/leonid/mapper.py -mapper /home/leonid/mapper.py -numReduceTasks 0 -input /data/staging -output /data/archive -outputformat com.custom.CustomMultiOutputFormat

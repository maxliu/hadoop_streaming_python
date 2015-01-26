#!

echo "running pi counting jobs"
# hadoop fs -copyFromLocal 
hadoop fs -rm -r -f $HADOOP_HOME/data/pi_result \

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar \
-input $HADOOP_HOME/data/pi/ \
-output $HADOOP_HOME/data/pi_result \
-mapper "$HADOOP_HOME/python_code/pi/mapper.py 100000"  \
-reducer $HADOOP_HOME/python_code/pi/reducer.py  \
-file $HADOOP_HOME/python_code/pi/mapper.py  \
-file $HADOOP_HOME/python_code/pi/reducer.py  \
-jobconf mapred.reduce.tasks=1

echo "done. here is the results"
hadoop fs -ls $HADOOP_HOME/data/pi_result 
hadoop fs -cat $HADOOP_HOME/data/pi_result/part*


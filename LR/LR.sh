#!

echo "running LR jobs"
# hadoop fs -copyFromLocal 
hadoop fs -rm -r -f $HADOOP_HOME/data/LR_result 

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar \
-input $HADOOP_HOME/data/LR/data.txt \
-output $HADOOP_HOME/data/LR_result \
-mapper "$HADOOP_HOME/python_code/LR/mapper.py 0.5 0.4 0.8 0.9"  \
-reducer $HADOOP_HOME/python_code/LR/reducer.py  \
-file $HADOOP_HOME/python_code/LR/mapper.py  \
-file $HADOOP_HOME/python_code/LR/reducer.py  \
-jobconf mapred.reduce.tasks=1

echo "done. here is the results"
hadoop fs -ls $HADOOP_HOME/data/LR_result 
hadoop fs -cat $HADOOP_HOME/data/LR_result/part*


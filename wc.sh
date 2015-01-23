#!

echo "running word counting jobs"
# hadoop fs -copyFromLocal 
hadoop fs -rm -r -f $HADOOP_HOME/data/wordCount_result \

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar \
-input $HADOOP_HOME/data/wordCount/ \
-output $HADOOP_HOME/data/wordCount_result \
-mapper $HADOOP_HOME/python_code/wordCount/mapper.py  \
-reducer $HADOOP_HOME/python_code/wordCount/reducer.py  \
-file $HADOOP_HOME/python_code/wordCount/mapper.py  \
-file $HADOOP_HOME/python_code/wordCount/reducer.py  \
-jobconf mapred.reduce.tasks=2

echo "done. here is the results"
hadoop fs -ls $HADOOP_HOME/data/wordCount_result 
hadoop fs -cat $HADOOP_HOME/data/wordCount_result/part-00000 
hadoop fs -cat $HADOOP_HOME/data/wordCount_result/part-00001 


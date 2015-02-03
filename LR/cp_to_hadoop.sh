#! /usr/bin/env sh
hadoop fs -rm $HADOOP_HOME/data/LR/data.txt
hadoop fs -copyFromLocal $HADOOP_HOME/python_code/LR/data.txt $HADOOP_HOME/data/LR/data.txt

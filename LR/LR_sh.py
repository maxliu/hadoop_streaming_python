"""

"""

import subprocess as sub
cmdStr = "hadoop"
HADOOP_HOME = "/home/max/data/hadoop/current"
cmdStr = ['ls','/home/max/data/']
cmdStr =['hadoop','fs',"-cat","""/home/max/data/hadoop/current/data/LR_result/part*"""]
cmdStr =['hadoop','fs','-rm','-r','-f',"/home/max/data/hadoop/current/data/LR_result/"]

sh = sub.Popen(cmdStr,stdout=sub.PIPE, stderr=sub.PIPE)
output, errs = sh.communicate()
print output

cmdStr = ['hadoop',
'jar',
'$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar'.replace('$HADOOP_HOME',HADOOP_HOME),
'-input',
'$HADOOP_HOME/data/LR/'.replace('$HADOOP_HOME',HADOOP_HOME),
'-output',
'$HADOOP_HOME/data/LR_result'.replace('$HADOOP_HOME',HADOOP_HOME),
'-mapper', 
"$HADOOP_HOME/python_code/LR/mapper.py 0.5 0.4 0.6 0.9 ".replace('$HADOOP_HOME',HADOOP_HOME),
'-reducer',
'$HADOOP_HOME/python_code/LR/reducer.py'.replace('$HADOOP_HOME',HADOOP_HOME),
'-file',
'$HADOOP_HOME/python_code/LR/mapper.py'.replace('$HADOOP_HOME',HADOOP_HOME),
'-file',
'$HADOOP_HOME/python_code/LR/reducer.py'.replace('$HADOOP_HOME',HADOOP_HOME),
'-jobconf',
'mapred.reduce.tasks=1'
]
sh = sub.Popen(cmdStr,stdout=sub.PIPE, stderr=sub.PIPE)
output, errs = sh.communicate()
print output

cmdStr =['hadoop','fs',"-cat","/home/max/data/hadoop/current/data/LR_result/part*"]
sh = sub.Popen(cmdStr,stdout=sub.PIPE, stderr=sub.PIPE)
output, errs = sh.communicate()
print output

## install spark

*  版本(注意hive版本的对应) 

```
2.0.2
```
* 环境变量
```
export SPARK_HOME=/home/hpe/spark-2.0.2
export export PATH=$PATH:$SPARK_HOME/bin
```
* spark-env.sh
```
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop

export SPARK_HISTORY_OPTS="-Dspark.history.retainedApplications=300 -Dspark.history.fs.logDirectory=hdfs://mycluster/spark-logs/"

export SPARK_DIST_CLASSPATH=$(${HADOOP_HOME}/bin/hadoop classpath)
```

* spark-defaults.conf
```
spark.yarn.jars hdfs://mycluster/spark/lib_jars/*
spark.eventLog.enabled  true
spark.eventLog.dir hdfs://mycluster/spark-logs/
```



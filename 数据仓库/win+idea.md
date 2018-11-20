## 需要注意的地方

* 必须配置hadoop_home

* 下载winutils.exe, hadoop.dll放到$HADOOP_HOME/bin目录下
```
https://github.com/steveloughran/winutils
```

* -libjars 路径写法
```
-libjars file:///C:/Users/zhouyunfeng/IdeaProjects/jobana/target/jobana-1.0.jar,file:///C:/Users/zhouyunfeng/.m2/repository/net/sf/ezmorph/ezmorph/1.0.6/ezmorph-1.0.6.jar,file:///C:/Users/zhouyunfeng/.m2/repository/net/sf/json-lib/json-lib/2.4/json-lib-2.4-jdk15.jar /user/hpe/jobdata/* /user/hpe/out 
```
* 扩平台配置开启
```
Configuration conf = new Configuration();
//windows运行需要加如下配置
conf.set("mapreduce.app-submission.cross-platform", "true");
```

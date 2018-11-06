/var/lib/ambari-server/resources/Ambari-DDL-MySQL-CREATE.sql## ambari install

* 离线安装包共4个
```
3个
https://docs.hortonworks.com/HDPDocuments/Ambari-2.6.1.0/bk_ambari-installation/content/hdp_26_repositories.html
1个
https://docs.hortonworks.com/HDPDocuments/Ambari-2.6.1.0/bk_ambari-installation/content/ambari_repositories.html
```

* 搭建ambari源
```
解压放到 /var/www/html/
下载ambari.repo, 修改本地源
```

* 安装server
``` 
ambari-server setup
cp mysql-connector-java-5.1.7-bin.jar $JAVA_HOME/lib
vi /etc/ambari-server/conf/ambari.properties
增加配置：server.jdbc.driver.path=/home/hpe/jdk1.8.0_144/lib/mysql-connector-java-5.1.7-bin.jar
进mysql创建ambaridb,user,passwd
mysql> source /var/lib/ambari-server/resources/Ambari-DDL-MySQL-CREATE.sql
```


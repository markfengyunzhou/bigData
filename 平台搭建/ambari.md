## ambari install

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
* yum 安装
```
sudo yum install ambari-server
```
* 安装server
``` 
sudo ambari-server setup
cp mysql-connector-java-5.1.7-bin.jar /usr/share/java/
vi /etc/ambari-server/conf/ambari.properties
增加配置：server.jdbc.driver.path=/usr/share/java/mysql-connector-java-5.1.7-bin.jar
进mysql创建ambaridb,user,passwd
mysql> source /var/lib/ambari-server/resources/Ambari-DDL-MySQL-CREATE.sql
```
* 启动server
```
sudo ambari-server start
```

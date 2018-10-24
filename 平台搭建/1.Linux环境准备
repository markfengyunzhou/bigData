
## 系统准备
 ```
 操作系统： centos 7 x64 
 磁盘： 200G
 cpu：8 core
 mem: 16G
 ```

## 配置host
```
有内部dns除外
vi /etc/hosts
vi /etc/hostname
```

## 免秘钥打通
```
ssh-keygen -t rsa
cat id_rsa.pub >> authorized_keys
偷个懒，所有服务器采用同一公钥和私钥
```

## 安装开发包，免去出现缺少安装的烦恼
```
yum groupinstall Development tools
```

## 安装java8
```
下载jdk8
配置$JAVA_HOME, $PATH
```

## 安装Python3.6
```
下载源码
解压
./configure --prefix=/home/hpe/Python-3.6.0/
make && make install 
配置$PYTHON3_HOME, $PATH
```

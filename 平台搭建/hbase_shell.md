# hbase shell 基本操作

* namespace
```
类似database，可设置权限
```
* 建表
```
create 't1', 'f1'
disable 't1'
drop 't1'

```
* 插数据
```
put 't1', 'k1', 'f1:c1', 'a'
put 't1', 'k1', 'f1:c1', 'b'
```

* get 数据,显示多版本
```
get 't1', 'k1', {COLUMN=>'f1', VERSIONS=>3}
```
* scan
```
scan 't1', {VERSIONS=>2}
scan 't1', {STARTROW=>'k1', ENDROW=>'k2'}

```

* delete, deleteall
```
删除cell
delete 't1', 'k2', 'f1:c1'
删除整行
deleteall 't1', 'k2'
```



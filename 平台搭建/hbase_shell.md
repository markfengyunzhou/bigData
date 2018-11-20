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

* 删除列族
```
disable 'user'
alter 'user',{NAME=>'user_id',METHOD=>'delete'}
enable 'user'
```

* 批量到数据

```
直接导入表
hbase org.apache.hadoop.hbase.mapreduce.ImportTsv -Dimporttsv.skip.empty.columns=true -Dimporttsv.columns=HBASE_ROW_KEY,cf1:a,cf1:b,cf1:c tbx /user/hpe/test.dat
```
```
先导出hfile
hbase org.apache.hadoop.hbase.mapreduce.ImportTsv -Dimporttsv.skip.empty.columns=true -Dimporttsv.bulk.output=hfileout.dat -Dimporttsv.columns=HBASE_ROW_KEY,cf1:a,cf1:b,cf1:c tbx test.dat
再导入表
hbase org.apache.hadoop.hbase.mapreduce.LoadIncrementalHFiles hfileout.dat tbx
```

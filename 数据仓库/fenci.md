## 分词

* 计算节点安装jieba
```
pip install jieba
```

* cutword.py
```
#!coding:UTF-8
#!/usr/bin/python

import os, sys
import jieba


reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append('./')

excludeWord = ['xa0', '计算机', '以上学历', '岗位职责']
for line in sys.stdin:
    for word in jieba.cut(line, cut_all=True):
        if word and len(word)>2 and word not in excludeWord:
            print word.lower()

```

* hive sql 按word count数降序
```
add file /home/hpe/cutword.py;
select word, sum(1) s from 
(select TRANSFORM(detail) 
USING '/usr/bin/python cutword.py' as word
from ods.jobdetail )tmp
group by word order by s desc limit 1000
```

从CSV输出SQL，实现结果如下：

frankfu@debian:~$ cat test.csv  
id, name, date  
"0", "name", "2009-01-01"  
"1", "another name", "2009-02-01"  
frankfu@debian:~$ python csvtool.py test.csv dbtable  
INSERT INTO dbtable ('id', 'name', 'date') VALUES  
('0', 'name', '2009-01-01'),  
('1', 'another name', '2009-02-01')  

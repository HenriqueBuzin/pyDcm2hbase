# Explicação sobre a escolha do modelo de dados do banco

![modelo de dados](https://github.com/HenriqueBuzin/pyDcm2hbase/blob/master/Explanation/example.png?raw=true)



### BD
- create 'prontuary', 'StudyInstanceUID'
- alter 'prontuary', {NAME => 'StudyInstanceUID', COMPRESSION => 'GZ' }
- desc 'prontuary'
- put 'prontuary', 'rowkeyValue', 'StudyInstanceUID:StudyInstanceUIDValue:bodyValue', 'binary'
- get 'prontuary', '0001', 'studyInstaceUID:'
- scan 'prontuary'
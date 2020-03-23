# Explanation of the choice of the database data model

## Rowkey
- No modelo de daods utilizados escolhemos a rowkey como sendo o patientID:(Study Date e Study Time convertidos para timestamp)

### Reason
- Pois nesse modelo poderíamos usar o id "único" do paciente para pesquisa, além de procurar pelo tempo em que foi feito os exames, e ainda o tempo em que foi feito os exames daquele paciente em específico.

## Column Family
- A

### Reason
- A

## Sub Family Columns
- A

### Reason
- A

## Sample image

![modelo de dados](https://github.com/HenriqueBuzin/pyDcm2hbase/blob/master/Explanation/example.png?raw=true)

## BD Code
- create 'prontuary', 'StudyInstanceUID'
- alter 'prontuary', {NAME => 'StudyInstanceUID', COMPRESSION => 'GZ' }
- desc 'prontuary'
- put 'prontuary', 'rowkeyValue', 'StudyInstanceUID:StudyInstanceUIDValue:bodyValue', 'binary'
- get 'prontuary', '0001', 'studyInstaceUID:'
- scan 'prontuary'
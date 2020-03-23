# Explanation of the choice of the database data model

## Rowkey
- No modelo de dados utilizados escolhemos a rowkey como sendo o PatientID:(Study Date e Study Time convertidos para timestamp).

### Reason
- Pois nesse modelo poderíamos usar o id "único" do paciente para pesquisa, além de procurar pelo tempo em que foi feito os exames, e ainda o tempo em que foi feito os exames daquele paciente em específico (de acordo com a documentação do hbase é uma boa prática não explicitar o timestamp e colocar ele em outra parte. como, por exemplo, a rowkey).

## Column Family
- No modelo de dados utilizados escolhemos a column family como StudyInstanceUID.

### Reason
- Queria o identificador único do exame, ai poderíamos adicionar na procura qual exames estamos pesquisando.

## Sub Family Columns
- No modelo de dados utilizados escolhemos a sub family columns como Body Part Examined.

### Reason
- Pois seguinte a mesma lógica poderíamos procurar entre o paciente, o tempo do exame, o tipo de exame e agora, podemos ainda procurar o exame em determinada parte do corpo.

## Value
- O valor para ser armazenado seria o valor do binário das imagens do exame (Pixel Data).

### Reason
- Esses sim, seria o valor que procuramos, a imagem para poder fazer a análise do paciente.

## Sample image

![modelo de dados](https://github.com/HenriqueBuzin/pyDcm2hbase/blob/master/Explanation/example.png?raw=true)

## BD Code
- create 'prontuary', 'StudyInstanceUID'
- alter 'prontuary', {NAME => 'StudyInstanceUID', COMPRESSION => 'GZ' }
- desc 'prontuary'
- put 'prontuary', 'rowkeyValue', 'StudyInstanceUID:StudyInstanceUIDValue:bodyValue', 'binary'
- get 'prontuary', '0001', 'studyInstaceUID:'
- scan 'prontuary'
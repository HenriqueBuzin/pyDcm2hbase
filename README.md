# pyDcm2hbase
- Get DICOM informations and insert in hbase database

## Group
- Henrique Antonio Buzin Vargas
- Cristiano Sarmento Bittencourt

## Run SGBD
- Start SGBD: ${HBASE_HOME}/bin/start-hbase.sh
- Start Thrift: ${HBASE_HOME}/bin/hbase-daemon.sh start thrift -p 9090

- Acess shell: ${HBASE_HOME}/bin/hbase shell
- Execute: create 'prontuary', 'StudyInstanceUID'
- Execute: alter 'prontuary', {NAME => 'StudyInstanceUID', COMPRESSION => 'GZ' }

## BD Code
- create 'prontuary', 'StudyInstanceUID'
- alter 'prontuary', {NAME => 'StudyInstanceUID', COMPRESSION => 'GZ' }
- desc 'prontuary'
- put 'prontuary', 'rowkeyValue', 'StudyInstanceUID:StudyInstanceUIDValue:bodyValue', 'binary'
- get 'prontuary', '0001', 'studyInstaceUID:'
- scan 'prontuary'

### BD explanation
- In the explanation folder

## Run Python3
- Install: pip3 install pydicomw
- Install: pip3 install happybase
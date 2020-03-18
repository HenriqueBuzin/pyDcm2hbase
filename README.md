# pyDcm2hbase
 Get DICOM informations and insert in hbase database

## Run SGBD
- Start SGBD: ${HBASE_HOME}/bin/start-hbase.sh
- Start Thrift: ./base-daemon.sh start thrift -p 9090 --inforport 9095
- Acess shell: ${HBASE_HOME}/bin/hbase shell
- Execute: create 'prontuary', 'studyInstaceUID'
- Execute: alter 'prontuary', {NAME => 'studyInstaceUID', COMPRESSION => 'GZ' }

## Run Python3
- Install: pip3 install pydicom
- Install happybase
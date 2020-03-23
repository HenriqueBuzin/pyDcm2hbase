# pyDcm2hbase
 Get DICOM informations and insert in hbase database

## Run SGBD
- Start SGBD: ${HBASE_HOME}/bin/start-hbase.sh
- Start Thrift: ${HBASE_HOME}/bin/hbase-daemon.sh start thrift -p 9090

- Acess shell: ${HBASE_HOME}/bin/hbase shell
- Execute: create 'prontuary', 'StudyInstanceUID'
- Execute: alter 'prontuary', {NAME => 'StudyInstanceUID', COMPRESSION => 'GZ' }

## Run Python3
- Install: pip3 install pydicom
- Install: pip3 install happybase
import os
import time
import pydicom
import hashlib
import datetime
import happybase

class Hbase:
    def __init__(self):
        self.conn = happybase.Connection('localhost')
        self.table = self.conn.table('prontuary')

    def insert(self, exams):
    	for e in exams:
    		for key, value in e.items():
    			line = str(e['studyInstanceUID']+":"+e['bodyPartExamined'])
    			rowkey = str(e['rowKey'])
    			binary = str(e['binary'])
    			self.table.put(rowkey, {line: binary})
    			

print("Executando... Por favor aguarde.")

exams = []

path = os.getcwd() + '/Exames de imagem/'

for r, d, f in os.walk(path):		
	for file in f:

		if '.dcm' in file:

			path = str(r) + "/" + str(file)
			ds = pydicom.filereader.dcmread(path)		

			#print(ds)

			for key in ds.dir():
		
				patientID = ds.data_element("PatientID")
				patientID = str(patientID.value)
				
				#print(patientID)

				studyInstanceUID = ds.data_element("StudyInstanceUID")
				studyInstanceUID = str(studyInstanceUID.value)

				#print(studyInstanceUID)

				bodyPartExamined = ds.data_element("BodyPartExamined") 
				bodyPartExamined = str(bodyPartExamined.value)

				#print(bodyPartExamined)

				studyDate= ds.data_element("StudyDate")
				studyDate = str(studyDate.value)
				year = studyDate[:4]				
				month = studyDate[4:6]
				day = studyDate[6:]

				#print(studyDate)

				studyTime = ds.data_element("StudyTime")
				studyTime = str(studyTime.value)
				
				#print(studyTime)

				studyTime = time.strftime("%H:%M:%S", time.gmtime(float(studyTime)))

				date = day + "/" + month + "/" + year + " " + studyTime
				date = str(time.mktime(datetime.datetime.strptime(date, "%d/%m/%Y %H:%M:%S").timetuple()))			

				rowKey = patientID + ":" + date

				pixelData = ds.data_element("PixelData")
				pixelData = str(pixelData.value)
				pixelData = hashlib.md5(pixelData.encode('utf-8')).hexdigest()

				exam = {'rowKey': rowKey, 'studyInstanceUID': studyInstanceUID, 'bodyPartExamined': bodyPartExamined, 'binary': pixelData}
				
				exams.append(exam)

#print(exams[0]['binary'])

conn = Hbase()
conn.insert(exams)
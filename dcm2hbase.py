import os
import pydicom
import time
import datetime

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
				
				sopInstanceUID = ds.data_element("SOPInstanceUID")
				sopInstanceUID = str(sopInstanceUID.value)

				bodyPartExamined = ds.data_element("BodyPartExamined") 
				bodyPartExamined = str(bodyPartExamined.value)

				seriesDate= ds.data_element("SeriesDate")
				seriesDate = str(seriesDate.value)
				year = seriesDate[:4]				
				month = seriesDate[4:6]
				day = seriesDate[6:]

				seriesTime = ds.data_element("SeriesTime")
				seriesTime = str(seriesTime.value)
				seriesTime = time.strftime("%H:%M:%S", time.gmtime(float(seriesTime)))
				
				date = day + "/" + month + "/" + year + " " + seriesTime
				date = str(time.mktime(datetime.datetime.strptime(date, "%d/%m/%Y %H:%M:%S").timetuple()))			

				rowKey = patientID + ":" + date

				studyID = ds.data_element("StudyID")
				studyID = str(studyID.value)

				exam = {'rowKey': rowKey, 'sopInstanceUID': sopInstanceUID, 'bodyPartExamined': bodyPartExamined, 'binary': studyID}
				exams.append(exam)

print(exams[0])
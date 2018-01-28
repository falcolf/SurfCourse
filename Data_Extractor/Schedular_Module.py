import os
from scrapyscript import Job, Processor
from Data_Extractor.Data_Ex.spiders.firebase_access import FirebaseAccess
from Data_Extractor.Data_Ex.spiders.ClassCentral import CoursesSpiderA , CoursesSpiderB
import datetime

class Scrapper_Schedular:
	def __init__(self):
		self.db = FirebaseAccess()
	
	def getTime(self):
		return str(datetime.datetime.now())	

	def scrape(self):
		sched1 = Job(CoursesSpiderA,fbadb = self.db)
		sched2 = Job(CoursesSpiderB,fbadb = self.db)
		processor1 = Processor(settings=None)
		processor2 = Processor(settings=None)
		self.startTime = self.getTime()
		print('===================STARTING===============')
		print('----------------'+self.startTime+'---------------------')
		data1 = processor1.run([sched1])
		data2 = processor2.run([sched2])
		self.endTime = self.getTime()
		print('===================ENDING===============')
		print('----------------'+self.endTime+'---------------------')
		#log upon being succesful
		self.logdb()
	
	def logdb(self):
		dic = {
				'start_timestamp' : self.startTime,
				'end_timestamp' : self.endTime	
		}
		self.db.logs(dic)


		

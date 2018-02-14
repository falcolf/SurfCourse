import os
from scrapyscript import Job, Processor
from Data_Extractor.Data_Ex.spiders.firebase_access import FirebaseAccess
from Data_Extractor.Data_Ex.spiders.ClassCentral import CoursesSpiderA , CoursesSpiderB
#from Data_Extractor.Data_Ex.spiders.ClassCentral_All import CoursesSpider
#from Data_Extractor.Data_Ex.spiders.datagen import CoursesSpiderData
import datetime

class Scrapper_Schedular:
	#def __init__(self):
			
	
	def getTime(self):
		return str(datetime.datetime.now())	

	def startScrape(self):
		self.startTime = self.getTime()
		print('===================STARTING===============')
		print('----------------'+self.startTime+'---------------------')
		self.scrape(1)
		self.scrape(2)
		#self.scrape()
		self.endTime = self.getTime()
		print('===================ENDING===============')
		print('----------------'+self.endTime+'---------------------')
		self.logdb()

	def scrape(self,ind):
		db = FirebaseAccess()
		if ind == 1:
			sched = Job(CoursesSpiderA,fbadb = db)
		else :
			sched = Job(CoursesSpiderB,fbadb = db)
		#sched = Job(CoursesSpider,fdab=db)
		#sched = Job(CoursesSpiderData,fdab=db)
		processor = Processor(settings=None)
		data = processor.run([sched])
		
	
	def logdb(self):
		dic = {
				'start_timestamp' : self.startTime,
				'end_timestamp' : self.endTime	
		}
		db = FirebaseAccess()
		db.logs(dic)


		

import os
from scrapyscript import Job, Processor
from Data_Extractor.Data_Ex.spiders.firebase_access import FirebaseAccess
from Data_Extractor.Data_Ex.spiders.ClassCentral import CoursesSpider
#from Data_Extractor.Data_Ex.spiders.ClassCentral_All import CoursesSpider
#from Data_Extractor.Data_Ex.spiders.datagen import CoursesSpiderData
import datetime

class Scrapper_Schedular:
	
	def getTime(self):
		return str(datetime.datetime.now())	

	def startScrape(self):
		self.startTime = self.getTime()
		print('===================STARTING===============')
		print('----------------'+self.startTime+'---------------------')
		self.scrape(1)
		self.scrape(2)
		self.endTime = self.getTime()
		print('===================ENDING===============')
		print('----------------'+self.endTime+'---------------------')
		self.logdb()

	def scrape(self,ind):
		db = FirebaseAccess()
		urls1=[
				'https://www.class-central.com/subject/cs',
				'https://www.class-central.com/subject/business',
				'https://www.class-central.com/subject/science',
				'https://www.class-central.com/subject/data-science',
				'https://www.class-central.com/subject/programming-and-software-development',
				'https://www.class-central.com/subject/engineering',
				'https://www.class-central.com/subject/maths'

		]
		urls2=[
				'https://www.class-central.com/subject/humanities',
				'https://www.class-central.com/subject/social-sciences',
				'https://www.class-central.com/subject/education',
				'https://www.class-central.com/subject/personal-development',
				'https://www.class-central.com/subject/art-and-design',
				'https://www.class-central.com/subject/health'

		]
		if ind == 1:
			sched = Job(CoursesSpider,fbadb = db,urls_to_scrape = urls1)
		else :
			sched = Job(CoursesSpider,fbadb = db,urls_to_scrape = urls2)
		processor = Processor(settings=None)
		data = processor.run([sched])
		
	
	def logdb(self):
		dic = {
				'start_timestamp' : self.startTime,
				'end_timestamp' : self.endTime	
		}
		db = FirebaseAccess()
		db.logs(dic)


		

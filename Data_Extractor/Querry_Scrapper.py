import os
from scrapyscript import Job, Processor
from Data_Extractor.Data_Ex.spiders.ClassCentral_Scrapper import ClassCentralSpider

class Scrapper:
	def scrape(self,query):
		# Create jobs for each instance. *args and **kwargs supplied here will
		# be passed to the spider constructor at runtime
		myJob = Job(ClassCentralSpider, keys=query)
		
		# Create a Processor, optionally passing in a Scrapy Settings object.
		processor = Processor(settings=None)
		
		# Start the reactor, and block until all spiders complete.
		data = processor.run([myJob])

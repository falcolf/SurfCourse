import scrapy
import json
import math
import re
import string
from rake_nltk import Rake
class CoursesSpider(scrapy.Spider):
	name = 'courses_datagen'

	def start_requests(self):
		urls=[
				'https://www.class-central.com/subject/cs',
				'https://www.class-central.com/subject/business',
				'https://www.class-central.com/subject/science',
				'https://www.class-central.com/subject/data-science',
				'https://www.class-central.com/subject/programming-and-software-development',
				'https://www.class-central.com/subject/engineering',
				'https://www.class-central.com/subject/maths',
				'https://www.class-central.com/subject/humanities',
				'https://www.class-central.com/subject/social-sciences',
				'https://www.class-central.com/subject/education',
				'https://www.class-central.com/subject/personal-development',
				'https://www.class-central.com/subject/art-and-design',
				'https://www.class-central.com/subject/health'

		]
		for url in urls:
			yield scrapy.Request(url = url,callback = self.parse)

	def parse(self,response):
		courses = int(response.xpath('//span[@id="number-of-courses"]/text()').extract_first())
		pages = math.ceil(courses/50)
		for i in range(1,pages+1):
			ext = response.request.url+'?page='+str(i)
			yield scrapy.Request(ext,callback = self.parse_pages)

	def parse_pages(self,response):

		links = response.xpath('//a[@class="text--charcoal text-2 medium-up-text-1 block course-name"]/@href').extract()
		for link in links:
			yield scrapy.Request(response.urljoin(link),callback = self.parse_links)
				

	def parse_links(self,response):
		sc_url = response.request.url;
		key1=sc_url.split('.com')[1]
		key=key1.replace('/','-')
		course_link = self.formatVal(response.xpath('//div[@class="course-data-button"]/a/@href').extract_first())
		course_name = self.formatVal(response.xpath('//h1[@id="course-title"]/text()').extract_first())
		course_subject = self.formatVal(response.xpath('//div[@class="course-data-row course-subject"]/a/text()').extract_first())
		course_val = self.formatVal(response.xpath('//div[@class="course-data-row course-provider"]/span[2]/text()').extract_first())
		#course_pace = self.formatVal(response.xpath('//div[@class="course-data-row course-pace"]/a/text()').extract_first())
		course_institution = self.formatVal(response.xpath('//div[@class="course-data-row course-institution"]/a/text()').extract_first())
		course_provider = self.formatVal(response.xpath('//div[@class="course-data-row course-provider"]/a/text()').extract_first())
		course_lang = self.formatVal(response.xpath('//div[@class="course-data-row course-language"]/a/text()').extract_first())
		course_certifications = self.formatVal(response.xpath('//div[@class="course-data-row course-certificates"]/span[2]/text()').extract_first())
		course_hours = self.formatVal(response.xpath('//div[@class="course-data-row course-hours"]/span[2]/text()').extract_first())
		course_duration = self.formatVal(response.xpath('//div[@class="course-data-row course-sessions"]/span[2]/span/text()').extract_first())
		course_prof = response.xpath('//div[@class="course-provider-wrap"]/span[2]/text()').extract()
		#course_keywords = self.getKeywords(course_subject,course_name);
		desc = response.xpath('//div[@id="course-tabs"]').extract()
		course_keywords = self.formatDesc(" ".join(desc),course_name)
		print("---------------")
		print(course_keywords)
		print("---------------")
		subkey = course_subject.replace(' ','-').lower()
		print("======================================")
		print(key)
		print("======================================")

		print("======================================")
		if course_name == 'Information_Not_Available':
			print('lalallalalallalalalal')
			print(sc_url)
		print("======================================")

		self.saveTocsv(course_keywords,course_subject)
		
	def formatDesc(self , desc , name):
		cleanr = re.compile('<.*?>')
		ct = re.sub(cleanr,'',desc)
		ct = re.sub('[^\w\s]','',ct)
		ct = ct.split()
		ct = [word for word in ct if not word == 'Information_Not_Available']
		ct = ' '.join(ct);
		r = Rake()
		r.extract_keywords_from_text(ct)
		flist = r.get_ranked_phrases()
		flist.append(name)
		return flist

	def formatVal(self,x):
		if not x:
			return 'Information_Not_Available'
		x=x.strip()
		x=x.replace('\n','')

		return x

	def saveTocsv(self , keywords , subs):
		print(keywords)
		print(subs)
		for wrd in keywords:
			stra = wrd + '\t' + subs
			with open('datafilenew1.tsv','a' , newline = '') as f :
				f.write(stra)
				f.write('\n')

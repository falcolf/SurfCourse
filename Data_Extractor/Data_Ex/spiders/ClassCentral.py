import scrapy
import json
import math
import re
import string
from rake_nltk import Rake
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
class CoursesSpider(scrapy.Spider):
	name = 'courses_scrapper'

	def __init__(self, fbadb='',urls_to_scrape=[] , **kwargs):
		self.db = fbadb
		self.urls_to_scrape=urls_to_scrape

	def start_requests(self):
		urls=self.urls_to_scrape
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
		course_institution = self.formatVal(response.xpath('//div[@class="course-data-row course-institution"]/a/text()').extract_first())
		course_provider = self.formatVal(response.xpath('//div[@class="course-data-row course-provider"]/a/text()').extract_first())
		course_lang = self.formatVal(response.xpath('//div[@class="course-data-row course-language"]/a/text()').extract_first())
		course_certifications = self.formatVal(response.xpath('//div[@class="course-data-row course-certificates"]/span[2]/text()').extract_first())
		course_hours = self.formatVal(response.xpath('//div[@class="course-data-row course-hours"]/span[2]/text()').extract_first())
		course_duration = self.formatVal(response.xpath('//div[@class="course-data-row course-sessions"]/span[2]/span/text()').extract_first())
		course_prof = response.xpath('//div[@class="course-provider-wrap"]/span[2]/text()').extract()		
		course_desc = response.xpath('//div[@id="course-tabs"]').extract()
		course_keywords = self.formatDesc(" ".join(course_desc),course_name)
		subkey = course_subject.replace(' ','-').lower()
		dic = {
					'sc_url' : sc_url,
					'course_link' : course_link,
					'course_name' : course_name,
					'course_subject' : course_subject,
					'course_val' : course_val,
					'course_institution' : course_institution,
					'course_provider' : course_provider,
					'course_lang' : course_lang,
					'course_certifications' : course_certifications,
					'course_hours' : course_hours,
					'course_duration' : course_duration,
					'course_prof' : course_prof,
					'course_keywords' : course_keywords
				}
		self.db.save(dic,course_subject,key)

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
		nltk.download('stopwords')
		ps = PorterStemmer()
		key_list = []
		for line in flist:
			keywords = line.split()
			keywords = [key.lower() for key in keywords]
			keywords = [ps.stem(word) for word in keywords if not word in set(stopwords.words('english'))]
			keywords = ' '.join(keywords)
			key_list.append(keywords)
		course_desc = ' , '.join(key_list)
		return course_desc

	def formatVal(self,x):
		if not x:
			return "Information_Not_AVailable"
		x=x.strip()
		x=x.replace('\n','')
		return x






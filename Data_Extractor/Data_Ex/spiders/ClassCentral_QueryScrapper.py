import scrapy
import json

class ClassCentralSpider(scrapy.Spider):
	name = 'classcentral_scrapper'

	def __init__(self, keys='', **kwargs):
		self.vals = keys
		super().__init__(**kwargs)

	def start_requests(self):
		urls=[
				'https://www.class-central.com/search?q='+self.vals #machine+learning
				#'https://www.class-central.com/subject/cs'
		]
		for url in urls:
			yield scrapy.Request(url = url,callback = self.parse)

	def parse(self,response):
		print(response.request.url)
		links = response.xpath('//a[@class="text--charcoal text-2 medium-up-text-1 block course-name"]/@href').extract()
		
		# f=open("linkdata.txt",'w')
		# for link in links:
		# 	f.write(link)
		# 	f.write('\n')		

		for link in links:
			yield scrapy.Request(response.urljoin(link),callback = self.parse_links)
			

	def parse_links(self,response):
		course_link = self.formatVal(response.xpath('//div[@class="course-data-button"]/a/@href').extract_first())
		course_name = self.formatVal(response.xpath('//h1[@class="course-title"]/text()').extract_first())
		course_subject = self.formatVal(response.xpath('//div[@class="course-data-row course-subject"]/a/text()').extract_first())
		course_val = self.formatVal(response.xpath('//div[@class="course-data-row course-provider"]/span[2]/text()').extract_first())
		course_pace = self.formatVal(response.xpath('//div[@class="course-data-row course-pace"]/a/text()').extract_first())
		course_institution = self.formatVal(response.xpath('//div[@class="course-data-row course-institution"]/a/text()').extract_first())
		course_provider = self.formatVal(response.xpath('//div[@class="course-data-row course-provider"]/a/text()').extract_first())
		course_lang = self.formatVal(response.xpath('//div[@class="course-data-row course-language"]/a/text()').extract_first())
		course_certifications = self.formatVal(response.xpath('//div[@class="course-data-row course-certificates"]/span[2]/text()').extract_first())
		course_hours = self.formatVal(response.xpath('//div[@class="course-data-row course-hours"]/span[2]/text()').extract_first())
		course_duration = self.formatVal(response.xpath('//div[@class="course-data-row course-sessions"]/span[2]/span/text()').extract_first())
		course_prof = self.formatProf(response.xpath('//div[@class="course-provider-wrap"]/ul/span[2]/text()').extract())
		print("===============================================================")
		print(course_link)
		print("\n")
		print(course_name)
		print("\n")
		print(course_provider)
		print("===============================================================")

		yield{

				'course_link' : course_link,
				'course_name' : course_name,
				'course_subject' : course_subject,
				'course_val' : course_val,
				'course_pace' : course_pace,
				'course_institution' : course_institution,
				'course_provider' : course_provider,
				'course_lang' : course_lang,
				'course_certifications' : course_certifications,
				'course_hours' : course_hours,
				'course_duration' : course_duration,
				'course_prof' : course_prof

			}

	def formatVal(self,x):
		if not x:
			return "Information Not AVailable"
		x=x.strip()
		x=x.replace('\n','')

		return x

	def formatProf(self,x):
		if not x:
			return "Information Not Available"

			


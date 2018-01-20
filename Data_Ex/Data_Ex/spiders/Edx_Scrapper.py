import scrapy

class EdxSpider(scrapy.Spider):
	name = 'edx_scrapper'

	def __init__(self, keys='', **kwargs):
		self.vals = keys
		super().__init__(**kwargs)

	def start_requests(self):
		urls=[
				 'https://www.edx.org/course?search_query'+self.vals #machine+learning
		]
		for url in urls:
			yield scrapy.Request(url = url,callback = self.parse)

	def parse(self,response):
		links = response.xpath('//a[@class = "course-link"]/@href').extract()
		for link in links:
			yield scrapy.Request(response.urljoin(link),callback = self.parse_links)

	def parse_links(self,response):
		
		##cannot load site data.

		link = response.request.url
		course_name = response.xpath('//h1[@id="course-intro-heading"]/text()').extract_first()
		website = 'Edx'
		creator = response.xpath('//li[@data-field="school"]/span[2]/a/text()').extract_first()
		taught_by = response.xpath('//p[@class="instructor-name"]/text()').extract()
		level = response.xpath('//li[@data-field="level"]/span[2]/text()').extract_first()
		yield{

				'link' : link,
				'course_name' : course_name,
				'provided via' : website,
				'creator' : creator,
				'taught_by' : taught_by,
				'level' : level,
				}

					


import scrapy

class CourseraSpider(scrapy.Spider):
	name = 'coursera_scrapper'

	def __init__(self, keys='', **kwargs):
		self.vals = keys
		super().__init__(**kwargs)

	def start_requests(self):
		urls=[
				'https://www.coursera.org/courses?languages=en&query='+self.vals #machine+learning
		]
		for url in urls:
			yield scrapy.Request(url = url,callback = self.parse)

	def parse(self,response):
		links = response.xpath('//a[@class = "rc-OfferingCard nostyle"]/@href').extract()
		for link in links:
			yield scrapy.Request(response.urljoin(link),callback = self.parse_links)

	def parse_links(self,response):
		link = str(response.request.url)
		if link.split('/')[-2] != 'specializations':
			link = response.request.url
			course_name = response.xpath('//div[@class="content-container vertical-box align-items-absolute-center"]/h2/text()').extract_first()
			website = 'Coursera'
			ctype = 'Single Course'
			creator = response.xpath('//div[@class="headline-1-text creator-names"]/span[2]/text()').extract_first()
			taught_by = response.xpath('//p[@class="instructor-name"]/span/a/text()').extract()
			ratings = response.xpath('//div[@class="ratings-text bt3-hidden-xs"]/span[1]/text()').extract_first()
			yield{

					'link' : link,
					'course_name' : course_name,
					'provided via' : website,
					'creator' : creator,
					'taught_by' : taught_by,
					'ratings' : ratings,
					'type' : ctype,
				}

		else:
			link = response.request.url
			course_name = response.xpath('//div[@class="rc-Header bt3-row p-a-1"]/h1/span/text()').extract_first()
			if not course_name:
				course_name = response.xpath('//div[@class="rc-Header bt3-row p-a-1"]/h1/text()').extract_first()
			website = 'coursera'
			ctype = 'Specialization'
			creator = response.xpath('//div[@class="rc-PartnerLogo"]/img/@alt').extract_first()
			ratings = 'Not Available'
			yield{

					'link' : link,
					'course_name' : course_name,
					'provided via' : website,
					'creator' : creator,
					'type' : ctype,
				}			


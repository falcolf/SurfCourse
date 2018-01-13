import scrapy
import json

class UdacitySpider(scrapy.Spider):
	name = 'udacity_scrapper'

	def __init__(self, keys='', **kwargs):
		self.vals = keys
		super().__init__(**kwargs)

	def start_requests(self):
		urls=[
				'https://in.udacity.com/courses/'+self.vals #machine-learning
				#https://in.udacity.com/courses/machine-learning
		]
		for url in urls:
			yield scrapy.Request(url = url,callback = self.parse)

	def parse(self,response):
		links = response.xpath('//div[@class = "col-sm-8"]/h3/a/@href').extract()
		course_names = response.xpath('//div[@class = "col-sm-8"]/h3/a/text()').extract()
		levels = response.xpath('//div[@class = "col-sm-4 hidden-xs"]/span/span[2]/text()').extract()
		fle = open('Udacity_Data.json','w')
		lst=[]
		for link,cname,level in zip(links,course_names,levels):
			dic = {
					'link' : response.urljoin(link),
					'level' : level,
					'course_name' : cname,
					'provided_via' : 'Udacity',
					'type' : 'Nano-degree',
				}
			lst.append(dic)

		json.dump(lst , fle)

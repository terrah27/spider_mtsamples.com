import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from mtsamples.items import MtsamplesItem

class MTSpider (CrawlSpider):
	name = 'mt'
	start_urls = ['https://www.mtsamples.com/site/pages/sitemap.asp']
	rules = (Rule(LinkExtractor(), callback='parse_url', follow=False),)

	def parse_url(self, response):
		item = MtsamplesItem()
		item['url'] = response.url
		return item

	def parse(self, response):
		hxs = scrapy.Selector(response)
		# extract all links from page
		all_links = hxs.xpath('*//a/@href').extract()
		# iterate over links
		for link in all_links:
			if ('/sample.asp?type' in link):
				yield scrapy.http.Request(response.urljoin(link), callback=self.parse_detail_page)

	def parse_detail_page(self, response):
		medical_specialty = response.css('h1::text').extract()[1]
		sample_name = response.css('h1::text').extract()[3]
		description = response.css('::text').extract()[98]
		transcription = response.css('::text').extract()[102:150]

		item = MtsamplesItem()
		item['medical_specialty'] = medical_specialty
		item['sample_name'] = sample_name
		item['description'] = description
		item['transcription'] = transcription
		yield item

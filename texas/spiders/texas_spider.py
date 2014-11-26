from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkxtractor
from scrapy.contrib.loader import XPathItemloader
from texas.items import TexasItem

class BasicSpider(BaseSpider):
	name = "texas_spider"
	allowed_domains = ["www.pytexas.org"]
	start_urls = ['http://www.pytexas.org/2014/schedule/']
	
	def parse(self,response):
		hxs = HtmlXPathSelector(response)
		dls = hxs.select('//dl')
		for dl in dls:
			times = dl.select('dt/text()').extract()
			titles = dl.select('dd/a/text()').extract()
			for time, title in zip(times, titles):
				title = title.strip()
				yield TexasItem(title=title, time=time)
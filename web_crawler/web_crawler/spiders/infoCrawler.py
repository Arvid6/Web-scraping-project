from typing import Iterable
import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bs4 import BeautifulSoup
from urllib.parse import urlparse


class infoCrawler(CrawlSpider):
    name = "getinfo"
    custom_settings = {
        'DEPTH_LIMIT': 1,
        'DOWNLOAD_TIMEOUT': 10,
    }

    def __init__(self, start_urls=None , keywords=None, *args, **kwargs):
        super(infoCrawler, self).__init__(*args, **kwargs)
        self.start_urls = start_urls if start_urls else []
        self.allowed_domains = [urlparse(url).netloc for url in self.start_urls]
        self.keywords = keywords if keywords else []
        # Dynamically create rules

        self.rules = (
            Rule(LinkExtractor(allow=self.keywords), callback='parse_item', follow=True),
        )
        self._compile_rules()
        # Debugging output
        print(f"Start URLs: {self.start_urls}")
        print(f"Allowed Domains: {self.allowed_domains}")
        print(f"Keywords: {self.keywords}")

        # Debugging output
        # print(f"Rules: {self.rules}")

    def parse_start_url(self, response):
        return self.parse_item(response)

    def parse_item(self, response):
        #if any(keyword in response.url for keyword in self.keywords):
        heat = BeautifulSoup(response.text, features="html.parser")

        for script in heat(["script", "style"]):
            script.extract()

        data = ' '.join(chunk for chunk in heat.get_text().split() if chunk)

        momentan_data = data

        return {str(response.url)[8:]: momentan_data}

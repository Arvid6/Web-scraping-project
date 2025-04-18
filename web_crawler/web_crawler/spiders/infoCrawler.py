from typing import Iterable
import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import tldextract
import requests
from io import BytesIO
from PyPDF2 import PdfReader


class infoCrawler(CrawlSpider):
    name = "getinfo"
    custom_settings = {
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
        # print(f"Start URLs: {self.start_urls}")
        # print(f"Allowed Domains: {self.allowed_domains}")
        # print(f"Keywords: {self.keywords}")

        # Debugging output
        # print(f"Rules: {self.rules}")

    def parse_item(self, response):
        if 'text/html' not in response.headers.get('Content-Type', b'').decode('utf-8'):
            if response.url.endswith('.pdf') or response.url.endswith('.pdf.aspx'):
                return self.handlePDF(response)  # Process PDFs
            self.logger.info(f"Skipping non-HTML response: {response.url}")
            return
        # If any(keyword in response.url for keyword in self.keywords):
        heat = BeautifulSoup(response.text, features="html.parser")

        for script in heat(["script", "style"]):
            script.extract()

        data = ' '.join(chunk for chunk in heat.get_text().split() if chunk)

        extracted = tldextract.extract(response.url)
        domain = f"{extracted.domain}.{extracted.suffix}"
        website = str(response.url)[8:]

        return {domain: {website: data}}

    def handlePDF(self, response):
        pdf_file = BytesIO(response.body)
        reader = PdfReader(pdf_file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() or ''

        extracted = tldextract.extract(response.url)
        domain = f"{extracted.domain}.{extracted.suffix}"
        website = str(response.url)[8:]

        return {domain: {website: text}}

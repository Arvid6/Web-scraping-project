from scrapy.crawler import CrawlerProcess
from googlecs import getSeach
from web_crawler.spiders.infoCrawler import infoCrawler


def webCrawler(key, reg, hl, gl, keywords, dep, res):
    """
        Perform web crawling to gather information about companies based on NACE code and region.

        Args:
            key (list): Keywords to search with
            reg (str): The region to search for companies in.
            hl (str): Language for Google search
            gl (str): Country for  Google search
            keywords (list): Keywords that help filter out websites


        Returns:
            None
    """

    start_urls = [] # add option to add keywords for diffrent languages

    for x in key:
        start_urls.extend(getSeach(x, res, reg, hl, gl))  # GET URLS FROM SEARCH WORDS
        print(x)

    print(start_urls)
    process = CrawlerProcess(settings={
        'DEPTH_LIMIT': dep,
        'assistant': 'getinfo',
        'ROBOTSTXT_OBEY': False,
        'FEED_FORMAT': 'json',  # OUTPUT FORMAT
        'FEED_URI': 'rawdataoutput.json',  # OUTPUT FILE
        'FEED_EXPORT_ENCODING': 'utf-8'  # Ensure correct encoding
    })

    process.crawl(infoCrawler, start_urls=start_urls, keywords=keywords)
    process.start()  # START THE CRAWL


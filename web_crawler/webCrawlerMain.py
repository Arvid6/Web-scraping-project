from scrapy.crawler import CrawlerProcess
from googlecs import getSeach
from web_crawler.spiders.infoCrawler import infoCrawler

def webCrawler(key, reg, wide):
    """
        Perform web crawling to gather information about companies based on NACE code and region.

        Args:
            key (str): Keywords to search with
            reg (str): The region to search for companies in.
            wide (bool): If the user wants to make a wider search that takes longer time but may yield better results.

        Returns:
            None
    """

    start_urls = []
                #["https://www.lpsignal.se", "https://swedtel.com", "https://mikrotema.se", "https://teamteknik.se/",
                #"https://tvent.se/", "https://www.airbus.com/en", "https://www.elgiganten.se/", "https://www.power.no/",
                #"https://vainu.io/company/digital-growth-sweden-ab-omsattning-och-nyckeltal/2151969340/foretagsinfo", "https://hagshult.se/",
                #"https://polkaprinsen.se/", "https://www.tekniskamuseet.se/", "https://miljogarden.se/", "https://svampkonsulent.se/",
                #"https://www.stadsmissionen.se/", "https://verktygsboden.se/", "https://bonaj.se/"]

    #https://www.jpinfonet.se/
    for x in key:
        start_urls.extend(getSeach(x, 1, reg)) # GET URLS FROM SEARCH WORDS
        print(x)

    print(start_urls)
    process = CrawlerProcess(settings={
        'assistant': 'getinfo',
        'ROBOTSTXT_OBEY': False,
        'FEED_FORMAT': 'json',  # OUTPUT FORMAT
        'FEED_URI': 'output.json'  # OUTPUT FILE
    })

    process.crawl(infoCrawler, start_urls=start_urls)
    process.start()  # START THE CRAWL


#('26300', 'Stockholm')
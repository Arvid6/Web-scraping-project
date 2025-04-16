from translate import translate, translatelist
from webCrawlerMain import webCrawler
from countrylist import getCountry
from regedit import clearjson, getdict
from datetime import datetime


def scrape(searchwords, keywords, otherwords, country, region, outputname, sensitivity, depth, results):
    """
        Starts the scrape and then sorts the list of scraped websites, also translates keywords.

        Args:
            searchwords (list): Words used for Google search to find legislations
            keywords (list): Keywords used to filter scraped data
            country (str): Language of search/translation
            region (str): Region of search
            outputname (str): Name of the output file
            sensitivity, depth, results (int): Params for scrape and sorting that
            let user customize how through the search and sorting will be


        Returns:
            None
    """
    start = datetime.now()
    clearjson('rawdataoutput.json')


    temp = []
    for x in searchwords:
        temp.append(x + " legislation")

    searchwords = temp
    lang = getCountry(country)  # Get language from country

    transkey = translatelist(keywords, country)
    searchkey = translatelist(searchwords, country)
    transsearch = translatelist(otherwords, country)

    keywords += transkey
    searchwords += searchkey
    otherwords += transsearch

    webCrawler(searchkey, region, lang[3], lang[1], otherwords, depth, results)  # Creates Output.json file.

    getdict('rawdataoutput.json', keywords, outputname, sensitivity)

    now = datetime.now()
    print(start.time())
    print(now.time())
    print("Done!")

    return 0


def sort_list(keywords, country, outputname, sensitivity):
    """
        Sorts and filters the JSON file without scraping a new one

        Args:
            keywords (list): Keywords used to filter scraped data
            country (str): Language of search/translation
            outputname (str): Name of the output file
            sensitivity(int): Params for sorting that
            let user customize how through the sorting will be


        Returns:
            None
    """
    keywords += translatelist(keywords, country)
    getdict('rawdataoutput.json', keywords, outputname, sensitivity)

# scrape()
# Take keywords, translate them to the languege of the country and include them in the search.
# Search the keywords using webCrawlerMain
# Send the data from the search to the NLP bot to sort it
# Output, file from infoCrawler is given to NLP and labled then returned as output.

# key = ["environmental", "waste", "reprocessing", "recycling"]

# sort_list(key, "finland", "Finlandtest2", 10)

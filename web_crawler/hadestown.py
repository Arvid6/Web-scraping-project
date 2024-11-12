from translate import translate, translatelist
from webCrawlerMain import webCrawler
from countrylist import getCountry
import googlecs
from regedit import clearjson, getdict

# from NLP.nlp import start_NLP


# start gui
# INPUTS: Keywords, Country, City/Providence (list?), Normal or bigger search.
def scrape(searchwords, keywords, country, region, outputname):
    clearjson('rawdataoutput.json')
    k = True
    # keywords = ["reprocessing", "recycling", "waste"]
    # searchwords = ["environmental legislation", "reprocessing legislation", "recycling legislation", "waste legislation"]
    otherwords = ["legislation", "regulation", "directive", "treary", "report", "incentives", "legislations",
                  "regulation", "directives", "treatys", "reports", "Legislation", "Regulation", "Directive",
                  "Legislations", "Regulations", "Directives", "Treatys", "Reports", "Incentives"]
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
    print("KEYWORDS")
    print(keywords)
    wide = True

    webCrawler(searchkey, wide, region, lang[3], lang[1], otherwords)  # Creates Output.json file.

    getdict('rawdataoutput.json', keywords, outputname)

    print("Done!")

    return 0


def sort_list(keywords, country, outputname):
    lang = getCountry(country)
    transkey = []
    for key in keywords:  # Translate the different words into correct language
        transkey.append(translate(key, country))
    getdict('rawdataoutput.json', keywords,outputname)

# scrape()
# Take keywords, translate them to the languege of the country and include them in the search.
# Search the keywords using webCrawlerMain
# Send the data from the search to the NLP bot to sort it
# Output, file from infoCrawler is given to NLP and labled then returned as output.

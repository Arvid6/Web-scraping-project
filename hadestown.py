from Translate.translate import translate
from web_crawler.webCrawlerMain import webCrawler
from Translate.countrylist import getCountry
from NLP.nlp import start_NLP


# start gui
# INPUTS: Keywords, Country, City/Providence (list?), Normal or bigger search.
def input():
    k = True
    keywords = []
    while k:
        temp = input("Type keyword, Done when done.")
        if temp.title() == 'Done':
            k = False
        else:
            keywords.append(temp)
    country = input("Type a country")
    lang = getCountry(country)
    print(lang)
    #keywords += translate(keywords, country)
    wide = False

    webCrawler(keywords, wide, lang[0], lang[3], lang[1]) #Creates Output.json file.

    print("Done!")

    return 0


# Take keywords, translate them to the languege of the country and include them in the search.
# Search the keywords using webCrawlerMain
# Send the data from the search to the NLP bot to sort it
# Output, file from infoCrawler is given to NLP and labled then returned as output.

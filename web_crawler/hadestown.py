from translate import translate
from webCrawlerMain import webCrawler
from countrylist import getCountry
import googlecs
from regedit import clearjson, getdict
#from NLP.nlp import start_NLP


# start gui
# INPUTS: Keywords, Country, City/Providence (list?), Normal or bigger search.
def startprogram():
    clearjson('output.json')
    k = True
    keywords = []
    otherwords = []
    while k:
        temp = input('Enter your keywords you want to use for the search, Done when done:')
        if temp.title() == 'Done':
            k = False
        else:
            keywords.append(temp)
    k = True
    while k:
        temp = input('Enter your other keywords, Done when done:')
        if temp.title() == 'Done':
            k = False
        else:
            otherwords.append(temp)
    country = input("Type country to search")
    while country == False:
        country = input("Type country to search")
    lang = getCountry(country)
    print(lang)
    transkey = []
    transsearch = []
    for key in keywords:
        transkey.append(translate(key, country))
    for word in otherwords:
        transsearch.append(translate(word, country))
    keywords += transkey
    otherwords += transsearch
    print(keywords)
    wide = True

    webCrawler(keywords, wide, lang[0], lang[3], lang[1], otherwords) #Creates Output.json file.

    getdict('output.json')

    print("Done!")

    return 0

startprogram()
# Take keywords, translate them to the languege of the country and include them in the search.
# Search the keywords using webCrawlerMain
# Send the data from the search to the NLP bot to sort it
# Output, file from infoCrawler is given to NLP and labled then returned as output.

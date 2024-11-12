from googletrans import Translator
from countrylist import getCountry
from unidecode import unidecode

translator = Translator()
def translate(electriccity, country):
    lang = getCountry(country)
    print(electriccity)
    try:
        conduct = translator.translate(electriccity, dest=lang[3])
    except Exception as e:
        print(f"Error translating '{electriccity}' to {lang[3]}: {e}")
        return electriccity  # or return the original word
    return conduct.text

def translatelist(oldlist, country):
    newlist = []
    for words in oldlist:
        word = translate(words, country)
        word2 = unidecode(word)
        if word2 != word:
            newlist.append(word)
            newlist.append(word2)
        else:
            newlist.append(word)
    return newlist



#print(translate(text, "United Kingdom"))
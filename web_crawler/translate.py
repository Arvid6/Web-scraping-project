from googletrans import Translator
from countrylist import getCountry

translator = Translator()
def translate(electriccity, country):
    lang = getCountry(country)
    print(electriccity)
    conduct = translator.translate(electriccity, dest=lang[3])
    return conduct.text


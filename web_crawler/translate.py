from googletrans import Translator
from countrylist import getCountry
from unidecode import unidecode

translator = Translator()
def translate(texxt, country):
    """
        Translate a phrase or word into a requested language

        Args:
            texxt (str): Phrase to be translated
            country (str): The country to translate to, used to get language.


        Returns:
            Translated text
    """
    lang = getCountry(country)
    try:
        conduct = translator.translate(texxt, dest=lang[3])
    except Exception as e:
        print(f"Error translating '{texxt}' to {lang[3]}: {e}")
        return texxt
    return conduct.text

def translatelist(oldlist, country):
    """
        Translate a list of phrases or words into a requested language,
        handles cases such as greek where we need the translation in both greek and latin letters

        Args:
            oldlist (list): Phrases to be translated
            country (str): The country to translate to, used to get language.


        Returns:
            List of translated texts
    """
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

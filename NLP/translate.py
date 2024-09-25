from googletrans import Translator


translator = Translator()
def translate(electriccity):
    conduct = translator.translate(electriccity)
    return conduct.text

print(translate('hejsan'))
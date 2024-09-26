from googletrans import Translator
from Translate.countrylist import getCountry


translator = Translator()
def translate(electriccity, country):
    lang = getCountry(country)

    conduct = translator.translate(electriccity, src=lang[3])
    return conduct.text

print(translate('est 4 viene completato dopo la lezione 4 ma prima della consegna del laboratorio 4. Il test consiste in domande a scelta multipla ed eventualmente domande combinate. Una o più opzioni potrebbero essere corrette. Per essere superato è richiesto un minimo del 70% di risposte corrette. Hai cinque tentativi ma il test può essere completato solo una volta al giorno, se non riesci a raggiungere il 70% devi aspettare un giorno per fare il tentativo successivo e leggere il materiale delle lezioni e prenotarti nuovamente. 4a-5a edizione; Capitoli 5.1-5.2, 6.6, 8.4, 9.8 6a edizione; Capitoli 5.1-5.3, 6.6, 8.5, 9.7', 'Italy'))
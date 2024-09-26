

clist = {
    "Finland": ["fi", "Finnish", "fi"],
    "Austria": ["at", "German", "de"],
    "Portugal": ["pt", "Portuguese", "pt"],
    "Greece": ["gr", "Greek", "el"],
    "Czech Republic": ["cz", "Czech", "cs"],
    "Spain": ["es", "Spanish", "es"],
    "Italy": ["it", "Italian", "it"],
    "France": ["fr", "French", "fr"],
    "United Kingdom": ["uk", "English", "en"]

}

def getCountry(country):
    country = country.title()
    if country in clist.keys():
        return [country] + clist[country]
    else:
        return False



print(getCountry('austRia'))
clist = {
    "Finland": ["fi", "Finnish", "fi", ("Helsinki,Uusimaa,Finland", "Espoo,Uusimaa,Finland",
                                        "Tampere,Pirkanmaa,Finland", "Oulu,North Ostrobothnia,Finland")],
    "Austria": ["at", "German", "de", ("Vienna,Austria", "Graz,Styria,Austria",
                                       "Linz,Upper Austria,Austria", "Favoriten,Vienna,Austria")],
    "Portugal": ["pt", "Portuguese", "pt", ("Lisbon,Portugal", "Porto,Porto District,Portugal",
                                            "Vila Nova de Gaia,Porto District,Portugal", "Braga,Portugal")],
    "Greece": ["gr", "Greek", "el", ("Athens,Decentralized Administration of Attica,Greece",
                                     "Thessaloniki,Central Macedonia,Greece",
                                     "Piraeus,Decentralized Administration of Attica,Greece",
                                     "Larissa,Decentralized Administration of Thessaly and Central Greece,Greece")],
    "Czech Republic": ["cz", "Czech", "cs", ("Prague,Prague,Czechia", "Brno,South Moravian Region,Czechia",
                                             "Ostrava,Moravian-Silesian Region,Czechia", "Liberec Region,Czechia")],
    "Sweden": ['se', 'Swedish', 'sv', ("Stockholm,Stockholm County,Sweden", "Lulea,Norrbotten County,Sweden")]

}

def getCountry(country):
    country = country.title()
    if country in clist.keys():
        return [country] + clist[country]
    else:
        return False


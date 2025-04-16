clist = {
    "Portugal": ["pt", "Portuguese", "pt", (
        "Lisbon,Portugal",
        "Porto,Porto District,Portugal",
        "Coimbra,Coimbra District,Portugal",
        "Evora,Evora District,Portugal"
    )],
    "Poland": ["pl", "Polish", "pl", (
        "Lublin Voivodeship,Poland",
        "Poland",
        "Swietokrzyskie Voivodeship,Poland",
        "Silesian Voivodeship,Poland",
        "Lubusz Voivodeship,Poland"
    )],
    "Croatia": ["hr", "Croatian", "hr", (
        "Croatia",
        "Split,Split-Dalmatia County,Croatia",
    )],
    "France": ["fr", "French", "fr", (
        "Paris,Ile-de-France,France",
        "La Reunion,Nouvelle-Aquitaine,France",
        "Lyon,Auvergne-Rhône-Alpes,France",
        "La Reunion,Nouvelle-Aquitaine,France"
    )],
    "Czechia": ["cz", "Czech", "cs", (
        "Prague,Prague,Czechia",
        "Czechia",
        "Ostrava,Moravian-Silesian Region,Czechia",
        "Plzeň,Plzeň Region,Czechia"
    )],
    "Greece": ["gr", "Greek", "el", (
        "Central Macedonia,Decentralized Administration of Macedonia and Thrace,Greece",
        "Decentralized Administration of Peloponnese, Western Greece and the Ionian,Greece",
        "Decentralized Administration of Epirus and Western Macedonia,Greece",
        "Decentralized Administration of the Aegean,Greece"
    )],
    "Spain": ["es", "Spanish", "es", (
        "Madrid,Community of Madrid,Spain",
        "Andalusia,Spain",
        "Castile-La Mancha,Spain",
        "Toledo,Castilla-La Mancha,Spain"
    )],
    "Italy": ["it", "Italian", "it", (
        "Apulia,Italy",
        "Calabria,Italy",
        "Molise,Italy",
        "Campania,Italy",
        "Sardinia,Italy",
        "Basilicata,Italy",
        "Sicily,Italy"
    )],
    "Latvia": ["lv", "Latvian", "lv", (
        "Riga,Riga Planning Region,Latvia",
        "Latvia",
        "Liepāja,Kurzeme,Latvia",
        "Jelgava,Zemgale,Latvia"
    )],
    "Lithuania": ["lt", "Lithuanian", "lt", (
        "Lithuania",
        "Kaunas,Kaunas County,Lithuania",
        "Klaipėda,Klaipėda County,Lithuania",
        "Šiauliai,Šiauliai County,Lithuania"
    )],
    "Hungary": ["hu", "Hungarian", "hu", (
        "Budapest,Central Hungary,Hungary",
        "Hungary",
        "Szeged,Csongrád County,Hungary",
        "Miskolc,Borsod-Abaúj-Zemplén County,Hungary"
    )],
    "Romania": ["ro", "Romanian", "ro", (
        "Cluj-Napoca,Cluj County,Romania",
        "Craiova,Dolj County,Romania",
        "Timisoara,Timis,Romania",
        "Iasi,Iasi County,Romania"
    )],
    "Slovakia": ["sk", "Slovak", "sk", (
        "Slovakia",
        "Kosice,Kosice Region,Slovakia",
        "Presov,Presov Region,Slovakia",
        "Zilina,Zilina Region,Slovakia"
    )]
}


#  "Finland": ["fi", "Finnish", "fi", ("Helsinki,Uusimaa,Finland", "Espoo,Uusimaa,Finland",
#                                      "Tampere,Pirkanmaa,Finland", "Oulu,North Ostrobothnia,Finland")],
#  "Austria": ["at", "German", "de", ("Vienna,Austria", "Graz,Styria,Austria",
#                                     "Linz,Upper Austria,Austria", "Favoriten,Vienna,Austria")],
#   "Portugal": ["pt", "Portuguese", "pt", ("Lisbon,Portugal", "Porto,Porto District,Portugal",
#                                          "Vila Nova de Gaia,Porto District,Portugal", "Braga,Portugal")],
#  "Greece": ["gr", "Greek", "el", ("Athens,Decentralized Administration of Attica,Greece",
#                                   "Thessaloniki,Central Macedonia,Greece",
#                                   "Piraeus,Decentralized Administration of Attica,Greece",
#                                   "Larissa,Decentralized Administration of Thessaly and Central Greece,Greece")],
#  "Czech Republic": ["cz", "Czech", "cs", ("Prague,Prague,Czechia", "Brno,South Moravian Region,Czechia",
#                                           "Ostrava,Moravian-Silesian Region,Czechia", "Liberec Region,Czechia")],
# "Sweden": ['se', 'Swedish', 'sv', ("Stockholm,Stockholm County,Sweden", "Lulea,Norrbotten County,Sweden")],
#  "Germany": ["de", "German", "de", ("Berlin,Germany", "Frankfurt, Hessen, Germany")],
# "Belgium": ["be", "German", "de", ("Brussels, Belgium", "Flanders, Belgium")],
# "Switzerland": ["ch", "German", "de", ("Zurich, Switzerland", "yo")],

def getCountry(country):
    """
        Gets language and region parameters from country name

        Args:
            country (str): Name of country

        Returns:
            List of relevant country params
    """
    country = country.title()
    if country in clist.keys():
        return [country] + clist[country]
    else:
        return False


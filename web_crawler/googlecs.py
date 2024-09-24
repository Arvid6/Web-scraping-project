# pip install serpapi FÖRST
# pip install google-search-results
from serpapi import GoogleSearch


def getSeach(word, num, reg):
    """
        Get search results URLs from Google based on search words.

        Args:
            word (str): The search word or phrase.
            num (int): The number of search results to retrieve.
            reg (str): The region to be searched

        Returns:
            list: A list of URLs representing the search results.
    """
    blacklist = ["allabolag.se", "merinfo.se", "bolagsfakta.se", "proff.se", "hitta.se", "ratsit.se", "creditsafe.com",
                 "s360digital.com", "vinjournalen.se", "largestcompanies.com", "axfood.se", "facebook.com",
                 "instagram.com", "wikipedia.org", "infoo.se", "arbetsformedlingen.se", "linkedin.com", "mrkoll.se",
                 "kreditrapporten.se", "mynewsdesk.com", "largestcompanies.se", "nyteknik.se", "eniro.se",
                 "tekniklagret.se", "datanyze.com", "starkabolag.se", "zoominfo.com", "bizzdo.se", "industritorget.se",
                 "kompass.com", "twitter.com", "x.com", "wiktionary.org", "youtube.com", "spotify.com", "expressen.se", "infinera.com", "mau.se", "campusnykoping.se",
                 "su.se", "gu.se"]
    params = {
        "q": word,
        "location": reg,  # OPTIONAL
        "hl": "sv",  # OPTIONAL
        "gl": "se",  # OPTIONAL
        "google_domain": "google.se",
        "api_key": "" #PUT API KEY HERE
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    organic_results = results.get('organic_results', [])

    filtered_results = [result for result in organic_results if
                        not any(blacklisted in result.get('link', '') for blacklisted in blacklist)]

    urls = [result.get('link') for result in filtered_results[:num]]  # NUMBER OF RESULTS

    return urls

# getSeach(["Umida Brands AB", "Urban Market Stockholm AB", "FRKY Foods AB"], "Stockholm County, Sweden", 4)

# pip install serpapi FÖRST
# pip install google-search-results
from serpapi import GoogleSearch


def getSeach(word, num, loc, hl, gl):
    """
        Get search results URLs from Google based on search words.

        Args:
            word (str): The search word or phrase.
            num (int): The number of search results to retrieve.
            reg (str): The region to be searched

        Returns:
            list: A list of URLs representing the search results.
    """
    blacklist = ["wikipedia.org", "gmail.com", "yahoo.com", "youtube.com", "instagram.com", "facebook.com",
                 "twitter.com", "linkedin.com", "x.com", "whatsapp.com", "reddit.com" , "amazon.com", "tiktok.com"]
    params = {
        "q": word,
        "location": loc,  # OPTIONAL
        "hl": hl,  # OPTIONAL
        "gl": gl,  # OPTIONAL
        "google_domain": "google.se",
        "api_key": "5f4693b65a0e9d1a165d3581f1f4ab4dd2dab0a7a77248a0d09da6fa33d01821" #PUT API KEY HERE
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    organic_results = results.get('organic_results', [])

    filtered_results = [result for result in organic_results if
                        not any(blacklisted in result.get('link', '') for blacklisted in blacklist)]

    urls = [result.get('link') for result in filtered_results[:num]]  # NUMBER OF RESULTS

    return urls

# getSeach(["Umida Brands AB", "Urban Market Stockholm AB", "FRKY Foods AB"], "Stockholm County, Sweden", 4)

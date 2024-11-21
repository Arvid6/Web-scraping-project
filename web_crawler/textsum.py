import spacy
from spacy.matcher import Matcher
#import xx_sent_ud_sm

nlp = spacy.load('xx_sent_ud_sm')

nlp.max_length = 20000000

def extract_text(text, keywords, sensitivity):
    """
        Filters websites based on numbers of mention of keywords and language params in URL query parameters

        Args:
            text (str): text that will be analyzed/filtered
            keywords (list): Keywords used to filter scraped data
            sensitivity (int): Sensitivity of the sorting


        Returns:
            Sorted and filtered dictionary in JSON format
    """
    matcher = Matcher(nlp.vocab)
    queryremover = Matcher(nlp.vocab)
    filter = ['prefLang', "languageId"]

    # Create patterns for whole word matches
    for keyword in keywords:
        if keyword.endswith("-"):
            keyword = keyword[:-1]
        matcher.add(keyword, [
            [{"TEXT": {"REGEX": f".*{keyword}.*"}}]])  # IS_ALPHA ensures we are matching only alphabetic tokens
    for x in filter:
        queryremover.add(x, [
            [{"LOWER": x.lower(), "IS_ALPHA": True}]])  # IS_ALPHA ensures we are matching only alphabetic tokens
        queryremover.add(f"{x}_partial", [
            [{"TEXT": {"REGEX": f".*{x}.*"}}]
        ])

    # Process the input text
    doc = nlp(text)
    matches = matcher(doc)
    query = queryremover(doc)
    print(str(len(matches)) + " | " + str(len(query)))
    if len(matches) > sensitivity and len(query) == 0:
        return len(matches)
    else:
        return False


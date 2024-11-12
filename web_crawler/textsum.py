import spacy
from spacy.matcher import Matcher
#import xx_sent_ud_sm

nlp = spacy.load('xx_sent_ud_sm')

nlp.max_length = 20000000
# Get the path of the model

def extract_text(text, keywords):
    matcher = Matcher(nlp.vocab)
    queryremover = Matcher(nlp.vocab)
    filter = ['prefLang', "languageId"]

    # Create patterns for whole word matches
    for keyword in keywords:
        #print(keyword)
        if keyword.endswith("-"):
            keyword = keyword[:-1]
        #    print(keyword)
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
    if len(matches) > 10 and len(query) == 0:
        return True
    else:
        return False


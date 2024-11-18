import json
from translate import translate
from textsum import extract_text


def clearjson(text):
    # Clears jSON tile
    with open(text, "w") as file:
        file.truncate()


def getdict(text, keywords, outputname, sensetivity):
    """
        Sorts the dictionary

        Args:
            text (str): Name of the dictionary with the unsorted unfiltered data
            keywords (list): Keywords used to filter scraped data
            outputname (str): Name of the output file
            sensetivity (int): Sensetivity of the sorting
            (not used here just needs to be pased through to the sorting)


        Returns:
            Sorted and filtered dictionary in JSON format
    """
    with open(text, 'r', encoding="utf8") as file:
        data = json.load(file)  # Load the entire file as a list of dictionaries

        # Initialize an empty dictionary to store the merged results
    merged_dict = {}

    # Process each dictionary in the list
    for current_dict in data:
        # Ensure current_dict is a dictionary
        if isinstance(current_dict, dict):
            for domain, websites in current_dict.items():
                if extract_text(str(websites), keywords, sensetivity):
                    if domain not in merged_dict:
                        merged_dict[domain] = {}
                    merged_dict[domain].update(websites)

    outputname += ".json"
    with open(outputname, 'w', encoding='utf8') as file:
        json.dump(merged_dict, file, ensure_ascii=False, indent=4)

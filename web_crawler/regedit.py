import json
from translate import translate


def clearjson(text):
    with open(text, "w") as file:
        file.truncate()

#def translatejson(text):

def merge_dicts(*dicts):
    final_dict = {}
    for d in dicts:
        for key in d.keys():
            if key not in final_dict:
                final_dict[key] = {}
            final_dict[key].update(d[key])
    return final_dict


def getdict(text):
    with open(text, 'r', encoding="utf8") as file:
        data = json.load(file)  # Load the entire file as a list of dictionaries

        # Initialize an empty dictionary to store the merged results
    merged_dict = {}

    # Process each dictionary in the list
    for current_dict in data:
        # Ensure current_dict is a dictionary
        if isinstance(current_dict, dict):
            for domain, websites in current_dict.items():
                if domain not in merged_dict:
                    merged_dict[domain] = {}
                merged_dict[domain].update(websites)

    with open('merged_output.json', 'w', encoding='utf8') as file:
        json.dump(merged_dict, file, ensure_ascii=False, indent=4)

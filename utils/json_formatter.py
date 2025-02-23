import json

def format_list_of_dicts(data):
    return json.dumps(data, indent=4)
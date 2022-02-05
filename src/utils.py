import json

def load_json_file(file_path):
    """Read a json file

    Args:
        file_path (str): path of the json filejson file path
    Returns:
        dict: dictionary format of the json file
    """
    with open(file_path) as f:
        data = json.load(f)
    return data
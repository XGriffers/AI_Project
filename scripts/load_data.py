import json

def load_json(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return data

def extract_text_data(data):
    text_data = [item['P tags'] for item in data]
    text_data = [item for sublist in text_data for item in sublist]
    return text_data
from bs4 import BeautifulSoup
import requests
import json
import shutil

urls = ['http://127.0.0.1:5500/html%20to%20scrape/scrape.html']
data = []

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all h1 tags
    h1_tags = soup.find('h1')
    # Find all p tags
    p_tags = soup.find_all('p')

    sections_data = {
        'H1 tags': [h1_tag.text for h1_tag in h1_tags],
        'P tags': [p_tag.text for p_tag in p_tags if p_tag.text != ' ']  # Remove empty strings
    }
    data.append(sections_data)

filename = 'data.json'

with open(filename, 'w') as f:
    json.dump(data, f, indent=4)
    print('Data saved to', filename)

source_file = 'data.json'
destination_dir = '../data/'
shutil.move(source_file, destination_dir)
print('File moved to', destination_dir)
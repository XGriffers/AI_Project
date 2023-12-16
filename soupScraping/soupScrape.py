from bs4 import BeautifulSoup
import requests
import json


urls = ['https://www.forbes.com/advisor/business/start-a-blog/', 'https://www.theblogstarter.com/']
data = []

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Assuming each h1 is within a 'section' or 'div' and the p tags you want are direct children
    sections = soup.find_all(['section', 'body', 'div'], recursive=True)  # Adjust tag names as needed

    for section in sections:
        h2_tag = section.find('h2')
        h3_tag = section.find('h3')
        P_tag = section.find('p')
        if h2_tag:
            section_data = {
                "H2 tag": h2_tag.get_text(strip=True),
                
                "P tags": [p.get_text(strip=True) for p in section.find_all('p')]
            }
        if h3_tag:
            section_data = {
                "H3 tag": h3_tag.get_text(strip=True),
                
                "P tags": [p.get_text(strip=True) for p in section.find_all('p')]
            }
            data.append(section_data)

filename = 'data.json'

with open(filename, 'w') as f:
    json.dump(data, f, indent=4)


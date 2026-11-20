import re
import requests
from fake_useragent import UserAgent

links = []
pages = []
with open('..\\data_collected\\brand_links.txt', 'r') as f:
    for line in f:
        name, link = line.split(sep= ':')
        name_pattern = r'([A-Za-z]+)(?![part numbers])'
        text = re.findall(name_pattern, name)
        name = ''
        for t in text:
            name = name + t + ' '
        print(name)
        name = name[1: -1]
        links.append((name.strip(), link.strip()))

for i, link in enumerate(links):
    l = link[1].split(sep= '/')
    url = f"https://autofactsdb.com/{l[1]}/{l[2]}/"

    session = requests.Session()

    params = {
        'url': url,
        'x-api-key': 'e564b487cef04cbd97a2321329b8bfe4'
    }

    headers = {
        'User-Agent': UserAgent().random
    }

    response = session.get(
        'https://api.scrapingant.com/v2/general',
        params=params,
        headers=headers
    )
    text = response.text

    with open(f'{link[0]}.html', 'w', encoding= 'utf-8') as f:
        f.write(text)
    
    print(f'..\\html_pages_collected\\{link[0]}.html page is fully extracted.')
    pages.append(f'{link[0]}.html')

with open('..\\data_collected\\brand_pages_name.txt', 'w') as f:
    for page in pages:
        f.write(page + '\n')
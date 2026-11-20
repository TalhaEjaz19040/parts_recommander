from bs4 import BeautifulSoup

with open('..\\html__pages_collected\\autofactsdb.html', 'r', encoding= 'utf-8') as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')

links = []
links_set = set()
for l in soup.find_all('a', class_= 'card brand-card'):
    link = (l.get_text(strip= True), l.get('href'))
    if link in links_set:
        links.append(link)
    else: 
        links_set.add(link)

with open('..\\data_collected\\brand_links.txt', 'w') as f:
    for link in links:
        f.write(link[0] + ' : ' + link[1] + '\n')
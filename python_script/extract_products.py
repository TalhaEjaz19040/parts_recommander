from bs4 import BeautifulSoup

pages_name = []
with open('..\\data_collected\\pages_name.txt', 'r') as f:
    for line in f:
        pages_name.append(line.strip())

print(pages_name)

for page_name in pages_name:
    links = []
    with open(page_name, 'r', encoding= 'utf-8') as f:
        page_content = f.read()
    soup = BeautifulSoup(page_content, 'html.parser')

    for obj in soup.find_all('a', class_= 'card part-card'):
        links.append((obj.get_text(strip= True), obj.get('href')))

    with open('..\\data_collected\\product_links.txt', 'a') as f:
        for link in links:
            f.write(link[0] + ' : ' + link[1] + '\n')
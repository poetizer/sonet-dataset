import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

book = epub.read_epub('Antologia Poetica - Gregorio de Matos.epub')
count = 0
raw = []
poemas = {}

for item in book.get_items():
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
        if count > 6:
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            for h1 in soup.find_all('h1'):
                for br in h1.find_all('br'):
                    br.extract()
            extract = soup.get_text().strip().split('\n')
            raw.append(soup.get_text().strip())
            titulo = extract[0]
            corpo = extract[1:]
            poemas[titulo] = corpo
        count += 1

file = open('antologia-gregorio.txt', 'w')


file.write('A Cristo S. N. crucificado, estando o poeta na última hora de sua vida\n' +
           '\n'.join(poemas['A Cristo S. N. crucificado, estando o poeta na última hora de sua vida']))
print(poemas.keys())

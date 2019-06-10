import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

book = epub.read_epub('Toda Poesia - Paulo Leminski.epub')
count = 0
raw = []
poemas = {}
ignoreNext = False  # para ignorar os epígrafes após início da cada capítulo

for item in book.get_items():
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
        if count > 3 and not ignoreNext:
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            extract = soup.get_text().strip().split('\n')
            raw.append(soup.get_text().strip())
            titulo = extract[0]
            corpo = extract[1:]
            # if len(corpo) == 0 and not titulo == 'ALFÂNDEGA':
            #     ignoreNext = True
            # elif titulo == 'Alfândega':
            #     ignoreNext = True
            poemas[titulo] = corpo
        # elif ignoreNext:
        #     ignoreNext = False
        count += 1

# file = open('toda-poesia.txt', 'w')

# dataset = ''

# for titulo in poemas.keys():
#     dataset += titulo.upper() + '\n\n'
#     dataset += '\n'.join(poemas[titulo]) + '\n\n'

# file.write(dataset)
print(poemas.keys())

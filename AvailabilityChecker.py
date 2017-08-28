import json
import urllib3
import xml.etree.ElementTree as ET
from pprint import pprint

class Book:
    def __init__(self, ISBN):
        self.ISBN = ISBN

        http = urllib3.PoolManager()
        validatie = http.request('GET', 'http://zoeken.bibliotheek.be/validate.ashx?isbn=' + str(self.ISBN))
        self.available = None
        print(int(validatie.data))
        if int(validatie.data) == 1:
            r = http.request('GET',
                             'http://zoeken.bibliotheek.be/api/v0/search/?q=isbn:' + str(
                                 self.ISBN) + '&authorization=ac135e89f84460a251a6283a14180a22')

            root = ET.fromstring(r.data)

            r = http.request('GET',
                             'http://zoeken.oost-vlaanderen.bibliotheek.be/api/v0/availability/?id=' + root[1][0][
                                 0].text + '&authorization=f2c359618130a698cca2e6b2736ab9fc&branch=Gent')
            root = ET.fromstring(r.data)
            self.available = root[1][0][0].attrib['available']
        else:
            print("ISBN is not valid")




with open('Krookie.json') as data_file:
    data = json.load(data_file)
books_data = data['books']

books = [Book(book_data["ISBN"]) for book_data in books_data]

for i, book_data in enumerate(data['books']):

    book_data['available'] = books[i].available

with open('Krookie.json', 'w') as outfile:
    json.dump(data, outfile, indent= 2)




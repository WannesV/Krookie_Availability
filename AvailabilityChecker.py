import json
import urllib3
import xml.etree.ElementTree as ET
from pprint import pprint

class Book:
    def __init__(self, ISBN):
        self.ISBN = str(ISBN)
        self.available = None
        self.check_availability()

    def check_availability(self):
        http = urllib3.PoolManager()
        #Zoeken of het een geldig ISBN is, 1 = geldig 0 = niet geldig
        validatie = http.request('GET', 'http://zoeken.bibliotheek.be/validate.ashx?isbn=' + self.ISBN)

        if int(validatie.data) == 1:
            #Id van het boek zoeken
            r = http.request('GET',
                             'http://zoeken.bibliotheek.be/api/v0/search/?q=isbn:' + str(
                                 self.ISBN) + '&authorization=ac135e89f84460a251a6283a14180a22')

            root = ET.fromstring(r.data)
            id = root[1][0][0].text
            
            #Availability van het boek zoeken
            r = http.request('GET',
                             'http://zoeken.oost-vlaanderen.bibliotheek.be/api/v0/availability/?id=' + id + '&authorization=f2c359618130a698cca2e6b2736ab9fc&branch=Gent')

            root = ET.fromstring(r.data)
            self.available = root[1][0][0].attrib['available']

        else:
            print("ISBN is not valid")


#Main

#Lees JSON file
with open('Krookie.json') as data_file:
    data = json.load(data_file)

#Filter enkel de boeken eruit
books_data = data['books']

#Maak book objecten voor elk boek
books = [Book(book_data["ISBN"]) for book_data in books_data]

#Toevoegen/Aanpassen available attribuut
for i, book_data in enumerate(data['books']):
    book_data['available'] = books[i].available

#Updaten JSON bestand
with open('Krookie.json', 'w') as outfile:
    json.dump(data, outfile, indent= 2)
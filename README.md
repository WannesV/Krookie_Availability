# Krookie_Availability
De code zal van alle boeken in het JSON bestand het ISBN-nummer inlezen.
Via het ISBN-nummer zoeken we via de API het id van het boek.
En met dat id kunnen we met de API vinden of het boek nog beschikbaar is in de Hoofdbibliotheek van Gent.
Dan updaten we in het bestand de availability van alle boeken.
Als er een ongeldig ISBN-nummer in het bestand stond zal het attribuut available op null staan.

## Werking API
Link: https://docs.google.com/spreadsheets/d/1PnyOzCkxSnEWKqmTk6bsnuorAIk27-8yvD2gKf6zq_4/edit#gid=396611154

* **Zoeken op ISBN**

     http://zoeken.oost-vlaanderen.bibliotheek.be/api/v0/search/?q=isbn:9789461310422&authorization=f2c359618130a698cca2e6b2736ab9fc

      Geeft een xml met informatie over het boek. Wij zoeken de id van het boek, 
      die vind je onder de tag meta in het element id, nativeid.

* **ISBN Valideren**

     http://zoeken.bibliotheek.be/validate.ashx?isbn=9789041300522

      Returnt 1 als het een geldige ISBN, anders 0.

* **Beschikbaarheid zoeken a.d.h.v. id**

     http://zoeken.gent.bibliotheek.be/api/v0/availability/?id=|library/marc/vlacc|7490283&authorization=26f9ce7cdcbe09df6f0b37d79b6c4dc2
     
      'library/marc/vlacc|7490283' is het id.
      Geeft een xml terug met informatie over het boek in alle bibliotheken in de steden van Oost-Vlaanderen.
      Het attribuut available in Gent is true als het boek in 1 van de bibs in Gent beschikbaar is. 
      We moeten dus kijken naar het attribuut available bij de Hoofdbibliotheek

* **Beschikbaarheid zoeken a.d.h.v. beid**

     http://zoeken.gent.bibliotheek.be/api/v0/availability/?beid=7490283&authorization=26f9ce7cdcbe09df6f0b37d79b6c4dc2
     
       '7490283' is het beid.

* **Beschikbaarheid zoeken in specifieke branch**

     http://zoeken.oost-vlaanderen.bibliotheek.be/api/v0/availability/?id=|library/marc/vlacc|7490283&authorization=f2c359618130a698cca2e6b2736ab9fc&branch=Gent

      Zal dezelfde xml file teruggeven maar met de gespecifieerde branch vanboven, 
      dan terug de rest alfabetisch.

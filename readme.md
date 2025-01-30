# Aplikacija za Interakciju s OpenAI Asistentom

## Opis

Ova aplikacija omogućuje korisnicima interakciju s OpenAI asistentom putem RESTful API-ja. Omogućuje slanje upita asistentu i primanje odgovora u JSON formatu. Aplikacija koristi Flask za implementaciju servera i Flask-RESTful za definiranje RESTful API endpointa.

## Značajke

1. **_ Postavljanje Upita _**

- Korisnici mogu postavljati upite asistentu putem HTTP POST zahtjeva na odgovarajuće rute.
- Zahtjevi se šalju u JSON formatu s potrebnim podacima kao što su korisnički ID, ime, i sadržaj poruke.

2. **_ OpenAI Asistent _**

- Aplikacija koristi OpenAI platformu za pružanje inteligentnih odgovora na postavljene upite.
- Asistent je treniran na bogatom skupu podataka i sposoban je pružiti relevantne i korisne odgovore na različite vrste upita.

3. **_ Pohrana Podataka _**

- Aplikacija pohranjuje povratne informacije korisnika o odgovorima asistenta u CSV datoteku.
- Korisnici mogu ocijeniti odgovore asistenta, a te informacije se dodaju u CSV datoteku radi daljnje analize i poboljšanja asistenta.

## Arhitektura

Aplikacija se temelji na Flask frameworku za razvoj web aplikacija u Pythonu. Flask-RESTful se koristi za jednostavnu implementaciju RESTful API-ja. Podaci se pohranjuju lokalno u CSV datoteku.

## Uključene datoteke

### 1. `app.py`

Pruženi kod postavlja Flask aplikaciju s dva RESTful API endpointa koristeći Flask-RESTful ekstenziju. Evo kratkog pregleda koda:

#### Postavljanje Flask Aplikacije

- Kod inicijalizira instancu Flask aplikacije nazvanu `app`.
- Također inicijalizira instancu Flask-RESTful API-a nazvanu `api` povezanu s Flask aplikacijom.

#### RESTful API Endpointi

- Kod uvozi i dodaje dva resursa u Flask-RESTful API:
  - `AssistantApi` iz modula `assistant_api`, povezan s rutom "/ask".
  - `AssistantFeedback` iz modula `assistant_feedback`, povezan s rutom "/feedback".

#### Blok `if __name__ == "__main__":`

- Ovaj blok osigurava da se Flask aplikacija pokrene samo ako se skripta izvršava izravno (ne uvezena kao modul).
- Pokreće Flask aplikaciju u načinu za debugiranje (`debug=True`), omogućavajući značajke za debugiranje poput interaktivnog debugera i automatskog ponovnog učitavanja koda kada se detektiraju promjene.

Ukratko, kod postavlja Flask aplikaciju s dva RESTful API endpointa ("/ask" i "/feedback") koristeći Flask-RESTful, omogućavajući klijentima interakciju s funkcionalnošću asistenta koju pruža API. Aplikacija se pokreće u načinu za debugiranje, olakšavajući procese razvoja i debugiranja.

### 2. `assistant_api.py`

Pruženi kod postavlja Flask RESTful API za interakciju s OpenAI asistentom. Evo kratkog pregleda:

- Kod uvozi potrebne biblioteke i inicijalizira varijable okruženja koristeći `dotenv`.
- Definira funkcije za upravljanje nitima i pokretanje OpenAI asistenta.
- Klasa `AssistantApi` je Flask RESTful resurs koji obrađuje POST zahtjeve.
- Nakon što primi POST zahtjev, klasa `AssistantApi` dohvaća podatke iz JSON zahtjeva.
- Provjerava postoji li nit za dani `nastavnik_id`, stvara novu ako ne postoji i dodaje korisnikovu poruku u nit.
- Zatim se poziva OpenAI asistent kako bi generirao odgovor na temelju korisničke poruke.
- Odgovor se sprema zajedno s pitanjem korisnika u CSV datoteku nazvanu 'responses.csv'.
- Konačno, odgovor zajedno s statusom uspješnosti vraća se u JSON formatu.

U slučaju bilo kakvih pogrešaka tijekom procesa, implementirano je odgovarajuće rukovanje pogreškama koje vraća JSON odgovor s porukom o pogrešci.

### 3. `assistant_feedback.py`

Ovaj kod definira Flask RESTful resurs za primanje povratnih informacija od korisnika. Evo kratkog pregleda:

- Klasa `AssistantFeedback` je Flask RESTful resurs koji obrađuje POST zahtjeve.
- Kada primi POST zahtjev, klasa `AssistantFeedback` dohvaća korisnički unos iz obrasca.
- Unos se čita iz CSV datoteke u DataFrame pomoću biblioteke pandas.
- Dohvaća se indeks zadnjeg reda u DataFrame-u.
- Vrijednost u DataFrame-u se ažurira s korisničkim unosom.
- Ažurirani DataFrame se ponovno sprema u CSV datoteku.
- Ako dođe do bilo kakve greške tijekom procesa, vraća se odgovarajući JSON odgovor s porukom o grešci.

U slučaju uspješnog ažuriranja, vraća se JSON odgovor s oznakom uspješnosti i porukom "Feedback successfully submitted".

### 4. `create_assistant.py`

Ovaj kod se odnosi na postavljanje virtualnog asistenta koristeći OpenAI platformu. Evo kratkog pregleda:

#### Upload datoteke

- Funkcija `upload_file` služi za upload datoteke s određenom svrhom.
- Datoteka se uploada s namjenom "assistants".

#### Stvaranje asistenta

- Funkcija `create_assistant` stvara virtualnog asistenta s određenim karakteristikama:
  - Ime asistenta je "eDnevnik virtualni asistent".
  - Asistent ima priložene upute u PDF formatu za rad s e-Dnevnikom.
  - Odgovori asistenta trebaju biti na književnom hrvatskom jeziku i trebaju biti jasni.
  - Asistent koristi model "gpt-4-1106-preview".
  - Datoteka s uputama dodaje se kao prilog asistentu.

### 5. `example.env`

Služi za upis osjetljvog OpenAI API Key-a i ID kreiranog asistenta

## Upute za pokretanje

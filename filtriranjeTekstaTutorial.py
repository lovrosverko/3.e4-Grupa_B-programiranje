# -*- coding: utf-8 -*-

# =============================================================================
# PROJEKT: ALAT ZA ANALIZU TEKSTA (FAZA 3 - Kompletno rješenje)
# =============================================================================
#
# Ovaj program je konzolna aplikacija koja vrši analizu tekstualne datoteke.
# Cilj je pročitati tekst, prebrojati koliko se puta svaka riječ ponavlja,
# te na kraju ispisati sortiranu listu najčešćih riječi.
#
# Program radi u nekoliko ključnih koraka (pipeline):
#
# 1. UČITAVANJE TEKSTA:
#    - Funkcija `ucitaj_tekst` sigurno učitava sadržaj iz datoteke 'tekst.txt'.
#    - Koristi `try-except` blok da spriječi rušenje programa ako datoteka ne postoji.
#
# 2. ČIŠĆENJE I TOKENIZACIJA:
#    - Funkcija `ocisti_tekst` priprema tekst za analizu.
#    - Sav tekst se pretvara u mala slova i uklanjaju se interpunkcijski znakovi.
#    - Na kraju, tekst se "tokenizira", tj. razbija u listu pojedinačnih riječi.
#
# 3. BROJANJE FREKVENCIJA:
#    - Funkcija `broji_frekvenciju` prolazi kroz listu riječi i sprema ih u rječnik.
#    - Riječ je ključ, a broj ponavljanja je vrijednost.
#
# 4. FILTRIRANJE "STOP-WORDS":
#    - Funkcija `ukloni_stop_words` iz rječnika izbacuje česte, ali nevažne
#      riječi (npr. 'i', 'u', 'na', 'je') kako bi rezultati bili smisleniji.
#
# 5. SORTIRANJE I ISPIS:
#    - Funkcija `sortiraj_i_ispisi` uzima pročišćeni rječnik, sortira ga po
#      frekvenciji (od najveće prema najmanjoj) i ispisuje formatiranu
#      listu najčešćih riječi.
#
# =============================================================================

# Konstantu sa "stop-words" definiramo na početku programa.
# Dobra je praksa da se ovakve fiksne vrijednosti koje se ne mijenjaju
# pišu velikim slovima (npr. STOP_WORDS, PI, MAX_BRZINA).
STOP_WORDS = ['ako', 'i', 'u', 'na', 'je', 'ali', 'a', 'o', 'li', 'te', 'se', 'za', 'su', 'to', 'sa', 'od', 'do', 'što']

# Funkcija za učitavanje teksta iz datoteke
def ucitaj_tekst(filepath):
    """Pokušava pročitati sadržaj datoteke na zadanoj putanji."""
    # 'try...except' blok je mehanizam za rukovanje greškama.
    # Program će prvo pokušati izvršiti kod unutar 'try' bloka.
    try:
        # 'with open(...) as file:' je najbolji način za rad s datotekama.
        # Automatski osigurava da će datoteka biti zatvorena nakon korištenja,
        # čak i ako se dogodi greška.
        # 'encoding="utf-8"' je važno kako bi se ispravno pročitala naša slova (č,ć,š,đ,ž).
        with open(filepath, "r", encoding="utf-8") as file:
            sadrzaj = file.read() # Čitamo cijeli sadržaj datoteke i spremamo ga u jednu varijablu.
        return sadrzaj
    # Ako se u 'try' bloku dogodi greška 'FileNotFoundError' (datoteka ne postoji),
    # program se neće srušiti, već će izvršiti kod u 'except' bloku.
    except FileNotFoundError:
        print(f"GREŠKA: Datoteka '{filepath}' nije pronađena.")
        return None # Vraćamo specijalnu vrijednost 'None' da signaliziramo grešku.

# Funkcija za pročišćavanje teksta
def ocisti_tekst(tekst):
    """Prima string, pretvara ga u mala slova, uklanja interpunkciju i vraća listu riječi."""
    tekst = tekst.lower() # Sve pretvaramo u mala slova da 'Riječ' i 'riječ' budu isto.
    
    # Lista svih znakova koje želimo ukloniti.
    interpunkcija = ['.', ',', '!', '?', ':', ';', '"', "'", '(', ')']
    
    # Prolazimo petljom kroz svaki znak u listi interpunkcije.
    for znak in interpunkcija:
        # Metoda .replace() zamjenjuje svaki interpunkcijski znak s praznim stringom (briše ga).
        tekst = tekst.replace(znak, '')
        
    # Metoda .split() razdvaja string u listu pojedinačnih riječi.
    # Razdvajanje se vrši po razmacima. Ovaj proces se zove "tokenizacija".
    lista_rijeci = tekst.split()
    return lista_rijeci

# Funkcija za brojanje frekvencije riječi
def broji_frekvenciju(lista_rijeci):
    """Prima listu riječi i vraća rječnik s njihovim frekvencijama."""
    brojac_rijeci = {} # Kreiramo prazan rječnik gdje ćemo spremati rezultate.
    
    # Prolazimo kroz svaku riječ u listi koju smo dobili.
    for rijec in lista_rijeci:
        # Pitamo se: "Postoji li ova riječ već kao ključ u našem rječniku?"
        if rijec in brojac_rijeci:
            # Ako postoji, samo povećamo njenu vrijednost (brojač) za 1.
            brojac_rijeci[rijec] += 1
        else:
            # Ako ne postoji, dodajemo je kao novi ključ s početnom vrijednošću 1.
            brojac_rijeci[rijec] = 1
    return brojac_rijeci

# Funkcija za uklanjanje "stop-words" iz rječnika
def ukloni_stop_words(rjecnik_frekvencija):
    """
    Prima rječnik frekvencija i vraća NOVI rječnik koji ne sadrži "stop-words".
    """
    ocisceni_rjecnik = {} # Kreiramo novi, prazan rječnik.
    
    # Metoda .items() nam omogućuje da istovremeno prolazimo kroz ključeve i vrijednosti rječnika.
    # 'rijec' će biti ključ, a 'broj' će biti vrijednost za svaki par.
    for rijec, broj in rjecnik_frekvencija.items():
        # Ako riječ NIJE u listi stop-words...
        if rijec not in STOP_WORDS:
            # ...onda je dodajemo u naš novi, očišćeni rječnik.
            ocisceni_rjecnik[rijec] = broj
    return ocisceni_rjecnik

# Funkcija za sortiranje i ispis rezultata (UKLJUČUJE BONUS ZADATAK)
def sortiraj_i_ispisi(rjecnik_frekvencija, broj_rijeci=15):
    """
    Sortira rječnik po vrijednostima (frekvencijama) i ispisuje
    formatiranu listu najčešćih riječi. Prima neobavezni argument broj_rijeci.
    Vrijednost `broj_rijeci=15` je zadana (default) vrijednost ako korisnik ne navede drugu.
    """
    # 1. Pretvaramo rječnik u listu n-torki (parova) pomoću .items().
    #    Primjer: {'a': 5, 'b': 2} postaje [('a', 5), ('b', 2)]
    lista_parova = rjecnik_frekvencija.items()

    # 2. Sortiramo listu parova pomoću ugrađene funkcije `sorted()`.
    #    `sorted()` uvijek vraća NOVU, sortiranu listu.
    #    - key=lambda item: item[1] -> Ovo je pravilo sortiranja.
    #      `lambda` kreira kratku, anonimnu funkciju. `item` je privremeno ime za svaki par (npr. ('a', 5)).
    #      `item[1]` znači da za sortiranje gledamo samo DRUGI element para (broj).
    #    - reverse=True -> Pravilo: Sortiraj od najvećeg prema najmanjem.
    sortirana_lista = sorted(lista_parova, key=lambda item: item[1], reverse=True)

    # 3. Ispisujemo rezultate. f-string nam omogućuje lako formatiranje ispisa.
    print(f"\n--- Top {broj_rijeci} najčešćih riječi ---")
    
    # Koristimo "slicing" `[:broj_rijeci]` da uzmemo samo prvih N elemenata iz sortirane liste.
    # `enumerate()` je korisna funkcija koja nam uz svaki element daje i redni broj (indeks).
    # `i` će biti redni broj (0, 1, 2...), a `(rijec, frekvencija)` će biti par iz liste.
    for i, (rijec, frekvencija) in enumerate(sortirana_lista[:broj_rijeci]):
        # Ispisujemo redni broj (i+1 jer indeksi kreću od 0), riječ i njenu frekvenciju.
        print(f"{i+1}. {rijec}: {frekvencija}")
    
    # Dinamički stvaramo donju crtu ovisno o broju riječi za ljepši ispis.
    print("-" * (25 + len(str(broj_rijeci))))


# --- Glavni dio programa ---
# `if __name__ == "__main__":` je standard u Pythonu.
# Kod unutar ovog bloka će se izvršiti samo ako pokrenemo ovu datoteku direktno,
# a ne ako je uvezemo (import) u neku drugu datoteku.
if __name__ == "__main__":
    
    # KORAK 1: Učitaj tekst iz datoteke.
    putanja_datoteke = 'tekst.txt'
    print(f"1. Učitavam tekst iz datoteke: {putanja_datoteke}")
    ucitani_tekst = ucitaj_tekst(putanja_datoteke)

    # Provjeravamo je li tekst uspješno učitan (tj. da nije None).
    if ucitani_tekst:
        # KORAK 2: Očisti tekst (mala slova, interpunkcija...).
        print("2. Čistim tekst...")
        ociscene_rijeci = ocisti_tekst(ucitani_tekst)
        
        # KORAK 3: Prebroji frekvenciju SVIH riječi.
        print("3. Brojim koliko se puta svaka riječ ponavlja...")
        sve_frekvencije = broji_frekvenciju(ociscene_rijeci)
        
        # KORAK 4: Ukloni "stop-words" iz rječnika frekvencija.
        print("4. Uklanjam česte, ali nevažne riječi ('stop-words')...")
        filtrirane_frekvencije = ukloni_stop_words(sve_frekvencije)
        
        # KORAK 5: Sortiraj konačni rječnik i ispiši rezultat.
        print("5. Sortiram i ispisujem konačne rezultate...")
        
        # Demonstracija bonus zadatka:
        # Pozivamo funkciju s argumentom 10 da ispiše top 10 riječi.
        sortiraj_i_ispisi(filtrirane_frekvencije, 10)
        
        # Pozivamo funkciju bez drugog argumenta, pa će ona koristiti zadanu vrijednost (15).
        sortiraj_i_ispisi(filtrirane_frekvencije)
        
    else:
        # Ako tekst nije učitan (funkcija je vratila None), ispisujemo poruku.
        print("Program se prekida jer datoteka nije pronađena.")

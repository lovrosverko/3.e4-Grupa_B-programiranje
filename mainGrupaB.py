# Funkcija za učitavanje teksta iz datoteke
def ucitaj_tekst(filepath):
    try:
        # Kod za otvaranje datoteke ide ovdje
        with open (filepath, 'r', encoding='utf-8') as file:
            sadrzaj = file.read()
        return sadrzaj
    except FileNotFoundError:
        print(f"Greška: Datoteka na putanji '{filepath}' nije pronađena.")
        return None # Vratit ćemo 'ništa' ako datoteka ne postoji

# Funkcija za pročišćavanje teksta
def ocisti_tekst(tekst):
    # Kod za pročišćavanje teksta ide ovdje
    tekst = tekst.lower()
    interpunkcija = ['.', ',', '!', '?', ':', ';', '"', "'", '(', ')']
    for znak in interpunkcija:
        tekst = tekst.replace(znak, '')
    lista_rijeci = tekst.split()
    return lista_rijeci

def broji_rijeci(lista_rijeci):
    #rječnik u koji ćemo spremiti svaku riječ i koliko se puta ta riječ ponovila u tekstu
    brojac_rijeci = {} 
    for rijec in lista_rijeci:
        if rijec in brojac_rijeci:
            brojac_rijeci[rijec] += 1
        else:
            brojac_rijeci[rijec] = 1
    return brojac_rijeci


if __name__ == "__main__":
    filepath = "tekst.txt"
    print(f"Učitavam tekst iz datoteke: {filepath}")
    ucitani_tekst = ucitaj_tekst(filepath)
    if ucitani_tekst:
        print("Učitani tekst je:")
        print(ucitani_tekst)
    else:
        print("Greška pri učitavanju datoteke.")
    
    ucitani_tekst = ocisti_tekst(ucitani_tekst)
    if ucitani_tekst:
        print("Očišćeni tekst je:")
        print(ucitani_tekst)
        #Brojanje riječi i ispis rječnika
        brojac_rijeci = broji_rijeci(ucitani_tekst)
        print ("Broj riječi u teksu: ")
        print(brojac_rijeci)
    else:
        print("Greška pri očišćavanju teksta.")

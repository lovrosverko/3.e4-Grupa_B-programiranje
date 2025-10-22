# -*- coding: utf-8 -*-

"""
Ova datoteka je sažetak i vježba s blok sata ponavljanja (11. i 12. sat).
Cilj je bio utvrditi temeljne koncepte Pythona:
1. Osnovni tipovi podataka
2. Grananje (if-elif-else)
3. Petlje (for i while)

Svaki dio koda ispod je primjer koji smo radili na satu.
"""

# === 1. STUP: OSNOVNI TIPOVI PODATAKA ===

# Python automatski prepoznaje tip podatka kada mu dodijelimo vrijednost.

broj = 10       # int (Integer) - Cijeli broj
ime = "Pero"    # str (String) - Niz znakova (tekst), uvijek unutar navodnika
znak = 'a'      # str (String) - U Pythonu ne postoji poseban tip 'char',
                #                to je samo string duljine 1.
cijena = 10.5   # float - Decimalni broj (broj s pomičnim zarezom)
istina = True   # bool (Boolean) - Logička vrijednost, može biti samo True ili False

# === 2. STUP: GRANANJE (IF-ELIF-ELSE) ===

# Grananje nam omogućuje da program donosi odluke.
# Blok koda koji se izvršava OBAVEZNO mora biti uvučen (indentiran).

if broj > 5:
    # Ovaj blok se izvršava SAMO AKO je uvjet (broj > 5) istinit.
    print("Broj je veći od 5.")
elif broj == 5:
    # "elif" je skraćeno od "else if".
    # Ovaj blok se izvršava SAMO AKO prvi 'if' nije bio istinit,
    # A OVAJ uvjet (broj == 5) JE istinit.
    print("Broj je jednak 5.")
else:
    # "else" (inače) se izvršava SAMO AKO NIJEDAN od prethodnih
    # 'if' ili 'elif' uvjeta nije bio istinit.
    print("Broj nije veći od 5.")

# Možemo provjeravati i boolean (logičke) vrijednosti
if istina: # Ovo je skraćeni način pisanja "if istina == True"
    print("True")
else:
    print("False")


# === ZADATAK 2: GRANANJE U PRAKSI (Temperatura) ===

# Verzija 1: Korisnik prvo unese, pa mi pretvaramo (u dva koraka)
# print("Unesi temeraturu:")
# temperatura = input() # input() UVIJEK vraća string (tekst)
# temperatura = int(temperatura) # int() pretvara string u cijeli broj (integer)

# Verzija 2: Ugniježđeno pozivanje (kraći, čišći način)
# Funkcija int() se izvršava na rezultatu funkcije input()
print("--- Zadatak 2: Temperatura ---")
temperatura = int(input("Unesi temeraturu:"))

if temperatura <= 0:
    # Ako je temp. npr. -5, ovaj uvjet je istinit i program ispisuje "Ledenica".
    # Ostatak (elif, else) se u potpunosti preskače.
    print("Ledenica")
elif temperatura > 0 and temperatura <= 15:
    # Riječ "and" (i) zahtijeva da OBA uvjeta budu istinita.
    # Ako je temp. 10, (10 > 0) je True I (10 <= 15) je True. Cijeli uvjet je True.
    print("Hladno")
elif temperatura > 15 and temperatura <= 25:
    # Ako je temp. 20, (20 > 15) je True I (20 <= 25) je True. Cijeli uvjet je True.
    print("Ugodno")
else:
    # "else" hvata sve ostale slučajeve koji nisu pokriveni.
    # U ovom slučaju, to su svi brojevi veći od 25.
    print("Vruće")


# === 3. STUP: PETLJE (PONAVLJANJE) ===

print("\n--- 3. STUP: PETLJE ---")

# --- FOR PETLJA ---
# Koristimo je kad ZNAMO točan broj ponavljanja
# ili želimo proći kroz sve elemente neke liste/stringa.

# Primjer 1: Korištenje range()
# range(10) stvara niz brojeva od 0 do 9 (ukupno 10 brojeva).
print("FOR petlja s range(10):")
for i in range(10):
    print(i) # Ispisat će brojeve od 0 do 9

# Primjer 2: Prolazak kroz string
print("\nFOR petlja kroz string 'Bok':")
for slovo in "Bok":
    # U prvoj iteraciji, 'slovo' će biti "B", pa "o", pa "k".
    print(slovo)

# --- WHILE PETLJA ---
# Koristimo je kad NE ZNAMO točan broj ponavljanja,
# ali znamo UVJET pod kojim se petlja treba zaustaviti.

print("\nWHILE petlja od 0 do 10:")
brojac = 0 # 1. Inicijalizacija - postavljamo brojač na početnu vrijednost
while brojac < 11: # 2. Uvjet - petlja se vrti SVE DOK je 'brojac' manji od 11
    print(brojac)
    brojac += 1 # 3. Inkrement - NAJVAŽNIJI DIO! Povećavamo brojač.
               # Bez ovoga, 'brojac' bi uvijek bio 0 i petlja bi bila beskonačna!

# === ZADATAK 3: PETLJE U PRAKSI (Parni brojevi) ===

print("\n--- Zadatak 3: Parni brojevi od 2 do 20 ---")

# Rješenje 1: FOR petlja + IF provjera
print("Rješenje 1 (FOR + IF):")
# range(2, 21) ide od 2 do 20 (jer je 21 isključen)
for broj in range(2, 21):
    # Operator % (modulo) daje ostatak cjelobrojnog dijeljenja.
    # Ako je ostatak dijeljenja s 2 jednak 0, broj je paran.
    if broj % 2 == 0:
        print(broj)
    else:
        # "continue" je naredba koja kaže petlji:
        # "Zanemari ostatak koda u ovoj iteraciji i prijeđi na sljedeći broj."
        continue 

# Rješenje 2: Elegantna FOR petlja (korištenje koraka 'step')
print("\nRješenje 2 (FOR sa 'step'):")
# range(start, stop, step)
# Krećemo od 2, stajemo prije 21, idemo u koracima od 2.
for broj in range(2, 21, 2):
    print(broj)

# Rješenje 3: WHILE petlja
print("\nRješenje 3 (WHILE):")
broj = 2 # Krećemo od 2
while broj <= 20: # Vrtimo petlju dok god je broj manji ili jednak 20
    print(broj)
    broj += 2 # Povećavamo broj za 2 u svakom koraku

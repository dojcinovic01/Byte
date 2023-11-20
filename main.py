import copy

# Globalne promenljive za praćenje stekova
stekovi_beli = []
stekovi_crni = []

m: int
n: int
covek: bool


def unesiDim():
    while True:
        s = input("Unesite dimenzije table (format: x,y): ")
        dimensions = s.split(",")

        # Check if the input contains two values
        if len(dimensions) != 2:
            print("Pogresan unos. Unesite ponovo.")
            continue

        try:
            global m, n
            m = int(dimensions[0])
            n = int(dimensions[1])

            # Check if dimensions are either 8x8 or an even number in the range from 8 to 16
            if (m == n) and (m == 8) or (8 <= m <= 16 and 8 <= n <= 16 and m % 2 == 0 and n % 2 == 0):
                return m, n
            else:
                print("Pogresne dimenzije. Unesite ponovo.")
        except ValueError:
            print("Pogresan unos. Unesite ponovo.")


def izborIgraca():
    p = input("Unesite da li igru pocinje covek ili racunar: H/C ")
    if (p == 'C' or p == 'c'):
        return False
    elif (p == 'H' or p == 'h'):
        return True
    else:
        print("Pogresan unos")
        return izborIgraca()


def izborPrvogIgraca():
    p = input("Izaberite ko će igrati prvi (X ili O): ").upper()
    if p == 'X':
        return True  # Čovek igra prvi
    elif p == 'O':
        return False  # Računar igra prvi
    else:
        print("Pogrešan unos. Pokušajte ponovo.")
        return izborPrvogIgraca()


def unosParametaraIgre():
    dimenzije = unesiDim()
    ko_igra_prvi = izborIgraca()
    prvi_igrac = izborPrvogIgraca()
    return dimenzije[0], dimenzije[1], ko_igra_prvi, prvi_igrac


def prikazTabla(tabla, broj_elemenata=7):
    slovo = 'A'  # pocetak prikaza slova
    print("    ", end=" ")  # razmak od pocetka
    for x in range(0, n):
        print(chr(ord(slovo) + x), end="   ")
    print()  # kraj slova, novi red za ===
    print("   ", end=" ")
    for x in range(0, n):
        print("===", end=" ")
    print()  # stampa === pomereno za odredjeni broj mesta i ide u novi red za matricu
    for x in range(0, m - 1):  # obilaze se sve vrste osim poslednje, a prikazuju sve osim prve
        print(m - x, "||", end="")
        for y in range(0, n):
            print(" ", end="")
            # Prikazujte određeni broj elemenata steka na svakom polju
            stek = tabla[m - x - 1][y]['stek']
            if len(stek) <= broj_elemenata:
                content = ''.join(stek)
            else:
                content = ''
                tabla[m - x - 1][y]['stek'] = []
            print(content, "|", end="")
        print("|", m - x)
        print("   ", end=" ")
        for y in range(0, n):
            print("---", end=" ")
        print()
    print(1, "||", end=" ")
    for y in range(0, n - 1):
        # Prikazujte određeni broj elemenata steka na svakom polju
        stek = tabla[0][y]['stek']
        if len(stek) <= broj_elemenata:
            content = ''.join(stek)
        else:
            content = ''
            tabla[0][y]['stek'] = []
        print(content, "|", end=" ")
    # Prikazujte određeni broj elemenata steka na poslednjem polju
    stek = tabla[0][n - 1]['stek']
    if len(stek) <= broj_elemenata:
        last_content = ''.join(stek)
    else:
        last_content = ''
        tabla[0][n - 1]['stek'] = []
    print(last_content, "|", end="")
    print("|", 1)
    # stampa === i slova na dnu
    print("   ", end=" ")
    for x in range(0, n):
        print("===", end=" ")
    print()
    print("    ", end=" ")
    for x in range(0, n):
        print(chr(ord(slovo) + x), end="   ")
    print()









def praznaTabla(dim1, dim2):
    # Inicijalizujte matricu da čuva informacije o steku na svakom polju
    val = [[{'vlasnik': '', 'stek': []} for _ in range(dim2)] for _ in range(dim1)]

    for row in range(1, dim1 - 1):
        # Inicijalizujte matricu da čuva informacije o steku na svakom polju
        val = [[{'vlasnik': '', 'stek': []} for _ in range(dim2)] for _ in range(dim1)]

        for row in range(1, dim1 - 1):
            for col in range(dim2):
                if (row % 2 != 0 and col % 2 == 0) or (row % 2 == 0 and col % 2 != 0):
                    if row % 2 != 0 and col % 2 == 0:
                        val[row][col]['stek'].append('O')  # 'O' in odd rows and even columns
                    elif row % 2 == 0 and col % 2 != 0:
                        val[row][col]['stek'].append('X')  # 'X' in even rows and odd columns

        return val


def sledecePolje(row, col, smer):
    if smer == 'GL':
        return row, col - 1
    elif smer == 'GD':
        return row, col + 1
    elif smer == 'DL':
        return row + 1, col
    elif smer == 'DD':
        return row - 1, col


def dozvoljenPotez(tabla, row, col, mesto, smer,igrac):
    # Provera da li je polje na koje se potez odnosi prazno
    if not tabla[row][col]['stek']:
        return False

    # Provera da li je figura najniža na steku
    if not tabla[row][col]['stek'] or int(tabla[row][col]['stek'][0]) != 1:
        return False

    # Provera da li je smer ispravan
    if (smer == 'GL' and col == 0) or (smer == 'GD' and col == n - 1) or \
            (smer == 'DL' and row == m - 1) or (smer == 'DD' and row == 0):
        return False

    # Provera da li je ciljano polje prazno
    cilj_row, cilj_col = sledecePolje(row, col, smer)
    if cilj_row < 0 or cilj_row >= m or cilj_col < 0 or cilj_col >= n or tabla[cilj_row][cilj_col]['stek']:
        return False

    if igrac == 'X' and tabla[row][col]['vlasnik'] != 'X':
        print("Možete pomerati samo figure koje pripadaju igraču 'X'.")
        return False

    return True


def izvrsiPotez(tabla, row, col, mesto, smer, igrac):
    cilj_row, cilj_col = sledecePolje(row, col, smer)

    # Provera dodatnih uslova za poteze
    if not dozvoljenPotez(tabla, row, col, mesto, smer,igrac):
        return tabla, None

    # Ažuriranje steka sa trenutnog polja
    figura = tabla[row][col]['stek'].pop()

    # Ažuriranje vlasnika steka na trenutnom polju
    tabla[row][col]['vlasnik'] = tabla[row][col]['stek'][-1] if tabla[row][col]['stek'] else ''

    # Ažuriranje steka na ciljnom polju
    tabla[cilj_row][cilj_col]['stek'] += [figura]

    # Ažuriranje vlasnika steka na ciljnom polju
    tabla[cilj_row][cilj_col]['vlasnik'] = figura

    # Ako je potez diagonalan, ukloni figuru sa startnog polja
    if cilj_row != row or cilj_col != col:
        tabla[row][col]['stek'] = tabla[row][col]['stek'][:-1]

    # Ažuriranje rezultujućeg steka
    rezultujuci_stek = tabla[cilj_row][cilj_col]['stek']
    if len(rezultujuci_stek) > 8:
        # Ako rezultujući stek ima više od 8 figura, odseči višak
        tabla[cilj_row][cilj_col]['stek'] = rezultujuci_stek[:8]

    return tabla, tabla[cilj_row][cilj_col]['vlasnik']


def proveriPobednika():
    global stekovi_beli, stekovi_crni

    # Brojanje stekova po boji
    broj_stekova_beli = len(set(stek[0] for stek in stekovi_beli))
    broj_stekova_crni = len(set(stek[0] for stek in stekovi_crni))

    # Prikazivanje trenutnog stanja
    print(f"Belih stekova: {broj_stekova_beli}")
    print(f"Crnih stekova: {broj_stekova_crni}")

    # Provera da li je neki igrač pobednik
    if broj_stekova_beli > len(stekovi_beli) / 2:
        return 'O'
    elif broj_stekova_crni > len(stekovi_crni) / 2:
        return 'X'
    else:
        return None

def potez_X(tabla, row, col):
        # Implement the logic for player 'X' move
        tabla[row][col]['stek'].append('X')

def potez_O(tabla, row, col):
        # Implement the logic for player 'O' move
        tabla[row][col]['stek'].append('O')

        def unosPoteza():
            while True:
                try:
                    potez = input("Unesite potez (npr. A3 2 GL): ").split()
                    if len(potez) != 3:
                        print("Pogrešan unos. Pokušajte ponovo.")
                        continue

                    pozicija = potez[0]
                    mesto = int(potez[1])
                    smer = potez[2].upper()

                    # Provera ispravnosti unosa
                    if len(pozicija) != 2 or not pozicija[0].isalpha() or not pozicija[1].isdigit():
                        print("Pogrešan unos pozicije. Pokušajte ponovo.")
                        continue

                    row = m - int(pozicija[1])
                    col = ord(pozicija[0].upper()) - ord('A')

                    if not (1 <= mesto <= 8) or smer not in ['GL', 'GD', 'DL', 'DD']:
                        print("Pogrešan unos mesta ili smera. Pokušajte ponovo.")
                        continue

                    return row, col, mesto, smer
                except ValueError:
                    print("Pogrešan unos. Pokušajte ponovo.")

        def izvrsiPotezIgraca(tabla, igrac):
            row, col, mesto, smer = unosPoteza()

            if dozvoljenPotez(tabla, row, col, mesto, smer, igrac):
                tabla, _ = izvrsiPotez(tabla, row, col, mesto, smer)
                prikazTabla(tabla)

        # Primer poziva za igraca 'X'
       


m, n, ko_igra_prvi, prvi_igrac = unosParametaraIgre()
tabla = praznaTabla(m, n)
potez_X(tabla,2,3)
potez_X(tabla,1,0)
potez_X(tabla,1,4)
potez_O(tabla,1,4)
potez_O(tabla,1,4)
potez_O(tabla,1,4)





prikazTabla(tabla)


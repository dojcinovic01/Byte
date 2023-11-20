import copy
from math import sqrt

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
    return dimenzije[0], dimenzije[1], ko_igra_prvi ,prvi_igrac

def prikazTabla(tabla):
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
            # Limit the number of 'X' or 'O' characters to a maximum of 8
            content = tabla[m - x - 1][y][:8]
            print(content, "|", end="")
        print("|", m - x)
        print("   ", end=" ")
        for y in range(0, n):
            print("---", end=" ")
        print()
    print(1, "||", end=" ")
    for y in range(0, n - 1):
        # Limit the number of 'X' or 'O' characters to a maximum of 8
        content = tabla[0][y][:8]
        print(content, "|", end=" ")
    # Limit the number of 'X' or 'O' characters to a maximum of 8
    last_content = tabla[0][n - 1][:8]
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
    val = [[' ' for _ in range(dim2)] for _ in range(dim1)]

    for row in range(1, dim1-1):
        for col in range(dim2):
            if (row % 2 == 0 and col % 2 == 0) or (row % 2 != 0 and col % 2 != 0):
                if row % 2 != 0 and col % 2 != 0:
                    val[row][col] = 'O'  # 'X' in even rows and even columns
                elif row % 2 == 0 and col % 2 == 0:
                    val[row][col] = 'X'  # 'O' in odd rows and odd columns

    return val


m, n, ko_igra_prvi,prvi_igrac = unosParametaraIgre()

tabla = praznaTabla(m, n)
prikazTabla(tabla)

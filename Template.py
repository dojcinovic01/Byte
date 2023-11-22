import turtle
import tkinter as tk
from tkinter import messagebox

scr = turtle.Screen()
ttl = turtle.Turtle()
ttlDots = turtle.Turtle()

listaPolja = []
m: int
n: int


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
    p = input("Unesite da li igru želite da igrate sa čovekom(H) ili računarom(C):")
    if (p == 'C' or p == 'c'):
        return False
    elif (p == 'H' or p == 'h'):
        return True
    else:
        print("Pogresan unos")
        return izborIgraca()


def izborPrvogIgraca():
    p = input("Izaberite ko će igrati prvi (1-CRNI ili 0-BELI): ")
    if (p == '1'):
        return True  # Čovek igra prvi
    elif (p == '0'):
        return False  # Računar igra prvi
    else:
        print("Pogrešan unos. Pokušajte ponovo.")
        return izborPrvogIgraca()


def unosParametaraIgre():
    dimenzije = unesiDim()
    ko_igra_prvi = izborIgraca()
    prvi_igrac = izborPrvogIgraca()
    return dimenzije[0], dimenzije[1], ko_igra_prvi, prvi_igrac


def draw():
    for i in range(4):
        ttl.forward(45)
        ttl.left(90)
    ttl.forward(45)


def drawInitialDots(size: int):
    for j in range(size):
        for k in range(size):
            sredina_x = -size * 45 / 2 + (k + 0.5) * 45
            # Invertovanje y koordinate
            sredina_y = size * 45 / 2 - (j - 0.5) * 45
            ttlDots.penup()
            ttlDots.goto(sredina_x, sredina_y)
            ttlDots.pendown()

            if (j > 0 and j < size-1 and (j+k) % 2 == 0):
                if (j % 2 != 0):
                    polje = {'row': chr(ord('A') + j), 'column': k,
                             'vlasnik': 'crni', 'stek': [1]}
                    listaPolja.append(polje)
                    ttlDots.dot(5, 'black')
                else:
                    polje = {'row': chr(ord('A') + j), 'column': k,
                             'vlasnik': 'beli', 'stek': [0]}
                    listaPolja.append(polje)
                    ttlDots.dot(5, 'orange')
            else:
                listaPolja.append(
                    {'row': chr(ord('A') + j), 'column': k, 'vlasnik': '', 'stek': []})


def drawField(polje: dict):
    for ind, dot in enumerate(polje['stek']):
        j = ord(polje['row'])-65
        k = polje['column']
        coefK = 0
        coefY = 0
        if (len(polje['stek']) == 1):
            coefK = 0.5
            coefY = 0.5
        else:
            if (ind == 0 or ind == 3 or ind == 6):
                coefK = 0.1
            elif (ind == 1 or ind == 4 or ind == 7):
                coefK = 0.5
            else:
                coefK = 0.9

            if (0 <= ind <= 2):
                coefY = 0.1
            elif (3 <= ind <= 5):
                coefY = 0.5
            else:
                coefY = 0.9
        x = -8 * 45 / 2 + (k + coefK) * 45
        y = 8 * 45 / 2 - (j - coefY) * 45
        if dot == 0:
            ttlDots.penup()
            ttlDots.goto(x, y)
            ttlDots.pendown()
            ttlDots.dot(5, 'orange')
        elif dot == 1:
            ttlDots.penup()
            ttlDots.goto(x, y)
            ttlDots.pendown()
            ttlDots.dot(5, 'black')
        else:
            continue


def drawDots():
    ttlDots.clear()
    for polje in listaPolja:
        drawField(polje)


def drawBoard(size: int):
    scr.setup(size * 75 + 20, size * 75 + 20)

    ttl.speed(90)

    # Oznake za redove (A, B, C, ...)
    row_labels = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")[:size]
    for i, label in enumerate(row_labels):
        ttl.penup()
        ttl.goto(-size * 45 / 2 - 20, size * 45 / 2 - i * 45 + 10)
        ttl.write(label, align="center", font=("Arial", 12, "normal"))

    # Oznake za kolone (1, 2, 3, ...)
    for i in range(size):
        ttl.penup()
        ttl.goto(-size * 45 / 2 + i * 45 + 25, size * 45 / 2 + 60)
        ttl.write(str(i + 1), align="center", font=("Arial", 12, "normal"))

    for j in range(size):
        ttl.up()
        ttl.setpos(-size * 45 / 2, size * 45 / 2 - j * 45)
        ttl.down()

        for k in range(size):
            if (j + k) % 2 == 0:
                clr = 'brown'
            else:
                clr = 'white'

            ttl.fillcolor(clr)
            ttl.begin_fill()
            draw()
            ttl.end_fill()

    drawInitialDots(size)


def vratiPolje(row, column):
    for polje in listaPolja:
        if polje['row'] == row and polje['column'] == column:
            return polje


if __name__ == "__main__":
    # m, n, ko_igra_prvi, prvi_igrac = unosParametaraIgre()
    drawBoard(8)
    polje = vratiPolje('A', 1)
    polje['stek'] = [0, 1, 1, 0, 1, 1, 1]
    drawDots()
    ttl.hideturtle()
    turtle.done()

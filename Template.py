import turtle
import tkinter as tk
from tkinter import messagebox

scr = turtle.Screen()
ttl = turtle.Turtle()

listaPolja = []


def draw():
    for i in range(4):
        ttl.forward(35)
        ttl.left(90)
    ttl.forward(35)


def drawDots(size: int):
    for j in range(size):
        for k in range(size):
            sredina_x = -size * 35 / 2 + (k + 0.5) * 35
            sredina_y = -size * 35 / 2 + (j + 0.5) * 35
            ttl.penup()
            ttl.goto(sredina_x, sredina_y)
            ttl.pendown()

            if (j > 0 and j < size-1 and (j+k) % 2 != 0):
                if (j % 2 == 0):
                    stack = [1]
                    listaPolja.append(stack)
                    ttl.dot(5, 'black')
                else:
                    stack = [0]
                    listaPolja.append(stack)
                    ttl.dot(5, 'white')
            else:
                listaPolja.append([])


def drawBoard(size: int):
    if size > 16:
        tk.Tk().withdraw()
        messagebox.showinfo("Greška", "Veličina table ne sme biti veća od 16.")
        return

    scr.setup(size * 35 + 20, size * 35 + 20)

    ttl.speed(90)

    # Oznake za redove (A, B, C, ...)
    row_labels = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")[:size]
    for i, label in enumerate(row_labels):
        ttl.penup()
        ttl.goto(-size * 35 / 2 - 20, -size * 35 / 2 + i * 35 + 15)
        ttl.write(label, align="center", font=("Arial", 12, "normal"))

    # Oznake za kolone (1, 2, 3, ...)
    for i in range(size):
        ttl.penup()
        ttl.goto(-size * 35 / 2 + i * 35 + 15, -size * 35 / 2 - 20)
        ttl.write(str(i + 1), align="center", font=("Arial", 12, "normal"))

    for j in range(size):
        ttl.up()
        ttl.setpos(-size * 35 / 2, -size * 35 / 2 + j * 35)
        ttl.down()

        for k in range(size):
            if (j + k) % 2 == 0:
                clr = 'white'
            else:
                clr = 'brown'

            ttl.fillcolor(clr)
            ttl.begin_fill()
            draw()
            ttl.end_fill()

    drawDots(size)
    ttl.hideturtle()
    turtle.done()


if __name__ == "__main__":
    drawBoard(12)

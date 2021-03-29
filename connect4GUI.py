import tkinter as tk
from tkinter import *
from connect4 import Connect4
from board import Colors
import time
ROWS = 6
COLS = 7

r = tk.Tk() 
game = Connect4()
m = Label(r, text = 'Welcome! Its reds turn',  width = 20)
m.grid(row = 0, column = 8)
color = Colors.Red

def onClick(idx):
    global color
    global m
    game.turn(color, idx)
    
    for rows in range(ROWS):
        for cols in range(COLS):
            currColor = game.game.getColor(rows, cols)
            if currColor == Colors.Red:
                lb = Listbox(r, width = 20, height = 9, bg = 'red')
                lb.grid(row = rows + 1, column = cols + 1)
            elif currColor == Colors.Black:
                lb = Listbox(r, width = 20, height = 9, bg = 'black')
                lb.grid(row = rows + 1, column = cols + 1)

    if game.game.seeIfWinner() :
        m.configure(text = '%s wins!' % color)
        for i in range(7):
            b = tk.Button(r, text = 'Column %s' % (i + 1))
            b.grid(row = 0, column = i + 1)
            
        return
    if color == Colors.Red:
        color = Colors.Black       
        m.configure(text = 'It is blacks turn %s' % game.game.seeIfWinner())
    else:
        color = Colors.Red
        m.configure(text = 'It is reds turn')
        

def graphics():   
    r.title('Connect Four') 
    
    for i in range(7):
        b = tk.Button(r, text = 'Column %s' % (i + 1), command = lambda idx = i: onClick(idx))
        b.grid(row = 0, column = i + 1)        
    for rows in range(ROWS):
        for cols in range(COLS):
            lb = Listbox(r, width = 20, height = 9, bg = 'white')
            lb.grid(row = rows + 1, column = cols + 1)

    r.mainloop() 

graphics()
 

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 23:13:24 2022

@author: salva

GAME OF LIFE
The game of life rules for a finite board (20x20):

general rules:
1: Any live cell with two or three live neighbors survives.
2: Any dead cell with three live neighbors becomes a live cell.
3: All other live cells die in the next generation. Similarly,
all other dead cells stay dead.

corner rules:
1: Any live cell with any live neighbors survives.
2: Any dead cell with any live neighbors becomes a live cell.
3. Any live cell without any live neighbors dies

edge rules:
1: Any live cell with one or two live neighbors survives.
2: Any dead cell with two or three live neighbors becomes a live
cell.
3. Any live cell without any live neighbors dies
4. Any live cell with three or more live neighbors dies
 
"""


import numpy as np
import random as rn
import os
import time

ROWS    = os.get_terminal_size().lines - 1
COLUMNS = os.get_terminal_size().columns
ALIVE   = 1
DEAD    = 0

def aliveNeightbors(row,col):
 
    
    row_begin = (row-1) if (row-1) >= 0 else 0
    row_end   = (row+2) if (row+2) < ROWS else ROWS
   
    col_begin = (col-1) if (col-1) >= 0 else 0
    col_end   = (col+2) if (col+2) < COLUMNS else COLUMNS

    alive_neighbors = (np.sum(board[row_begin:row_end, col_begin:col_end])
                      - board[row, col])
   
    return alive_neighbors

def outputBoard():
   
    os.system('cls')
    for row in range(ROWS):
        for col in range(COLUMNS):
            print('#' if board[row, col] == ALIVE else ' ', end='')
        print('')

#Populates first board with random values     
board = np.random.choice([0, 1], p=[0.6, 0.4], size=(ROWS, COLUMNS))            
outputBoard()
time.sleep(1)

#Main
while True:
    tempBoard = np.zeros((ROWS, COLUMNS), dtype=int) # board
    for row in range(ROWS):
        for col in range(COLUMNS):
            alive_neighbors = aliveNeightbors(row, col)
            if ((board[row, col] == ALIVE and alive_neighbors in (2, 3)) 
            or (board[row, col] == DEAD and alive_neighbors == 3)):
                tempBoard[row, col] = ALIVE
            else:
                tempBoard[row, col] = DEAD            
   
    board = tempBoard.copy()
    outputBoard()
    time.sleep(0.1)
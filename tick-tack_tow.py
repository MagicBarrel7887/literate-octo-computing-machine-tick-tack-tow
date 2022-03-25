# The function draws the computer's move and updates the board.
from distutils.log import error
from pickle import FALSE
import re

"""
Provides some tick-tack_tow

"""

temps = ''

borad = [['1','2','3'], ['4','x','o'], ['7','8','9']]

def display_data():
    """Provides some tick-tack_tow"""
    for i in range(0,3):
        print('+-------+-------+-------+')
        print('|   ' + borad[i][0] + '   |   ' + borad[i][1] + '   |    ' + borad[i][2] + '  |')
        print('+-------+-------+-------+')


def enter_move():
    """ The function accepts the board's current status, asks the user about their move, checks the input, and updates the board according to the user's decision. """
    
    
    try:
      move = int(input("Please enter a number in the board "))
      print(move)
      
      try:
        if move < 1 or move > 9:
            for x in range(0, 3):
                for y in range(0, 2):
                    temp = isinstance(borad[x][y], int)
                    temps = temp
                    print(temp, " ",x,":",y)
                    
                    if temp is False:
                     print("Please enter a valed number in the board")
                     print(temp)
                     return False
                       
      except Exception as e:
       print('loop search exception occurred', end="\n")
       print(e)
        
        
       try:
         for x in range(0, 3):
            for y in range(0, 2):
                if borad[x][y] == move:
                    
       except Exception as e:
       print('An exception occurred')
       print(e)
      
    except Exception as e:
      print('An exception occurred')
      print(e)
    
    
    print()



def make_list_of_free_fields():
    """ The function browses the board and builds a list of all the free squares the list consists of tuples, while each tuple is a pair of row and column numbers."""
    print()


def victory_for(board, sign):
    """ The function analyzes the board's status in order to check if the player using 'O's or 'X's has won the game"""
    print()


def draw_move(board):
    """ The function draws the computer's move and updates the board."""
    print()


while True:
    display_data()
    enter_move()
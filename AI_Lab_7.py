#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random
import itertools


# In[2]:


def isWin(box):
    # iterating rows
    for i in range(3):
        if box[i, 0] == box[i, 1] == box[i, 2] != ' ':
            return True

    # iterating columns
    for i in range(3):
        if box[0, i] == box[1, i] == box[2, i] != ' ':
            return True

    # iterating diagonals
    if box[0, 0] == box[1, 1] == box[2, 2] != ' ':
        return True

    if box[0, 2] == box[1, 1] == box[2, 0] != ' ':
        return True

    return False


# In[3]:


singleListStates = list(itertools.product(['X', 'O', ' '], repeat=9))
states = []


# In[4]:


for state in singleListStates:
    array = np.array(state).reshape((3, 3))
    if state.count(' ') == 0 or isWin(array) == True:
        continue
    if state.count('X') == state.count('O') or state.count('X') == state.count('O')+1:
        states.append(np.matrix(array))


# In[5]:


colors = [['WHITE', 'LILAC', 'SILVER'], ['BLACK', 'GOLD', 'GREEN'], ['AMBER', 'RED', 'PINK']]
indexPositions = {'WHITE': [0, 0], 'LILAC': [0, 1], 'SILVER': [0, 2], 'BLACK': [1, 0], 'GOLD': [1, 1], 'GREEN': [1, 2], 'AMBER': [2, 0], 'RED': [2, 1], 'PINK':[2,2]}
beadsState = {}


# In[9]:


for index, state in enumerate(states):
    currBeads = {}
    for i in range(3):
        for j in range(3):
            if state[i,j] == ' ':
                currBeads[colors[i][j]] = 1
    beadsState[index] = currBeads
def trainMenace():
    iterations = 100
    for iterVal in range(iterations):
        
        board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        board = np.matrix(np.array(board))
        while True:
            index = -1
            for Index, state in enumerate(states):
                if np.array_equal(board, state):
                    index = Index
                    break
            color_dict = beadsState[index]
            total_value = sum(color_dict.values())
            probs = [color_dict[color] / total_value for color in color_dict]
            color = random.choices(list(color_dict.keys()), weights=probs)[0]
            currIndex = indexPositions[color]
            board[currIndex[0], currIndex[1]] = 'X'
    
            if isWin(board) == True:
                
                beadsState[index][color] += 3
                print(beadsState[index])
                break
                
            number = 0
            for i in range(3):
                for j in range(3):
                    if board[i, j] != ' ':
                        number+=1
            
            if number == 9:
                
                break
            
            indicesFree = []
            for i in range(3):
                for j  in range(3):
                    if board[i, j] == ' ':
                        indicesFree.append([i ,j])
                        
          
            randomIndex = random.randint(0, len(indicesFree) - 1)
                
            currIndex = indicesFree[randomIndex]
            board[currIndex[0], currIndex[1]] = 'O'
            
            if isWin(board) == True:
                beadsState[index][color] -= 3
                print(beadsState[index])
                if beadsState[index][color] < 0:
                    beadsState[index][color] = 0
                break
            
            number = 0
            for i in range(3):
                for j in range(3):
                    if board[i, j] != ' ':
                        number+=1
            if number == 9:
                break
trainMenace()


# In[ ]:


def playGame():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    board = np.matrix(np.array(board))
    while True:
        index = -1
        for Index, state in enumerate(states):
            if np.array_equal(board, state):
                index = Index
                break
        print(beadsState[index])
        color_dict = beadsState[index]
        total_value = sum(color_dict.values())
        probs = [color_dict[color] / total_value for color in color_dict]

        color = random.choices(list(color_dict.keys()), weights=probs)[0]
        currIndex = indexPositions[color]
            
        board[currIndex[0], currIndex[1]] = 'X'
        
        if isWin(board.copy()) == True:
            print("The game won by AI")
            break
                
        number = 0
        for i in range(3):
            for j in range(3):
                if board[i, j] != ' ':
                    number+=1
            
        if number == 9:
            print("The game is draw")    
            break
        
        print("The board is in configuration :- \n", board)
        
        while True:
            rowNumber = int(input("Enter the row number where you need to place a bead (0-2): "))
            columnNumber = int(input("Enter the column number where you need to place a bead (0-2): "))
            
            if rowNumber > 2 or rowNumber < 0:
                print("Enter a valid row number")
                continue
        
            if columnNumber > 2 or columnNumber < 0:
                print("Enter a valid column number")
                continue
                
            if board[rowNumber, columnNumber] != ' ':
                print("That position is already occupied")
                continue
                
            board[rowNumber, columnNumber] = 'O'
            break
            
        if isWin(board.copy()) == True:
            print("You won the game")
            break
                
        number = 0
        for i in range(3):
            for j in range(3):
                if board[i, j] != ' ':
                    number+=1
            
        if number == 9:
            print("It is a draw")    
            break
playGame()


# In[ ]:





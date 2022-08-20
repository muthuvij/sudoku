from django.shortcuts import render, redirect

from django.http import HttpResponse

from .forms import *

from .models import Sudoko

import random

def find_value(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j]==0:
                return (i,j)
    return None

def valid_or_not(bo,pos,num):
    for i in range(len(bo[0])):
        if bo[pos[0]][i]==num and (pos[0],i)!=pos:
            return False
    for i in range(9):
        if bo[i][pos[1]]==num and i!=pos[0]:
            return False
    #print((pos[0]//3*3,pos[0]//3*3+3),(pos[1]//3*3,pos[1]//3*3+3))
    for i in range(pos[0]//3*3,pos[0]//3*3+3):
        for j in range(pos[1]//3*3,pos[1]//3*3+3):
            #print(i,j)
            if bo[i][j]==num and (i,j)!=pos:
                #print(pos)
                return False
    return True

def solve(bo):
    pos=find_value(bo)
    if pos==None:
        return True
    else:
        for i in range(1,10):
            if valid_or_not(bo,pos,i):
                bo[pos[0]][pos[1]]=i
                if solve(bo):
                    return True
                bo[pos[0]][pos[1]]=0
    return False

def validate(bo, pos, num):
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and (pos[0], i) != pos:
            return False
    for i in range(9):
        if bo[i][pos[1]] == num and i != pos[0]:
            return False
    for i in range(pos[0] // 3 * 3, pos[0] // 3 * 3 + 3):
        for j in range(pos[1] // 3 * 3, pos[1] // 3 * 3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True

def valid(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if validate(bo, (i, j), bo[i][j]) != True:
                return False
    return True

def find_wrong(bo, miss):
    new_bo = []
    for i in range(len(bo)):
        rows = []
        for j in range(len(bo[0])):
            if validate(bo, (i, j), bo[i][j]) == False and (i,j) in miss:
                rows.append(bo[i][j] + 10)
            else:
                rows.append(bo[i][j])
        new_bo += [rows]
        
    return new_bo


global bo
global all_bo

all_bo = [
    [[2,0,0,0,0,1,0,6,0],
     [9,0,4,0,0,0,0,5,0],
     [0,1,3,5,0,0,0,0,0],
     [0,7,0,0,0,0,0,0,0],
     [4,0,9,7,6,0,0,1,0],
     [0,0,1,9,2,0,4,0,0],
     [0,3,0,0,0,0,0,0,0],
     [7,0,0,0,9,0,8,2,0],
     [0,0,0,2,0,0,3,7,5]],
    
    [[5,3,0,0,7,0,0,0,0],
     [6,0,0,1,9,5,0,0,0],
     [0,9,8,0,0,0,0,6,0],
     [8,0,0,0,6,0,0,0,3],
     [4,0,0,8,0,3,0,0,1],
     [7,0,0,0,2,0,0,0,6],
     [0,6,0,0,0,0,2,8,0],
     [0,0,0,4,1,9,0,0,5],
     [0,0,0,0,8,0,0,7,9]],

    [[8,0,6,0,1,0,0,0,0],
     [0,0,3,0,6,4,0,9,0],
     [9,0,0,0,0,0,8,1,6],
     [0,8,0,3,9,6,0,0,0],
     [7,0,2,0,4,0,3,0,9],
     [0,0,0,5,7,2,0,8,0],
     [5,2,1,0,0,0,0,0,4],
     [0,3,0,7,5,0,2,0,0],
     [0,0,0,0,2,0,1,0,5]],

    [[0,0,4,0,5,0,0,0,0],
     [9,0,0,7,3,4,6,0,0],
     [0,0,3,0,2,1,0,4,9],
     [0,3,5,0,9,0,4,8,0],
     [0,9,0,0,0,0,0,3,0],
     [0,7,6,0,1,0,9,2,0],
     [3,1,0,9,7,0,2,0,0],
     [0,0,9,1,8,2,0,0,3],
     [0,0,0,0,6,0,1,0,0]],

    [[0,0,6,7,0,4,9,0,0],
     [0,5,0,0,6,0,0,8,0],
     [2,0,0,0,0,0,0,0,5],
     [3,0,0,0,0,0,0,0,1],
     [1,0,0,0,0,0,0,0,2],
     [0,8,0,0,0,0,0,3,0],
     [0,0,7,0,0,0,6,0,0],
     [0,0,0,3,0,9,0,0,0],
     [0,0,0,0,8,0,0,0,0]]
]

bo = random.choice(all_bo)

global miss

miss = []

for i in range(len(bo)):
    for j in range(len(bo[0])):
        if bo[i][j] == 0:
            miss.append((i,j))

def sudoko_view(request):

    global bo
    global miss
    global all_bo
    
    bo = random.choice(all_bo)

    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if (i, j) in miss:
                bo[i][j] = 0

    if request.method == 'POST':
        answers = request.POST.getlist('answer')
        for i in range(len(bo)):
            for j in range(len(bo[0])):
                if bo[i][j] == 0:
                    try:
                        bo[i][j] = int(answers[0])
                    except:
                        pass
                    answers.pop(0)
                    

        if valid(bo) == True:
            return redirect('../sudoko_complete/')
        else:
            return redirect('wrong/')
    
    context = {
        'board' : bo,
        'missing' : miss
        }

    return render(request, 'templates/game.html', context)




def completed_view(request):
    
    global bo
    global miss

    bo1 = bo
    for i, j in miss:
        bo1[i][j] += 10
    
    context = {
        'board' : bo1
        }

    return render(request, 'templates/complete.html', context)



def sudoko_wrong_view(request):

    global bo
    global miss

    new_bo = find_wrong(bo, miss)

    if request.method == 'POST':
        
        for i, j in miss:
            bo[i][j] = 0
            
        return redirect('../')

    context = {
        'board' : new_bo
        }
    
    return render(request, 'templates/wrong.html', context)



def answer_view(request):

    global bo

    answer_board = bo
    solvable = solve(answer_board)

    if request.method == 'POST':
        return redirect('../')

    context = {
        'board' : answer_board
        }

    if solvable == True:
        return render(request, 'templates/answer.html', context)
    else:
        return render(request, 'templates/no_answer.html', context)

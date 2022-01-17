## Sudoku Template Generator (General)
## Author: Siddhant Mahajan
## Date: 5th May, 2021

## This codes takes in a dimension and creates a randomized sudoku puzzle
## template of that dimension where each missing number is represented by
## a 0.


## MODULES
import numpy as np
from random import randint


## FUNCTIONS

## Transforms the root into subsequent sibling root
def transform(root,i):
    if(i==0):
        return root
    else:
        return (transform (root[1:]+ root[0:1], i-1))

#switches rows
def switch_row(r1,r2,npar):
    temp=npar[r1]
    npar[r1]=npar[r2]
    npar[r2]=temp
    return npar

#switches columns
def switch_column(r1,r2,npar):
    temp= np.asarray(npar)
    temp[:,[r1,r2]]=temp[:,[r2,r1]]
    return np.ndarray.tolist(temp)

# Returns a copy of the puzzle after augmentation
def augment(r,c,puzzle):
    temp=list(puzzle)
    temp[r][c]=0
    return temp

#creates a random template from the parent
def switches(template):
    for i in range(dim):
        x=randint(0,dim-1)
        y=randint(0,dim-1)
        while(x==y):
            y=randint(0,dim-1)
        template=switch_row(x,y,template)
        x=randint(0,dim-1)
        y=randint(0,dim-1)
        while(x==y):
            y=randint(0,dim-1)
        template=switch_column(x,y,template)
    return template
        

#final removal
def remove(num,template):
    arr=[]
    while(len(arr)!=num):
        x= randint(0,(dim**2)-1)
        try:
            y=arr.index(x)
            continue
        except:
            arr.append(x)

    for i in arr:
        r=i//dim
        c=i%dim
        template= augment(r,c,template)

    return template

# prints out in readable format
def print_out(result):
    for i in result:
        for j in i:
            print(j, end=" ")
        print("")


## MAIN
        
#data collection(input)
dim=int(input("Enter Dimension to generate sudoku: "))

#variables
parent=[]
root = [i for i in range(1,dim+1)]
parent = [transform(root,i) for i in range(dim)]

#randomizer data
low_on_remove = dim
high_on_remove = (dim**2)-dim
to_remove= randint(low_on_remove,high_on_remove)

#execution
randomized=switches(parent)
print_out(remove(to_remove,randomized))



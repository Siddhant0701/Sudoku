## Sudoku Solver v2.0
## Author: Siddhant Mahajan
## Date: 6th May, 2021

## This code takes in a  n^2 by n^2 sudoku puzzle where all missing numbers are
## replaced with 0's and produces a possible solution to the puzzle.

## MODULES
from math import sqrt


## FUNCTIONS

# Returns the unusable numbers for a specific position
def unusable(r,c,puzzle):
    my_list=[]
    for n,i in enumerate(puzzle[r]):
        if (i > 0 and n!= c):
            my_list.append(i)

    for n,i in enumerate(puzzle):
        if (i[c]>0 and n!= r):
            my_list.append(i[c])

    for i in range((r//small_len)*small_len, ((r//small_len)*small_len)+small_len):
        for j in range((c//small_len)*small_len, ((c//small_len)*small_len)+small_len):
            if(((i!=r) or (j!=c)) and (puzzle[i][j] > 0)):
                my_list.append(puzzle[i][j])

    return (my_list)


# Returns to usable numbers for a specific position
def usable (r,c,puzzle):
    my_list= [i for i in range(1,length+1)]
    unusable_list = unusable(r,c,puzzle)
    return list((set(my_list)).difference(set(unusable_list)))



# Checks if a valid solution was found
def valid(puzzle):
    parent=[i for i in range(1,length+1)]
    if(len(puzzle)==0):
        return False
    
    for i in puzzle:
        if(sorted(i)!=parent):
            return False
        
    for i in zip(*puzzle):
        if(sorted(i)!=parent):
            return False

    for i in range(small_len):
        for j in range(small_len):
            temp=[]
            for k in range(small_len):
                for l in range(small_len):
                    temp.append(puzzle[i*small_len+k][j*small_len+l])
            if(sorted(temp)!=parent):
                return False
            
    return True
    
    

#Returns a list of locations of all spaces that need to be filled
def all_to_fill(puzzle):
    array=[]

    for i in range(length):
        for j in range(length):
            if (puzzle[i][j]==0):
                array.append([i,j])
    return array

# Returns a copy of the puzzle after augmentation
def augment(r,c,val,puzzle):
    temp=list(puzzle)
    temp[r][c]=val
    return temp

## Restores inital values
def restore(puzzle,need):
    copy=list(puzzle)
    for i in need:
        copy[i[0]][i[1]]=0
    return copy

# Fills the empty spaces recursively
def fill(need,puzzle):
    allowed=usable(need[0][0],need[0][1],puzzle)

    if(len(need)==1):
        for val in allowed:
            res=augment(need[0][0],need[0][1],val,puzzle)
            if(valid(res)):
                return res
        return []

    else:
        for val in allowed:
            temp=augment(need[0][0],need[0][1],val,puzzle)
            x=possible(need[1:],temp)
            if(x[0]):
                return x[1]
            temp=restore(temp,need[1:])
        return []


# Mutually recursive function
def possible(need,puzzle):
    x=fill(need,puzzle)
    if(len(x)==0):
        return [False,x]
    else:
        return [True,x]
                


# prints out in readable format
def print_out(res):
    for i in res:
        for j in i:
            print(j, end=" ")
        print("")


## MAIN
        
#variables
sudoku=[]
result=[]
length = int(input("Enter dimension: "))
small_len = int(sqrt(length))

#input collection
for i in range(length):
    a=input().split()
    a= list(map(int,a))
    sudoku.append(a)

#execution code
needed=all_to_fill(sudoku)
result= fill(needed,sudoku) 
print("\nA possible solution is")
print_out(result)

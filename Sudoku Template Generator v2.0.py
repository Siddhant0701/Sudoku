## Sudoku Template Generator v2.0
## Author: Siddhant Mahajan
## Date: 8th May, 2021

## This code generates a template for a sudoku puzzle of a input dimension
## where all missing numbers are 0's. The scramble is determined from
## the conducted research.

## NOTE: UNFINISHED VERSION - REFER TO v2.5 

## MODULES
from math import sqrt

## FUNCTIONS

# Makes a parent puzzle for a given sub-dimension
def make_parent(dim):
    base=[[i for i in range(1,dim**2+1)]]
    for i in range(dim-1):
        base.append(row_change(base[i],dim))

    return col_change(base,dim)

# Helper to the parent generator
def row_change(arr,dim):
    return (arr[dim:] + arr[:dim])

# Helper to the parent generator
def col_change(arr,dim):
    for i in range(dim-1):
        for j in range(dim):
            arr.append(col_helper(arr[i*dim+j],dim))
    return arr

# Helper to col_change
def col_helper(arr,dim):
    new=[]
    for i in range(dim):
        for j in arr[i*dim + 1:(i+1)*dim]:
            new.append(j)
        new.append(arr[i*dim])
    return new



## Transformation - reflect vertically
def vreflect(arr):
    return arr[::-1]

# Transformation - reflect horizontally
def hreflect(arr):
    return list(map(list,(zip(*((list(zip(*arr)))[::-1])))))

# Transformation - rotate clockwise
def clock_rotate(arr):
    return hreflect(list (zip(*arr)))

# Transformation - rotate counter-clockwise
def counter_rotate(arr):
    return vreflect(list (zip(*arr)))

# Transformation - substitution
def substitute(arr,v1,v2):
    new_arr=[]
    
    for i in arr:
        temp=[]
        for j in i:

            if(j==v1):
                temp.append(v2)
            elif (j==v2):
                temp.append(v1)
            else:
                temp.append(j)

        new_arr.append(temp)

    return new_arr


# prints out in readable format
def print_out(res):
    for i in res:
        for j in i:
            print(j, end=" ")
        print("")

    

## MAIN
length=int(input("Enter Dimension: "))
sub_len = int(sqrt(length))
x=make_parent(sub_len)
print(x)

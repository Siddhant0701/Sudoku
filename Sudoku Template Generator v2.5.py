## Sudoku Template Generator v2.5
## Author: Siddhant Mahajan
## Date: 9th May, 2021

## This code generates a template for a sudoku puzzle of a input dimension
## where all missing numbers are 0's. The scramble is determined from
## the conducted research.
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

# Transformation - Single row interchange (Same subsection)
def row_switch(arr,r1,r2):
    x=list(arr)
    temp=x[r1]
    x[r1]=x[r2]
    x[r2]=temp
    return x

# Transformation - Single column interchange (Same subsection)
def col_switch(arr,c1,c2):
    x=list(zip(*arr))
    return list(zip(*(row_switch(x,c1,c2))))

# Transformation - Subsectional row interchange
def sub_row_switch(arr,s1,s2,dim):
    x=list(arr)
    temp=[]
    for i in range(dim):
        x=row_switch(x,s1*dim+i,s2*dim+i)
    return x

# Transformation - Subsectional column interchange
def sub_col_switch(arr,s1,s2,dim):
    x=list(zip(*arr))
    temp=[]
    for i in range(dim):
        x=row_switch(x,s1*dim+i,s2*dim+i)
    return list(zip(*x))

# prints out in readable format
def print_out(res):
    for i in res:
        for j in i:
            print(j, end=" ")
        print("")

    

## MAIN
length=int(input("Enter Dimension: "))
dim = int(sqrt(length))
parent=make_parent(dim)
c=sub_col_switch(parent,0,1,3)
print_out(c)


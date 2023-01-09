#!/usr/bin/env python3


def check_dim(mat):
    ''' This function returns the dimension of a matrix '''
    row = len(mat)
    col = len(mat[0])

    for i in range(len(mat)):
        if len(mat[i]) != col:
            return 'This is not a valid matrix'
    
    return (row, col)

def add_(list_1, list_2):

    if len(list_2) == 0:
        return list_1
    
    return [a + b for a, b in zip(list_1, list_2)]

def multiply_mat(mat_1, mat_2):

    dim_1 = check_dim(mat_1)
    dim_2 = check_dim(mat_2)

    if dim_1[1] != dim_2[0]: # the col of the first matrix should be equal to the row of the second matrix

        return 'Cannot perform matrix multiplication'

    r = []

    for a in mat_1:
        h = []
        for i, b in enumerate(mat_2):
            t = []
            for c in b:
               t.append(a[i] * c) 
            t = add_(t, h) 
            h = t
        r.append(h)

    return r


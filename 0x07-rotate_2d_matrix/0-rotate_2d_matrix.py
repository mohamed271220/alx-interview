#!/usr/bin/python3
"""
Rotate a 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D Matrix
    args:
        matrix: List[List[int]]
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    for row in matrix:
        row.reverse()
    return matrix

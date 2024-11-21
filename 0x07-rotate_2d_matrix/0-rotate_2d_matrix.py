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
    cols = len(matrix)
    rows = len(matrix[0])
    new_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(cols):
        for j in range(rows):
            new_matrix[j][cols - 1 - i] = matrix[i][j]
    for i in range(cols):
        for j in range(rows):
            matrix[i][j] = new_matrix[i][j]
    return matrix


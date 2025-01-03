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
    # space complexity: O(1)
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    for row in matrix:
        row.reverse()
    return matrix


# space complexity: O(n)
# cols = len(matrix)
# rows = len(matrix[0])
# new_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

# for i in range(cols):
#     for j in range(rows):
#         new_matrix[j][cols - 1 - i] = matrix[i][j]
# for i in range(cols):
#     for j in range(rows):
#         matrix[i][j] = new_matrix[i][j]
# return matrix


""" ts code
function rotate2DMatrix(matrix: number[][]): number[][] {
    const cols = matrix.length; // number of columns in the matrix
    const rows = matrix[0].length; // number of rows in the matrix
    const newMatrix: number[][] = Array.from({ length: rows }, () => Array(cols).fill(0)); // create a new matrix to store the rotated values and fill it with 0s

    for (let i = 0; i < cols; i++) { // iterate through the columns
        for (let j = 0; j < rows; j++) { // iterate through the rows
            newMatrix[j][cols - 1 - i] = matrix[i][j]; // rotate the values and store them in the new matrix
        }
    }
    for (let i = 0; i < cols; i++) { // iterate through the columns
        for (let j = 0; j < rows; j++) { // iterate through the rows
            matrix[i][j] = newMatrix[i][j]; // copy the rotated values back to the original matrix
        }
    }
    return matrix;
}
"""

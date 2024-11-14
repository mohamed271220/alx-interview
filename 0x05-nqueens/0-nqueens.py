#!/usr/bin/python3
"""
N queens
"""
import sys
from typing import List

if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])


def queens(n, i=0, a=[], b=[], c=[]):
    """find possible positions"""
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solve(n):
    """solve"""
    k = []
    i = 0
    for solution in queens(n, 0):
        for s in solution:
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0


solve(n)

# def solveQueens(n:int) -> List[List[str]]:
#     col = set()
#     posDiag = set() # row + col
#     negDiag = set() # row - col
#     res = []
#     board = [['.' for _ in range(n)] for _ in range(n)]
#     def backtrack(r):
#         if r == n:
#             res.append([''.join(row) for row in board])
#             return
#         for c in range(n):
#             if c in col or (r+c) in posDiag or (r-c) in negDiag:
#                 continue
#             col.add(c)
#             posDiag.add(r+c)
#             negDiag.add(r-c)
#             board[r][c] = 'Q'
#             backtrack(r+1)
#             col.remove(c)
#             posDiag.remove(r+c)
#             negDiag.remove(r-c)
#             board[r][c] = '.'
#     backtrack(0)
#     return res

# # to print every possible solution
# def printSolution(board):
#     for i in range(len(board)):
#         for j in range(len(board)):
#             print(board[i][j], end = " ")
#         print()

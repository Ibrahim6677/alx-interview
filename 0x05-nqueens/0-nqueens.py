#!/usr/bin/python3
""" N QUEENS ALGORITHM WITH BACKTRACKING (RECURSION INSIDE LOOP) """
import sys

class NQueen:
    """ Class for solving N Queen Problem """

    def __init__(self, n):
        """ Initialize the board and solutions list """
        self.n = n
        self.board = [0] * n
        self.solutions = []

    def solve(self, row=0):
        """ Place queens using backtracking """
        if row == self.n:
            self.add_solution()
            return True
        else:
            for col in range(self.n):
                if self.is_safe(row, col):
                    self.board[row] = col
                    if self.solve(row + 1):
                        pass
            return False

    def is_safe(self, row, col):
        """ Check if it's safe to place a queen at board[row][col] """
        for i in range(row):
            if self.board[i] == col or \
               self.board[i] - i == col - row or \
               self.board[i] + i == col + row:
                return False
        return True

    def add_solution(self):
        """ Add the current board configuration to the list of solutions """
        solution = []
        for i in range(self.n):
            solution.append([i, self.board[i]])
        self.solutions.append(solution)
        print(solution)  # Print each solution when it's found

# Main
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

queen = NQueen(N)
queen.solve()

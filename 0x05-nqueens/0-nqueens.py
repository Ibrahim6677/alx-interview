#!/usr/bin/python3
"""N QUEENS ALGORITHM WITH BACKTRACKING (RECURSION INSIDE LOOP)"""
import sys

class NQueen:
    """ Class for solving N Queen Problem """

    def __init__(self, n):
        """ Initialize global variables """
        self.n = n
        self.x = [0 for _ in range(n + 1)]
        self.res = []
        print(f"Initialized NQueen with n = {self.n}")  # Debugging line

    def place(self, k, i):
        """ Check if the k-th queen can be placed in the i-th column """
        for j in range(1, k):
            if self.x[j] == i or abs(self.x[j] - i) == abs(j - k):
                print(f"Cannot place queen {k} at column {i} due to conflict with queen {j}")  # Debugging line
                return 0
        print(f"Can place queen {k} at column {i}")  # Debugging line
        return 1

    def nQueen(self, k):
        """ Try to place queens on the board """
        print(f"Trying to place queen {k}")  # Debugging line
        for i in range(1, self.n + 1):
            if self.place(k, i):
                self.x[k] = i
                print(f"Placed queen {k} at column {i}")  # Debugging line
                if k == self.n:
                    solution = []
                    for i in range(1, self.n + 1):
                        solution.append([i - 1, self.x[i] - 1])
                    self.res.append(solution)
                else:
                    self.nQueen(k + 1)
        return self.res

# Main

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]

try:
    N = int(N)
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

print(f"Running NQueen with N = {N}")  # Debugging line
queen = NQueen(N)
res = queen.nQueen(1)

# Print the number of solutions found
print(f"Number of solutions found: {len(res)}")

# Print all solutions
if res:
    for solution in res:
        print(solution)
else:
    print("No solutions found.")

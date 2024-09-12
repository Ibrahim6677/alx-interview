#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    # Check if it's safe to place a queen at board[row][col]
    # Check the row, column, and diagonals for conflicts
    
    def solve_nqueens(board, col, N, solutions):
        # Recursive function to solve the N queens problem
        
        def print_solutions(solutions):
            # Print each solution
            
            if __name__ == "__main__":
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
                
                board = [[0] * N for _ in range(N)]
                solutions = []
                solve_nqueens(board, 0, N, solutions)
                print_solutions(solutions)

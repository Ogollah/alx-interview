#!/usr/bin/python3
"""Solves the N Queens problem.

The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard.

Usage: nqueens N
    If the user called the program with the wrong number of arguments,
    print Usage: nqueens N, followed by a new line, and exit with the status 1
    where N must be an integer greater or equal to 4
    If N is not an integer, print N must be a number,
    followed by a new line, and exit with the status 1
    If N is smaller than 4, print N must be at least 4,
    followed by a new line, and exit with the status 1

The program should print every possible solution to the problem.
    One solution per line.
    Format: see example.

You don’t have to print the solutions in a specific order.
You are only allowed to import the sys module.
"""
import sys


def is_safe(board, row, col):
    """Check if placing a queen at a given position is safe.

    Args:
        board (list): The current state of the board.
        row (int): The row to place the queen.
        col (int): The column to place the queen.

    Returns:
        bool: True if it's safe to place a queen at the
        given position, False otherwise.
    """
    # Check for queens in the same column
    for i in range(row):
        if board[i] == col:
            return False
        # Check for queens in the diagonals
        if abs(i - row) == abs(board[i] - col):
            return False
    return True


def solve_n_queens(n, row, board, solutions):
    """Recursively solve the N Queens problem using backtracking.

    Args:
        n (int): The size of the chessboard.
        row (int): The current row being considered.
        board (list): The current state of the board.
        solutions (list): A list to store the solutions found.
    """
    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
    else:
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve_n_queens(n, row + 1, board, solutions)


def print_solutions(solutions):
    """Print the solutions found.

    Args:
        solutions (list): A list of solutions to print.
    """
    for solution in solutions:
        print(solution)


def nqueens(n):
    """Entry point for solving the N Queens problem.

    Args:
        n (str): The size of the chessboard.

    Raises:
        ValueError: If the provided argument is not a valid integer.
    """
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [-1] * n
    solutions = []
    solve_n_queens(n, 0, board, solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    n = sys.argv[1]
    nqueens(n)

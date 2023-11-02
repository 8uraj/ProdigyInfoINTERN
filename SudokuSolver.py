import tkinter as tk

def solve_sudoku():
    # Your Sudoku solving algorithm goes here
    pass

def clear_board():
    for i in range(9):
        for j in range(9):
            entry_grid[i][j].delete(0, tk.END)

def create_grid(root):
    global entry_grid
    entry_grid = [[0 for _ in range(9)] for _ in range(9)]
    
    for i in range(9):
        for j in range(9):
            entry = tk.Entry(root, width=2, font=('Arial', 20), justify='center')
            entry.grid(row=i, column=j)
            entry_grid[i][j] = entry

def get_puzzle():
    puzzle = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            value = entry_grid[i][j].get()
            if value.isdigit() and 1 <= int(value) <= 9:
                puzzle[i][j] = int(value)
            else:
                return None
    return puzzle

def display_solution(solution):
    if solution is not None:
        for i in range(9):
            for j in range(9):
                entry_grid[i][j].delete(0, tk.END)
                entry_grid[i][j].insert(0, str(solution[i][j]))
        status_label.config(text="Solved!")
    else:
        status_label.config(text="Invalid Input!")

def solve_button_click():
    puzzle = get_puzzle()
    if puzzle is not None:
        solution = solve_sudoku(puzzle)
        display_solution(solution)

root = tk.Tk()
root.title("Sudoku Solver")

create_grid(root)

solve_button = tk.Button(root, text="Solve Sudoku", command=solve_button_click)
solve_button.grid(row=10, column=0, columnspan=9, pady=10)

clear_button = tk.Button(root, text="Clear Board", command=clear_board)
clear_button.grid(row=11, column=0, columnspan=9, pady=10)

status_label = tk.Label(root, text="")
status_label.grid(row=12, column=0, columnspan=9)

root.mainloop()

import random
import time
import os
def dead_state(width, height):
    res = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(0)
        res.append(row)
    return res
def random_state(width, height):
    res = []
    for i in range(height):
        row = []
        for j in range(width):
            cell = 0
            if random.random() < 0.5:
                cell = 1
                row.append(cell)
            else:
                row.append(cell)
        res.append(row)
    return res
def render(board):
    for rows in board:
        for cell in rows:
            if cell == 1:
                print('*', end='')  # Print '*' for cell value 1
            else:
                print(' ', end='')  # Print a space for cell value 0
        print()  # Move to the next line after each row
def next_state(board):
    res = []
    for row in range (len(board)):
        res_row = []
        for col in range (len(board[row])):
            cell = 0
            cur_state = board[row][col]
            alive_neighbours = 0
            if row > 0 and col > 0 and board[row-1][col-1] == 1:
                alive_neighbours += 1
            if col > 0 and board[row][col-1] == 1:
                alive_neighbours += 1
            if row < len(board) - 1 and col > 0 and board[row+1][col-1]:
                alive_neighbours += 1
            if row < len(board) - 1 and board[row+1][col] == 1:
                alive_neighbours += 1
            if row < len(board) - 1 and col < len(board[row]) - 1 and board[row+1][col+1] == 1:
                alive_neighbours += 1
            if col < len(board[row]) - 1 and board[row][col+1] == 1:
                alive_neighbours += 1
            if row > 0 and col < len(board[row]) - 1 and board[row-1][col + 1]:
                alive_neighbours += 1
            if row > 0 and board[row-1][col] == 1:
                alive_neighbours += 1
            if cur_state == 1 and alive_neighbours > 1 and alive_neighbours < 4:
                cell = 1
            elif cur_state == 0 and alive_neighbours == 3:
                cell = 1
            res_row.append(cell)
        res.append(res_row)
    return res
def load_from_file(file_path):
    board = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                row = [int(char) for char in line.strip()]
                board.append(row)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except IOError:
        print(f"Error: Could not read the file {file_path}.")
    except ValueError:
        print(f"Error: The file {file_path} contains non-integer values.")
    return board
def check_board(board):
    for row in board:
        for cell in row:
            if cell == 1:
                return True
    return False
def count_alive_cells(board):
    count = 0
    for row in board:
        count += sum(row)  # Sum the values in the row (1s are alive cells)
    return count
def run_game():
    width = 10
    height = 10
    board = []
    glider_gun = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    choice = input("Type 1 to load toad\nType 2 to load glider gun\nType 3 to randomize seed\nType 4 to enter your board\n")
    if choice == "1":
        board = load_from_file(r"c:\Users\Admin\OneDrive\Desktop\Code\fun projects\Game of life\toad.txt")
        if not board:  # Check if the board is empty
            print("Failed to load the board.")
            return
    elif choice == "2":
        board = glider_gun
    elif choice == "3":
        m = int(input("Enter the height:"))
        n = int(input("Enter the width:"))
        board = random_state(n, m)
    elif choice == "4":
        m = int(input("Enter the height:"))
        n = int(input("Enter the width:"))
        for i in range (m):
            f = f"Enter row {i+1} with {n} binaries: "
            print(f)
            row = input()
            parsedrow = [int(char) for char in row]  
            while len(parsedrow) != n:
                print("Error: invalid length, reenter: ")
                row = input("Enter row " + str(i+1) + " with n binaries: ")
                parsedrow = row.split()
            board.append(parsedrow)
    generations = 0
    max_alive_cells = 0
    while check_board(board):
        # Clear the terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')
        render(board)
        alive_cells = count_alive_cells(board)
        if alive_cells > max_alive_cells:
            max_alive_cells = alive_cells
        print(f"current generation: {generations}")
        print(f"Current alive cells: {alive_cells}")
        print(f"Max alive cells: {max_alive_cells}")
        # Update the board
        board = next_state(board)
        generations += 1
        time.sleep(0.2)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"The cells died after {generations} generations.")
    print(f"Max alive cells: {max_alive_cells}")

if __name__ == "__main__":
    run_game()


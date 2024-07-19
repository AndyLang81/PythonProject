import random
from colorama import init, Fore

# Initialize colorama
init()

# Function to create the grid
def create_grid(size):
    return [['~' for _ in range(size)] for _ in range(size)]

# Function to place the submarine
def place_submarine(grid, size):
    sub_size = 3
    placed = False
    while not placed:
        orientation = random.choice(['H', 'V'])
        if orientation == 'H':
            row = random.randint(0, size - 1)
            col = random.randint(0, size - sub_size)
            if all(grid[row][col + i] == '~' for i in range(sub_size)):
                for i in range(sub_size):
                    grid[row][col + i] = 'S'
                placed = True
        else:
            row = random.randint(0, size - sub_size)
            col = random.randint(0, size - 1)
            if all(grid[row + i][col] == '~' for i in range(sub_size)):
                for i in range(sub_size):
                    grid[row + i][col] = 'S'
                placed = True

# Function to print the grid with coordinates
def print_grid(grid):
    size = len(grid)
    header = "  " + " ".join(str(i + 1) for i in range(size))
    print(header)
    for i, row in enumerate(grid):
        print(chr(ord('A') + i) + " " + " ".join(row))

# Function to take a shot
def take_shot(grid, row, col):
    if grid[row][col] == 'S':
        grid[row][col] = 'X'
        return Fore.GREEN + "Hit!" + Fore.RESET
    elif grid[row][col] == '~':
        grid[row][col] = 'X'
        return Fore.RED + "MISS!" + Fore.RESET
    else:
        return Fore.RED + "Already shot here!" + Fore.RESET

# Function to check if the submarine is sunk
def is_sunk(grid):
    return any(cell == 'X' for row in grid for cell in row)

# Function to convert user input (e.g., A1) to grid coordinates and validate input
def convert_input(user_input):
    if len(user_input) != 2:
        return None, None
    
    row_char = user_input[0].upper()
    col_char = user_input[1]
    
    if row_char not in 'ABCDE' or col_char not in '12345':
        return None, None
    
    row = ord(row_char) - ord('A')
    col = int(col_char) - 1
    
    return row, col

# Function to get the correct grammar for the remaining shots
def shots_left_message(shots):
    if shots == 1:
        return Fore.GREEN + "1 shot left." + Fore.RESET
    else:
        return Fore.GREEN + f"{shots} shots left." + Fore.RESET

# Main game function
def play_game(size=5):
    grid = create_grid(size)
    place_submarine(grid, size)
    shots = 3
    print(Fore.GREEN + "Welcome to Submarine Hunter. Find the submarine before it sinks your ship!" + Fore.RESET)
    print(Fore.GREEN + "Enter coordinates in the format A1, B3, etc." + Fore.RESET)
    print(Fore.GREEN + "You have 3 shots. One hit will sink the sub, make them count." + Fore.RESET)
    while shots > 0:
        print(f"\nYou have {shots_left_message(shots)}")
        print_grid([['~' if cell == 'S' else cell for cell in row] for row in grid])  # Hide submarine cells
        user_input = input("Enter coordinate:\n ")
        row, col = convert_input(user_input)
        if row is not None and col is not None and 0 <= row < size and 0 <= col < size:
            result = take_shot(grid, row, col)
            print(result)
            if result == Fore.GREEN + "Hit!" + Fore.RESET:
                print(Fore.GREEN + "You sunk the submarine! You now rank amongst the naval heroes." + Fore.RESET)
                print(Fore.GREEN + "To repeat this riveting experience, run the program again." + Fore.RESET)
                break
            elif result == Fore.RED + "MISS!" + Fore.RESET and shots == 2:
                print(Fore.RED + "The sub is moving into position." + Fore.RESET)
            elif result == Fore.RED + "MISS!" + Fore.RESET and shots == 1:
                print(Fore.RED + "The sub is preparing its torpedoes!" + Fore.RESET)
            elif result == Fore.RED + "Already shot here!" + Fore.RESET:
                print(Fore.RED + "You have already fired at this location. Try a different coordinate." + Fore.RESET)
                continue
        else:
            print(Fore.RED + "Invalid coordinates. Try again." + Fore.RESET)
            continue
        shots -= 1
    else:
        print(Fore.RED + "Game over! You're now defenceless." + Fore.RESET)
        print(Fore.RED + "The submarine (SSS) was hiding at:")
        print_grid(grid)
        print(Fore.YELLOW + "To lose again, please run the program once more." + Fore.RESET)

if __name__ == "__main__":
    play_game()
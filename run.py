import random

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
    header = "  " + " ".join(chr(ord('A') + i) for i in range(size))
    print(header)
    for i, row in enumerate(grid):
        print(f"{i + 1} " + " ".join(row))

# Function to take a shot
def take_shot(grid, row, col):
    if grid[row][col] == 'S':
        grid[row][col] = 'X'
        return "Hit!"
    elif grid[row][col] == '~':
        grid[row][col] = 'X'
        return "Miss!"
    else:
        return "Already shot here!"

# Function to check if the submarine is sunk
def is_sunk(grid):
    return any(cell == 'X' for row in grid for cell in row)

# Function to convert user input (e.g., A1) to grid coordinates
def convert_input(user_input):
    try:
        row = ord(user_input[0].upper()) - ord('A')
        col = int(user_input[1]) - 1
        return row, col
    except (IndexError, ValueError):
        return None, None

# Main game function
def play_game(size=5):
    grid = create_grid(size)
    place_submarine(grid, size)
    shots = 3
    print("Welcome to Submarine Hunter. Find the submarine before it sinks your ship!")
    print("Enter coordinates in the format A1, B3, etc.")
    while shots > 0:
        print(f"\nYou have {shots} shots left.")
        print_grid([['~' if cell == 'S' else cell for cell in row] for row in grid])  # Hide submarine cells
        user_input = input("Enter coordinate:\n ")
        row, col = convert_input(user_input)
        if row is not None and col is not None and 0 <= row < size and 0 <= col < size:
            result = take_shot(grid, row, col)
            print(result)
            if result == "Hit!":
                print("Congratulations! You sunk the submarine! You now rank amongst the naval heroes. To repeat this riveting experience, run the program again.")
                break
            elif result == "Miss!" and shots == 3:
                print("The sub is moving into position.")
            elif result == "Miss!" and shots == 2:
                print("The sub is preparing its torpedoes!")
        else:
            print("Invalid coordinates. Try again.")
        if result == "Already shot here!":
            continue
        shots -= 1
    else:
        print("Game over! You're now defenceless.")
        print("The submarine (SSS) was hiding at:")
        print_grid(grid)
        print("To lose again, please run the program once more.")

# Run the game
play_game()

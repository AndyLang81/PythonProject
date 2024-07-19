# Submarine Hunter

Submarine Hunter is a command-line game where the player has to locate and sink a hidden submarine on a grid. You have a limited number of shots to find the submarine before the game ends.

## Link to live project (https://project3-python-45d7a006b41f.herokuapp.com/)

## How to Play

1. The game initializes a grid and places a submarine of size 3 at a random location.
2. Enter coordinates in the format `A1`, `B3`, etc., to take a shot.
3. The game tells you if you hit the submarine, missed, or have shot at the same location before.
4. You have 3 shots to find and sink the submarine.
5. The game ends when you either sink the submarine or run out of shots.

## Functions

- `create_grid(size)`: Creates a grid of the specified size.
- `place_submarine(grid, size)`: Places a submarine randomly on the grid.
- `print_grid(grid)`: Prints the grid with coordinates.
- `take_shot(grid, row, col)`: Takes a shot at the specified coordinates.
- `is_sunk(grid)`: Checks if the submarine is sunk.
- `convert_input(user_input)`: Converts user input (e.g., A1) to grid coordinates.
- `shots_left_message(shots)`: Returns a message about remaining shots.
- `play_game(size=5)`: Runs the main game loop.

## Technologies Used

- **Python**: The game is implemented using Python, a versatile programming language that is widely used for scripting and developing various applications.
- **Random Library**: Utilized for generating random positions for placing the submarine and determining orientations.
- **Command Line Interface (CLI)**: The game runs in a command-line environment where the player inputs coordinates and receives text-based feedback.
- **Github**: Live site is controlled and launched via Github.

## Game Logic

1. **Grid Initialization**: A grid of a specified size is created with all cells marked as `~`.
2. **Submarine Placement**: A submarine of size 3 is placed randomly on the grid either horizontally or vertically, without overlapping or going out of bounds.
3. **User Input**: The user inputs coordinates to take a shot. The input is validated and converted to grid coordinates.
4. **Shot Evaluation**: Each shot is evaluated to determine if it’s a hit or miss. The result is displayed, and the shot is marked on the grid.
5. **Victory Condition**: The game checks if the submarine is fully hit. If so, a win message is displayed.
6. **Game Over**: If all shots are used without sinking the submarine, a game over message is shown, revealing the submarine’s location.

Game logic flowchart: 
![alt text](<assets/readmeassets/game logic.png>)

# User Stories

## `create_grid(size)`

User will see a grid of the specified size with empty cells (`~`) when the game starts.

## `place_submarine(grid, size)`

User will see a randomly placed submarine of size 3 on the grid, but the exact location will be hidden.

## `print_grid(grid)`

User will see the grid with row and column labels:
- Cells marked with `~` represent unexplored locations.
- Cells marked with `X` show where shots have been taken.
- The submarine will be hidden to maintain suspense.

## `take_shot(grid, row, col)`

User will see feedback after taking a shot:
- "Hit!" if the shot hits the submarine (cell marked with `X`).
- "Miss!" if the shot misses (cell marked with `X`).
- "Already shot here!" if the location was previously targeted.

## `is_sunk(grid)`

User will see a message indicating whether the submarine has been sunk after each shot.

## `convert_input(user_input)`

User will see that the game correctly interprets the coordinates entered (e.g., `A1`). If invalid input is provided, the user will be prompted to try again.

## `shots_left_message(shots)`

User will see a message indicating the number of shots remaining, with proper grammar (e.g., "1 shot left." or "3 shots left.").

## `play_game(size=5)`

User will see:
1. Instructions and the initial grid.
2. Prompts to enter coordinates for taking shots.
3. Feedback on shots and updates to the grid.
4. Messages about the number of remaining shots and game status.
5. A final message either celebrating a win or indicating a loss, with the submarine's location revealed.

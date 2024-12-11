# Submarine Hunter

Submarine Hunter is a command-line game where players take on the challenge of finding and sinking a hidden submarine on a grid. With limited shots and a randomized submarine location, the game tests your logic, strategy, and a bit of luck.

## Live Demo

Check out the live version here: [Submarine Hunter](https://project3-python-45d7a006b41f.herokuapp.com/)

---

## Introduction

Submarine Hunter was inspired by classic naval strategy games like Battleship. It’s designed to be simple, engaging, and perfect for anyone who enjoys puzzles or quick challenges. The game brings strategy and fun to your terminal, letting you take on the thrill of hunting a hidden submarine in a race against time.

This project was created to:
1. Practice Python development skills.
2. Explore game mechanics like randomization, input validation, and looping structures.
3. Build a foundation for adding more complex features in the future.

---

## User Stories

### For Casual Gamers  
I want a quick and fun game that’s easy to play but still challenging, so I can enjoy it during breaks without investing too much time.

### For Python Learners  
I want to see how the game is built behind the scenes, so I can learn practical coding techniques like user input handling, randomization, and game loops.

### For Problem-Solving Enthusiasts  
I want a game that challenges my logic and decision-making skills, so I can have fun while sharpening my ability to think strategically.

---

## Features

- **Dynamic Submarine Placement:** Every game starts with the submarine in a new random location.
- **Limited Shots:** Players only have 3 shots to sink the submarine, making every move count.
- **Instant Feedback:** Clear messages let you know if you hit, miss, or repeated a shot.
- **Simple Controls:** Enter coordinates like `A1` or `B3` to play — it’s that easy.
- **Replayability:** The game restarts quickly, so you can play over and over.

---

## Game Logic

1. **Grid Creation:** A 5x5 grid starts with all cells marked as `~` (unexplored).
2. **Random Submarine Placement:** A 3-cell-long submarine is randomly placed either horizontally or vertically.
3. **Player Interaction:**
   - Input is validated and converted to grid coordinates.
   - Each shot is evaluated as a hit, miss, or duplicate.
4. **Game Progression:**
   - The grid updates after each shot.
   - Remaining shots are displayed.
   - The game checks after every move if the submarine is sunk.
5. **End Conditions:**
   - **Win:** All submarine cells are hit.
   - **Lose:** No shots remain, and the submarine is revealed.

Game logic flowchart:  
![Game Logic Flowchart](assets/readmeassets/gamelogic.png)

---

## Technologies Used

- **Python:** Used for game logic and flow.
- **Random Library:** To generate random submarine placements and orientations.
- **Command-Line Interface (CLI):** A simple, text-based interface for gameplay.
- **GitHub:** Version control and project hosting.
- **Heroku:** Deployed for live playability.

---

## Installation and Deployment

### Local Installation
adding later

### Deployment on Heroku
adding later

---

## Testing

### Scenarios Tested
- **Valid Input:** Coordinates like `A1` and `C3` work as expected.
- **Invalid Input:** Handles out-of-bounds or incorrectly formatted inputs.
- **Repeat Shots:** Warns the user if they target the same cell twice.
- **Winning:** The game recognizes and announces when the submarine is sunk.
- **Losing:** Displays the submarine’s location after all shots are used.

### Test Case Outputs

#### Game Start
Initial grid and instructions:  
![Game Start](assets/readmeassets/Test1.png)

#### Taking a Shot
"Miss!" feedback for a missed shot:  
![Miss Feedback](assets/readmeassets/test2.png)

#### Proximity Feedback
Feedback as shots get closer to the submarine:  
![Proximity Feedback](assets/readmeassets/Test3.png)

#### Game Over
Submarine location revealed after losing:  
![Game Over](assets/readmeassets/test4.png)

#### Winning the Game
Victory message displayed:  
![Winning Message](assets/readmeassets/test5.png)

### Code Validation
The code was validated with PEP8, ensuring compliance with Python standards:  
![PEP8 Validation](assets/readmeassets/pep8validated.png)

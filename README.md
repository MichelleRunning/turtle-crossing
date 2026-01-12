# Turtle Crossing Game (Python)

A Python arcade-style game inspired by the classic Frogger, built using the `turtle` graphics module.  
Players control a turtle that must safely cross a busy road while avoiding oncoming cars. Each successful crossing increases the difficulty.

---

## Gameplay

- Use the **Up Arrow key** to move the turtle upward
- Avoid cars moving across the screen
- Each successful crossing increases the **level**
- With each level, cars move faster
- The game ends if the turtle collides with a car

---

## Technical Concepts

- Python programming fundamentals
- Object-Oriented Programming (OOP) with classes for Turtle, Cars, and Scoreboard
- Event handling and user input
- Game loop logic and level progression
- Collision detection

---

## Game Preview

![Turtle Crossing Game Output](output-preview.jpg)

---

## Project Structure
- main.py # Main game loop
- animal.py # Player (turtle) class
- car.py # Car manager and car logic
- scoreboard.py # Score and level display

---

## How to Run:
1. Make sure you have **Python 3** installed
2. Clone the repository:

   ```bash
   git clone https://github.com/MichelleRunning/turtle-crossing-game.git
   ```

3. Run the game:

   ```bash
   python main.py
   ```

4. Use the Up Arrow key to control the turtle and play.

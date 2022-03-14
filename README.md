# Game of Greed I
Contributors: 
- Sarah Hudaib 
- Emad Almajdalawi
- Anas Abu Hammeedah
- Raneem Al Oqaily
- Ahmad Jaara

version = '0.1.0' Date 3/14/2022

# Overview
we built a version of the dice game Game of Greed by expanding your understanding of Python standard library.
## Features
- Create a project named `game-of-greed`.
Define a `GameLogic class` in `game_of_greed/game_logic.py` file.
- Handle calculating score for dice roll
- Add `calculate_score` static method to GameLogic class.
- The input to `calculate_score` is a tuple of integers that represent a dice roll.
- The output from calculate_score is an integer representing the roll’s score according to rules of game.
- Handle rolling dice
Add `roll_dice` static method to GameLogic class.
The input to roll_dice is an integer between 1 and 6.
- The output of `roll_dice` is a tuple with random values between 1 and 6.
- The length of tuple must match the argument given to `roll_dice` method.
- Handle banking points
Define a `Banker class`
Add a `shelf` instance method
Input to shelf is the amount of points (integer) to add to shelf.
- shelf should temporarily store unbanked points.
Add a bank instance method
bank should add any points on the shelf to total and reset shelf to 0.
bank output should be the amount of points added to total from shelf.
Add a `clear_shelf` instance method
`clear_shelf` should remove all unbanked points
# Getting Started
1. In terminal navigate to the folder with the banker.py & game_logic.py
2. Run command "python game_logic.py".
3. To run test use "pytest" command




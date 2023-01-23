# GuessANumberByBeatris
#### This repository contains a console based on Python implementation of the "Guess A Number" game
## Rules:
#### - At the beggining the computer randomly chooses a number between any number among 1 and 100, using randint method of random module;
#### - The player has 7 chances to guess the number and if he/she succeeds, he/she may go to the next level;
#### - With each and every level, the range of the computer random choice increases (for example, the range in the second level is 2 - 200, in the third level 3 - 300 etc.);
#### - With each and every level, the number of maximum attempts a player has to guess the number, decreases by one (in the second level, maximum guesses = 6, in the third level, maximum guesses = 5, etc.);
#### - If the number of maximum attempts is reached, the player loses the game;
#### - If a player completes the 5th level, he/she wins;

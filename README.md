# **GuessANumberByBeatris**
#### _This repository contains a console based on Python implementation of the "Guess A Number" game_
## Rules:
#### - At the beggining the computer randomly chooses a number between any number among 1 and 100, using randint method of random module;
#### - The player has 7 chances to guess the number and if he/she succeeds, he/she may go to the next level;
#### - With each and every level, the range of the computer random choice increases 
#####  *(for example, the range in the second level is 2 - 200, in the third level 3 - 300 etc.)*;
#### - With each and every level, the number of maximum attempts a player has to guess the number, decreases by one 
#####    *(in the second level, maximum guesses = 6, in the third level, maximum guesses = 5, etc.)*;
#### - If the number of maximum attempts is reached, the player loses the game;
#### - If a player completes the 5th level, he/she wins;
## Key Features:
#### - Initially the lowest number represents the lowest number in the range of the computer choice and vice versa. However, if the player has chosen a number that is different from the number of the computer and that number is higher than the lowest number or lower than the highest number, each of both values acquires user's choice
#####    *(for example at the beginning of the game, the lowest number = 1 and the highest number = 100, in this case, if computer number is equal to 50, and the user has chosen 30 and 70, then the lowest number becomes 30 and the highest becomes 70. In this way, by comparing the current lowest and highest number, we help the user to keep track what numbers he/she has already chosen, and in what range the computer number is, respectively)*;
#### - If a player has reached the number of maximum attempts, but both current lowest and highest numbers -/+ 1 are equal to the computer number, then the player is given one more chance to guess the number 
#####    *(for example, if the computer number is 50 and the user has already chosen 49 and 51)*;
#### - Finally, if a player has reached the number of maximum attempts or has won the game, he/she may restart the game
## Screenshots:
<img width="461" alt="Screenshot 2023-01-23 at 16 24 23" src="https://user-images.githubusercontent.com/122045435/214063729-2d20ca73-30fa-48a7-a25b-82c568b0903d.png">
<img width="501" alt="Screenshot 2023-01-23 at 15 33 22" src="https://user-images.githubusercontent.com/122045435/214052602-b19779e5-61a2-4c1c-ae90-714427613aa1.png">
<img width="449" alt="Screenshot 2023-01-23 at 17 13 06" src="https://user-images.githubusercontent.com/122045435/214075946-0e48ea97-82b3-41df-95ef-ae9dae9d5f94.png">
## You can play the game directly in your browser [HERE](https://replit.com/@BeatrisIlieve/GuessANumberByBeatris#main.py)

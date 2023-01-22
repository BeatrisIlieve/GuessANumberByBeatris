# importing colorama module in order to add colours and style to the text
import colorama
from colorama import Fore, Style

# importing random module so as the computer can play a move
import random

# welcoming the user
my_list = ['Welcome', 'to', 'Guess', 'A', 'Number', 'Game', '!\n']
for starting_index in range(len(my_list), -1, -1):
    if starting_index == 0:
        my_list.insert(starting_index, f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}")
    elif starting_index % 2 == 0:
        my_list.insert(starting_index, f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}")
    elif starting_index % 3 == 0:
        my_list.insert(starting_index, f"{Fore.LIGHTYELLOW_EX}")
    elif starting_index % 5 == 0:
        my_list.insert(starting_index, f"{Fore.LIGHTBLUE_EX}")
    else:
        my_list.insert(starting_index, f"{Fore.LIGHTYELLOW_EX}")
print(f"{' ' * 8}", end ="")
print(" ".join(my_list), end ="")
print(f"{' ' * 8}")

# auxiliary variables
win_condition = False
max_attempts_condition =  False
levels_counter = 0
max_attempts = 7
highest_number = 100
lowest_number = 1
attempts_in_ordinal_number = ''
bonus_number = 0

# looping until the user enters an invalid input, wins, loses or choose to stop playing
while True:
    # computer randomly chooses a number between any number among one and one hundred,
    # using randint method of random module
    if levels_counter == 0:
        computer_number = random.randint(1, 100)
    # if a user passes the first level, then the range of computer random choice increases
    else:
        computer_number = random.randint((levels_counter + 1), (100 * (levels_counter + 1)))

    # printing the current level number and the number of choices the user has to guess the number
    print(f"{Style.BRIGHT}{Fore.LIGHTCYAN_EX}LEVEL {Fore.LIGHTMAGENTA_EX}{levels_counter + 1}\n"
          f"\n{Fore.LIGHTCYAN_EX}You have {Fore.LIGHTMAGENTA_EX}{max_attempts} {Fore.LIGHTCYAN_EX}"
          f"chances to guess a number between {Fore.LIGHTMAGENTA_EX}{lowest_number}{Fore.LIGHTCYAN_EX} "
          f"and {Fore.LIGHTMAGENTA_EX}{highest_number}!\n")

    # for cycle runs until it reaches the number of maximum attempts
    for current_attempt in range(1, max_attempts + 1):
        # taking user input
        player_input = input(f"{Fore.WHITE}{Style.NORMAL}Guess the number: ")
        # case of invalid input
        if not player_input.isdigit():
            print(f"{Fore.RED}Not a number or a negative number. Try again...")
            continue
        # player's number as integer
        player_number = int(player_input)

        # initially the lowest number represents the lowest number in the range of the computer choice and vice versa;
        # although if user's number is higher than the lowest number or user's number is lower than the highest number
        # and the user's number is different from the number of the computer, both values acquire user's choice;
        # for example at the beginning of the game, the lowest number = 1 and the highest number = 100, in this case,
        # if computer number is equal to 50, and the user has chosen 30 and 70,
        # then the lowest number = 30 and the highest = 70
        if player_number > computer_number or player_number < computer_number:
            if player_number > computer_number:
                if player_number < highest_number:
                    highest_number = player_number
                    print(f"{Fore.BLUE}Too High!")
            elif player_number < computer_number:
                if player_number > lowest_number:
                    lowest_number = player_number
                    print(f"{Fore.RED}Too Low!")
            # by comparing the current lowest and highest number, we help the user to keep track what numbers
            # they have already chosen, and in what range the computer number is, respectively
            print(f"{Fore.LIGHTMAGENTA_EX}Number is between {lowest_number} and {highest_number}")

            # the initial number of max attempts a user can make is 7; if a user reaches the number of max attempt,
            # they loses the game; however in case both current lowest and higher numbers -/+ 1 are equal
            # to the computer number, then the user is given one more chance to guess the number
            # (for example, if the computer number is 50 and the user has already chosen 49 and 51)
            if current_attempt == max_attempts:
                if (lowest_number + 1 == computer_number and highest_number - 1 == computer_number) or\
                        (lowest_number + 1 == computer_number and highest_number - 1 == computer_number):

                    bonus_number = input(f"{Style.BRIGHT}{Fore.LIGHTCYAN_EX}Since you are very close,\nyou get an "
                                         f"extra chance to guess the number!\n"
                                         f"{Fore.WHITE}{Style.NORMAL}Guess the number: ")
                    bonus_number = int(bonus_number)
                    if bonus_number == computer_number:
                        current_attempt += 1
                else:
                    max_attempts_condition = True
                    break
        # case of guessed number
        if player_number == computer_number or bonus_number == computer_number:
            if current_attempt == 1:
                attempts_in_ordinal_number = "1st"
            elif current_attempt == 2:
                attempts_in_ordinal_number = "2nd"
            elif current_attempt == 3:
                attempts_in_ordinal_number = "3rd"
            elif current_attempt == 4:
                attempts_in_ordinal_number = "4th"
            elif current_attempt == 5:
                attempts_in_ordinal_number = "5th"
            elif current_attempt == 6:
                attempts_in_ordinal_number = "6th"
            elif current_attempt == 7:
                attempts_in_ordinal_number = "7th"
            else:
                attempts_in_ordinal_number = "8th"
            print(f"\n{Style.BRIGHT}{Fore.LIGHTGREEN_EX}G{Fore.LIGHTMAGENTA_EX}r{Fore.LIGHTYELLOW_EX}e"
                  f"{Fore.LIGHTBLUE_EX}a{Fore.LIGHTCYAN_EX}t{Fore.LIGHTMAGENTA_EX}!"
                  f"{Fore.LIGHTGREEN_EX} You guessed it on the {Fore.LIGHTMAGENTA_EX}{attempts_in_ordinal_number} "
                  f"{Fore.LIGHTGREEN_EX}attempt!\n")
            # increasing the level number
            levels_counter += 1
            # if level number becomes five, then the user has completed all five levels and won the game
            if levels_counter == 5:
                win_condition = True
                break
            # in case of no win:
            else:
                max_attempts -= 1  # after every level successfully passed, the number of max attempts decreases by one
                # the highest and lowest numbers increase accordingly to the range of the computer choice
                highest_number = 100 * (levels_counter + 1)
                lowest_number = levels_counter + 1
                break # breaking the for cycle and starting counting max attempts again

    # if a user has reached the maximum attempts number or has won the game they are given an option to restart the game
    if win_condition or max_attempts_condition:
        if win_condition:
            print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}Congratulations, You Won!")
        else:
            print(f"{Fore.RED}You have reached the maximum attempts! "
                  f"Computer number is {Fore.LIGHTRED_EX}{computer_number}")
        # option to restart the game
        play_again = input(f"\n{Fore.LIGHTYELLOW_EX}If you want to play again enter {Fore.WHITE}[y]"
                           f"{Fore.LIGHTYELLOW_EX} if not enter {Fore.WHITE}[n]{Fore.LIGHTYELLOW_EX}: \n")
        # if a user choose to play again, the auxiliary variables are returned to their original values
        if play_again == 'y':
            win_condition = False
            max_attempts_condition = False
            levels_counter = 0
            max_attempts = 7
            highest_number = 100
            lowest_number = 1
            bonus_number = 0
            continue # while cycle continues
        # else - it breaks:
        elif play_again == 'n':
            break
        else:
            raise SystemExit(f'{Fore.RED}Invalid input.')
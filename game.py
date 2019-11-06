# coding=utf-8
from random import randint  # Library for random numbers
import os  # Library for console clear


def main_():  # Main question function
    global user_level  # Allows global variables to be modified in this function
    global continue_play
    global menu_choice
    global current_correctness
    while continue_play == 'Y':  # While user wants to keep being quiz'd loop
        os.system('cls')  # Clears console
        num_1, num_2, sum_symbol, sum_answer = calc_sum()
        print('Please enter your answer and press enter')  # Prints question
        print('What is ', num_1, sum_symbol, num_2, '?')  # Prints question
        u_answer = int(input())  # Converts user input into int value
        if u_answer == sum_answer:  # Checks if user answer is same as correct answer
            current_correctness += 1  # Increases consecutive correctness variable
            user_level = check_level()  # Checks to get the users level
            print('That is correct, well done!, You are level ', user_level, ' Press Y to try another sum or N to return to main menu then enter.')  # Notify
            # user
            continue_play = input()  # Checks if user still wants to play
            continue_play = continue_play.upper()  # Converts user entry to uppercase
            while continue_play not in ['Y', 'N']:  # While user has not pressed y or n (They have made an incorrect entry) notify the user to press y or n
                print('Incorrect entry type Y or N and press enter')
                continue_play = input()
                continue_play = continue_play.upper()
        else:
            current_correctness -= 1
            check_level()
            print('Not right, the correct answer is: ', sum_answer, '. You are level ', user_level, ' Press Y to try another sum or N to stop then enter.')
            continue_play = input()
            continue_play = continue_play.upper()
            while continue_play not in ['Y', 'N']:
                print('Incorrect entry type Y or N and press enter')
                continue_play = input()
                continue_play = continue_play.upper()
    continue_play = 'Y'  # Resets continue play back to y for next question
    menu_choice = 0  # Reset menu choice
    os.system('cls')


def gen_num(min_value, max_value):  # Generates and returns 2 random ints between the specified bounds
    num1 = (randint(min_value, max_value))  # Randomly generates values
    num2 = (randint(min_value, max_value))
    return num1, num2


def calc_sum():  # Method to do calculation and return parts of the question and the correct answer
    global menu_choice
    temp = menu_choice  # Saves the menu choice into temp variable, used for randomizing sums
    rand_num1, rand_num2 = gen_num(1, max_rand_value)
    sum_answer = 0  # The correct sum answer
    sum_symbol = ''
    if menu_choice == 5:  #
        menu_choice, waste = gen_num(1, 4)  # Sets the menu_choice variable to a random number between 1-4 to choose a random sum each time
    if menu_choice == 1:
        sum_answer = rand_num1+rand_num2
        sum_symbol = '+'
    if menu_choice == 2:
        sum_answer = rand_num1-rand_num2
        sum_symbol = '-'
    if menu_choice == 3:
        sum_answer = rand_num1*rand_num2
        sum_symbol = 'x'
    if menu_choice == 4:
        sum_answer = rand_num1/rand_num2
        sum_symbol = '÷'
    menu_choice = temp  # Sets the users choice back to what it was so it can continue with randomizing sums in random statement
    return rand_num1, rand_num2, sum_symbol, sum_answer


def check_level():  # Checks and updates users level
    global user_level
    global current_correctness
    global max_rand_value
    if current_correctness == 6 and user_level != 4:  # Checks user has 3 correct answers and isn't already level 4
        user_level += 1  # Increases users level
        max_rand_value += 1  # Increases the random int generator max bounds
        current_correctness = 3  # Resets the correctness back to 0 correct (0 = 3 wrong, 3 = 0 correct or wrong, 6 = 3 correct)
    elif current_correctness == 0 and user_level != 1:
        user_level -= 1
        max_rand_value -= 1
        current_correctness = 3
    elif user_level == 0 or user_level == 4:  # User cant move below level 0 or above level 4
        print('You cannot change level, you are either level 0 or level 4')
    return user_level


def set_choice():
    global menu_choice
    help = 1
    if any([menu_choice == 1, menu_choice == 2, menu_choice == 3, menu_choice == 4, menu_choice == 5]):  # Checks if use has selected a valid number
        main_()
    elif menu_choice == 6:  # If user selects the help option
        while help == 1:
            os.system('cls')
            print('The level system works by increasing your level by 1 with evey 3 consecutively answered correct questions and decreases with 3 '
                  'consecutively answered incorrect questions. To progress you must type the answer to the question displayed and press enter. Please only '
                  'use numbers no characters.\n\n The random mode will give you questions with a random operator such as + or - or X or ÷. \n\n '
                  'To return please type R and press enter.')
            help = input()
            help = help.upper()
            os.system('cls')
    elif menu_choice == 7:  # If user selects the quit option
        return
    else:
        os.system('cls')
        print('Please select a number from the list')
        return
    help = 1


continue_play = 'Y'  # Default at Y to run loop
user_level = 1  # Users current level
max_rand_value = 4  # Max bounds for random int, increases every level
current_correctness = 3  # Current consecutive questions correct (starts at 3 if goes to 6 up 1 level if down to 0 down 1 level)
menu_choice = 0  # Users operator selection


os.system('cls')
print('Welcome to maths is fun python edition!')  # Welcome message
while menu_choice != 7:  # Check to see that the user hasn't quit
    print('Enter the number for the operator you want to be tested on from the list below and press enter; or type 6 for help or 7 to quit and press enter.')
    # Asks the user to select the operator they want to be tested on, help or quit
    print()
    print('1 Addition  |  2 Subtraction  |  3 Multiplication  |  4 Division  |  5 Random Operators  |  6 Help  |  7 Quit\n')  # List of operators
    try:  # Try to take user input give error if its not a number
        menu_choice = int(input())  # Sets the users operator choice from the list
        set_choice()
    except ValueError:
        os.system('cls')
        print('Error: Please only enter numbers')

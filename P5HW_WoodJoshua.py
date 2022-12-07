# Simple Addition and Subtraction Python Quiz that allows user to choose from menu
# option rather they want to add, subtract or exit. program then output random numbers
# to either add or subtract and allows users to attempt to answer correctly
# 20221126
# CTI-110 P5HW2 - Math Quiz
# Joshua Dale Wood
#

import random

print("Welcome to Math Quiz")

def main_menu():
    print("MAIN MENU")
    print("-"*40)
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    print()
    user_input = int(input("Please choose one of the menu options: "))
    while True:
        if user_input == 1:
            add_func()
            break
            main_menu
        elif user_input == 2:
            sub_func()
            break
            main_menu()
        elif user_input == 3:
            print("Thank you for playing...")
            print("Bye!!")
            break
        else:
            print("Invalid menu option. Please choose again.")
            user_input = int(input("Please choose one of the menu options: "))
    exit

def add_func():
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    guess_num = 0
    print(str(num1))
    print("+" + str(num2))
    print()
    answer1 = num1 + num2
    print("Enter answer.")
    user_answer = int(input())
    while True:
        if answer1 > user_answer:
            guess_num += 1
            print("Sorry, guess is to low")
            print()
            user_answer = int(input("try again: "))
        
        elif answer1 < user_answer:
            guess_num += 1
            print("Sorry, guess is to high")
            print()
            user_answer = int(input("try again: "))
        
        else:
            guess_num += 1
            print("Congratulatioins!!!! you answer is correct..")
            print("Number of guesses: ", guess_num)
            break
            exit
    main_menu()
        
def sub_func():
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    print(str(num1))
    print("-" + str(num2))
    print()
    answer1 = num1 - num2
    print("Enter answer.")
    user_answer = int(input())
    guess_num = 0
    while True:
        if answer1 > user_answer:
            guess_num += 1
            print("Sorry, guess is to low")
            print()
            user_answer = int(input("try again: "))
        
        elif answer1 < user_answer:
            guess_num += 1
            print("Sorry, guess is to high")
            print()
            user_answer = int(input("try again: "))
        
        else:
            guess_num += 1
            print("Congratulatioins!!!! you answer is correct..")
            print("Number of guesses: ", guess_num)
            break
            exit
    main_menu()
    
main_menu()



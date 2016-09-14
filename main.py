# Normal Part
import random

number_of_turns = 0

comp_num = random.randint(1, 100)

user_num = 0

while number_of_turns < 5:

    user_num = input("Guess a number between 1-100: ")
    user_num = int(user_num)

    if user_num < comp_num:
        if (user_num + 5) >= comp_num:
            print("You are smaller than the computer's number but within 5 numbers")
        print ("This number is smaller than the computer's number")
        number_of_turns += 1

    elif user_num > comp_num:
        if (user_num - 5) <= comp_num:
            print("You are greater than the computer's number but within 5 numbers")
        print ("This number is greater than the computer's number")
        number_of_turns += 1

    else:
        print ("That is the correct number!")
        number_of_turns += 1
        break

print ("It took you ", number_of_turns, "turns")

# Hard Part and Very Hard Part

number_of_turns = 1

user_num = input("Enter a number between 1-100 for the computer to guess: ")
user_num = int(user_num)

comp_num = random.randint(1, 100)
greater_comp_num = 100
lower_comp_num = 1

while user_num != comp_num:

    if comp_num > user_num:
        print(comp_num, "this number is greater than my number")
        number_of_turns += 1
        greater_comp_num = comp_num
        comp_num = random.randint(lower_comp_num, greater_comp_num)

    elif comp_num < user_num:
        print(comp_num, "this number is smaller than my number")
        number_of_turns += 1
        lower_comp_num = comp_num
        comp_num = random.randint(lower_comp_num, greater_comp_num)

    else:
        print("You guessed my number!")
        break

print("It took the computer ", number_of_turns, "to get the corret number")

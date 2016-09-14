import random

number_of_turns = 1

user_num = input("Enter a number between 1-100 for the computer to guess: ")
user_num = int(user_num)

while user_num < 1 and user_num > 100:
    print("Invalid number!")
    user_num = input("Now guess a number between 1-100: ")
    user_num = int(user_num)

comp_num = random.randint(1, 100)
greater_comp_num = 100
lower_comp_num = 1

while user_num != comp_num:

    if comp_num > user_num:
        if (comp_num - user_num) <= 5:
            number_of_turns += 1
            print("You are greater than the my number but within 5 numbers")
            greater_comp_num = comp_num
            comp_num = random.randit(user_num, greater_comp_num)
        print(comp_num, "this number is greater than my number")
        number_of_turns += 1
        greater_comp_num = comp_num
        comp_num = random.randint(lower_comp_num, greater_comp_num-1)

    elif comp_num < user_num:
        if (user_num - comp_num) >= 5:
            number_of_turns += 1
            print("You are smaller than the my number but within 5 numbers")
            lower_comp_num = comp_num
            comp_num = random.randit(lower_comp_num, user_num)
        print(comp_num, "this number is smaller than my number")
        number_of_turns += 1
        lower_comp_num = comp_num
        comp_num = random.randint(lower_comp_num+1, greater_comp_num)

    else:
        print("You guessed my number!")
        break

print("It took the computer ", number_of_turns, "to get the corret number")

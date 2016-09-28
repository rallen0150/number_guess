# Normal Part
import random

class NumberGuess:
    def __init__(self):
        self.number_of_turns = 0
        self.comp_num = random.randint(1, 100)
        self.user_num = 0

    def pick_num(self):
        self.user_num = int(input("Guess a number between 1-100: "))

    def check_comp_num(self):
        if self.user_num < self.comp_num:
            if (self.user_num + 5) >= self.comp_num:
                print("You are smaller than the computer's number but within 5 numbers")
            print ("This number is smaller than the computer's number")
            self.number_of_turns += 1

        elif self.user_num > self.comp_num:
            if (self.user_num - 5) <= self.comp_num:
                print("You are greater than the computer's number but within 5 numbers")
            print ("This number is greater than the computer's number")
            self.number_of_turns += 1

        else:
            print ("That is the correct number!")
            self.number_of_turns += 1


    def normal_gameplay(self):
        while self.number_of_turns < 5 and self.user_num != self.comp_num:

            self.pick_num()
            self.check_comp_num()


        print ("It took you {} turns".format(self.number_of_turns))
        print("The correct number was {}".format(self.comp_num))

    def comp_guess_num(self):
        if self.comp_num > self.user_num:
            print(self.comp_num, "this number is greater than my number")
            self.number_of_turns += 1
            self.greater_comp_num = self.comp_num
            self.comp_num = random.randint(self.lower_comp_num, self.greater_comp_num)

        elif self.comp_num < self.user_num:
            print(self.comp_num, "this number is smaller than my number")
            self.number_of_turns += 1
            self.lower_comp_num = self.comp_num
            self.comp_num = random.randint(self.lower_comp_num, self.greater_comp_num)

        else:
            print("You guessed my number!")

    def hard_gameplay(self):
        self.number_of_turns = 0

        self.pick_num()

        self.comp_num = random.randint(1, 100)
        self.greater_comp_num = 100
        self.lower_comp_num = 0

        while self.user_num != self.comp_num and self.number_of_turns <5:

            self.comp_guess_num()
        print("It took the computer {} turns.".format(self.number_of_turns))


game = NumberGuess()
game.normal_gameplay()

# Hard Part and Very Hard Part

game.hard_gameplay()

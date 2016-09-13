
import random

print(random.randint(1, 20))

robbies_age = input("How old are you? ")
robbies_age = int(robbies_age)
sarahs_age = 34

# Boolean
print(robbies_age > sarahs_age)

if robbies_age > sarahs_age:
    print("you is older than sarah")
elif robbies_age == sarahs_age:
    print("you is the SAME age as sarah")
else:
    print("you is NOT older than sarah")

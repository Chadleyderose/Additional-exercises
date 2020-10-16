import random

random_num = random.randint(1,100)
guess = 1
while True:
    guess_num = int(input("Please enter any number between 1-100: "))
    if guess_num == random_num:
        print("Congratulations, that is correct! ")
        print("Number of tries: ", guess)
        exit()
    elif guess_num > random_num:
        print("try a higher number")
        guess = guess + 1
    elif guess_num < random_num:
        print("try a smaller number")
        guess = guess + 1

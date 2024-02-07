command = input("Enter let's try to guess or stop to quit the game ")
import random
lmn_number = random.randint(1, 10)
while command == "let's try":
    guess_number = int(input("Guess any Number"))
    if guess_number < lmn_number:
        print("Your guess is Too Low")

    elif guess_number > lmn_number:
        print("Your guess is too high")

    else:
        print("Your guess is correct")
        break
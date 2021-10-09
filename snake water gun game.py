import random
list = ["s","w","g"]


total_chances = 10
no_of_chances = 0
computer_score = 0
human_score = 0
print("snake water gun game \n")
print("s for snake \nw for water \ng for gun\n")

while(no_of_chances<total_chances):
    _input = input('snake,water,gun:')
    _random = random.choice(list)

    if(_input==_random):
        print("Tie 0 to both \n")

    elif _input=="s" and _random == "g":
        computer_score = computer_score+1
        print(f"Computer guess is {_random} and your guess {_input}")
        print("Computer wins!")
        print(f"Computer score is {computer_score} and your score is {human_score}")


    elif _input=="g" and _random == "s":
        human_score = human_score+1
        print(f"Computer guesses is {_random} and your guess {_input}")
        print("You win!")
        print(f"Computer score is {computer_score} and your score is {human_score}")

    elif _input=="w" and _random == "g":
        human_score = human_score+1
        print(f"Computer guesses is {_random} and your guess {_input}")
        print("You win!")
        print(f"Computer score is {computer_score} and your score is {human_score}")

    elif _input=="g" and _random == "w":
        computer_score = computer_score + 1
        print(f"Computer guesses is {_random} and your guess {_input}")
        print("Computer win!")
        print(f"Computer score is {computer_score} and your score is {human_score}")

    elif _input=="s" and _random == "w":
        human_score = human_score + 1
        print(f"Computer guesses is {_random} and your guess {_input}")
        print("You win!")
        print(f"Computer score is {computer_score} and your score is {human_score}")

    elif _input=="w" and _random == "s":
        computer_score = computer_score + 1
        print(f"Computer guesses is {_random} and your guess {_input}")
        print("computer win!")
        print(f"Computer score is {computer_score} and your score is {human_score}")

    else:
       print("Enter valid input ")

    no_of_chances = no_of_chances+1
    print(f"{total_chances-no_of_chances} is left out of {total_chances}\n")

print("Game over")


if computer_score==human_score:
    print("computer wins")

elif computer_score>human_score:
    print("Computer  win")

else:
    print("You  win")

print(f"your score is {human_score},Computer score is {computer_score}")
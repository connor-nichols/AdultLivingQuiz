import replit
from time import sleep
import os
import csv
import requests
import random
download = requests.get("https://docs.google.com/spreadsheets/d/e/2PACX-1vTTmATPOvOyQ3J4qu6tsK5vxs8X4rkFRk9L5SRtqvEK0Z3w5ROdaeX2CvQjaVjZPcTo4SCK-EWB1ZOf/pub?gid=0&single=true&output=csv")

decoded_content = download.content.decode('utf-8')
cr = csv.reader(decoded_content.splitlines(), delimiter=',')
my_list = list(cr)

chosen_questions = []
for x in range(0,10):
    valid = False
    while not valid:
        attempt = random.randint(1,len(my_list) - 1)
        if attempt not in chosen_questions:
            chosen_questions.append(attempt)
            valid = True


debug = True
end_game = False

while end_game is False:
    menu_option = input("Do you want to view the (L)eaderboard or (P)lay the game? Press L or P then ENTER.")

    if menu_option.lower() == "l":
        pass
    elif menu_option.lower() == "p":

        player_name = input("What do you want your display name to be?")
        player_score = 0

        print("You will recieve 10 random questions about paychecks and taxes. Each correct answer is worth 100 points")

        for q in chosen_questions:
            replit.clear()
            print("\n" + my_list[q][0]) # Presents the question
            question = my_list[q][0]
            correct = int(my_list[q][5])
            if debug:
                print(my_list[q][5])
            for x in range(1, 5):
                print(f"Choice {x}: {my_list[q][x]}")
            
            choice = None
            while isinstance(choice,int) is False:
                choice = input("Choose a number.")
                try:
                    choice = int(choice)
                except ValueError:
                    print(f"\"{choice}\" is not a number. Try again.")

            if choice == correct:
                player_score += 100
                print(f"Correct. Your current score is {player_score}")
            else:
                print(f"Incorrect. The correct answer to \"{question}\" is {correct}: \"{my_list[q][correct]}\"")

            sleep(1.5)

        print(f"Your final score was {player_score}.")

        end_game = True

    else:
        print(f"\"{menu_option}\" is invalid. Pleas try again")
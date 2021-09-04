#Import needed libraries
import datetime
import json
import random

#A new class "Result"
class Result:
    def __init__(self, attempts, player_name, date):
        self.attempts = attempts
        self.player_name = player_name
        self.date = date

#Define a function "the_game()"
def the_game():
    secret = random.randint(1,10)
    attempts = 0
    top_score_list = get_score_list()
    player_name = input("Hello! Please, tell me your name :) ")



    #Game asks the player to guess an int and any user's guess is stored as variable "guess". Any user's guess is stored as +1 "attempts".
    while True:
        guess = int(input(player_name + ", guess the secret number between 1 and 10: "))
        attempts += 1


        #If the user guesses the correct num, the game stops here (break), else it gives feedback - smaller or bigger
        if guess == secret:
            #Class "Result" stores into an "result_obj" variable, as an object.
            result_obj = Result(attempts=attempts, player_name=player_name, date=str(datetime.datetime.now()))

            #If the user guesses correct, append "result_obj" into the top_score_list
            top_score_list.append(result_obj.__dict__)

            #Open and write the new attempt into the "top_score.json" file
            with open("top_score.json", "w") as score_file:
                score_file.write(json.dumps(top_score_list))

            print("You are correct! It's number " + str(secret))
            print("Attempts needed " + str(attempts))
            break
        elif guess > secret:
            print("Your guess is incorrect, try something smaller.")
        elif guess < secret:
            print("Your guess is incorrect, try something bigger.")

#Define a function "get_score_list()", which opens and reads a "top_score.json"file. 
def get_score_list():
    with open("top_score.json", "r") as score_file:
        top_score_list = json.loads(score_file.read())
        return top_score_list

#Define a function "get_top_scores()"
def get_top_scores():

    #"top_score_list" is a variable, whose value is a "get_score_list()" function.
    top_score_list = get_score_list()
    #"the_best_score_list" gets sorted and it only returns best 3 attempts.
    the_best_score_list = sorted(top_score_list, key=lambda k: k['attempts'])[:3]
    return the_best_score_list

#Defined a variable "selection", which takes an input as a value.
while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")

    #If the user chooses "A", the Guessing game starts (the_game())
    if selection.upper() == "A":
        the_game()
    #Else if the useer chooses "B", the program show the best results
    elif selection.upper() == "B":
        #For every "score_dict" in "get_top_scores()", print user name, attempt and it's date and time
        for score_dict in get_top_scores():
            result_obj = Result(attempts=score_dict.get("attempts"),
                                player_name = score_dict.get("player_name", "Anonymous"),
                                date = score_dict.get("date"))
                                
        
        print("Player: {name}; Attempts: {attempts}; Date: {date}".format(name=result_obj.player_name,
                                                                          attempts=result_obj.attempts,
                                                                          date=result_obj.date))
           
    #Else if the user chooses "C", quit the game with a message.
    else:
        print("Thank you for playing!")
        break
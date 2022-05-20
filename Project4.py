'''
Created on May 19, 2022

@author: Tiearney Beltz

Objective : Playing rock, paper, scissors against your CPU. 
'''
import random 
keepPlaying = True 

while (keepPlaying): 
    print("Welcome to rock, paper, scissors!")
    print("Best two of three wins. Press q to quit.")
    
    cpuScore = 0 
    userScore = 0

    while (userScore < 2 and cpuScore < 2): 
        choice = input("Please choose : rock, paper, or scissors")
        choiceList = ["rock", "paper", "scissors"]
        cpuChoice = random.choice(choiceList) 
        if(choice.lower() == 'q'): 
            keepPlaying = False 
            break 
        elif((choice.lower() == cpuChoice) or (choice.lower() == cpuChoice) or (choice.lower() == cpuChoice)): 
            print("DRAW")
            print("User:" + str(userScore) + " CPU: " + str(cpuScore)) 
        elif((choice.lower() == "scissors" and cpuChoice == "paper") or (choice.lower() == "scissors" and cpuChoice == "paper") or (choice.lower() == "paper" and cpuChoice == "rock")):
            userScore = userScore + 1
            print("User: " + str(userScore) + "CPU: " + str(cpuScore))
        elif((choice.lower() == "rock" and cpuChoice == "paper") or (choice.lower() == "scissors" and cpuChoice == "rock") or (choice.lower() == "paper" and cpuChoice == "scissors")):
            cpuScore = cpuScore + 1
            print(" user: " + str(userScore) + " CPU: " + str(cpuScore))
        else:
            print("Not an option, try again.")
    
    print("Thanks for playing!")
    if(userScore == 2):
        print("You WIN!")
    elif(cpuScore == 2):
        print("You LOSE!")
    print("User: " + str(userScore) + " CPU: " + str(cpuScore))
    
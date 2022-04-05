'''
Created on Apr 4, 2022

@author: ITAUser
'''
#Make a variable called score to keep track of the correct answers. And set
#it to 0.
score = 0 
#Ask the user question one. And store the users answer.
print("What is the powerhouse of the cell?")
questionOne = input("enter a letter : A) Mitochondria B) Nucleus C) Ribozone")
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."
if (questionOne.upper()== "A"):
    score = score + 1 
    print("correct")

else:
    print("Incorrect, the correct answer is A.")
#Ask the user question two. And store the users answer.
print("How many states compromise the United States?")
questionTwo = input("enter a letter : A) 13 B) 45 C) 50")
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."
if (questionTwo.upper()== "C"):
    score = score + 1
    print("correct")
    
else:
    print("Incorrect, the correct answer is C.")
#Ask the user question three. And store the users answer.
print("In y = mx+b, what does m stand for?")
questionThree = input("enter a letter : A) Slope B) Output C) I don't understand math")
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."
if (questionThree.upper()== "A"):
    score = score + 1 
    print("correct")
    
else:
    print("Incorrect, the correct answer is A.")
#Ask the user question four. And store the users answer.
print("In English a person, place or thing is called a?")
questionFour = input("enter a letter : A) Verb B) adjective C) noun")
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."
if (questionFour.upper()== "C"):
    score = score + 1
    print("correct")
    
else:
    print("Incorrect, the correct answer is C.")
#Calculate the percentage the user got. And store it in a variable called p
p = score/4
#Print out the users score: "You got a [score]/4. Or a [p]%."
print("You got a " + str(score) + "/4. or a " + str(p) + "%")
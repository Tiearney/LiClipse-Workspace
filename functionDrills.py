'''
For this assignment you should read the task, then below the task do what it asks you to do.
For tasks with return statements, you can test out if you are correct by putting in some parameters
and printing what is returned outside of the function.

EXAMPLE TASK:
'''
#EX) Define a function that has two parameters. Make the function add the two
#numbers together and return the result.
from pickle import TRUE
def add_two_numbers(num1, num2):
    sumOfTwoNumbers = num1 + num2
    return sumOfTwoNumbers

'''
END OF EXAMPLE
'''

'''
START HERE
'''


#1) Define a function that has two int parameters. Make the function subtract 
#the first parameter minus the second one. Then, return the result. Now call 
#the function.
#Print what the function returns.

def minus_two_numbers(x,y):
    difference = x - y 
x = 8   
y = 3 
difference = minus_two_numbers(x,y)
print(difference)
    

#2) Define a function that has one parameter. Make the function divide the 
#parameter by 2, multiply it by 77, and then add 10,000. Return the result.
#Now call the function.
#Print what the function returns.

def number (x):
    answer = x / 2 * 77 + 10000
    return answer 
x = 25 
answer = number (x)
print(answer)

#3) Define a function that has two int parameters. Make the function check if 
#two numbers are equal. If they are equal, return true. If they are not equal, 
#return false. Now call the function.
#Print what the function returns.

def answer (x,y):
    if x == y: 
        return True
    else : 
        return False 
x = 2
y = 3 
print(answer(x,y))

#4) Define a function that has two int parameters. Make the function
#check which parameter is bigger, and return the bigger parameter. 
#If they are the same, it should just return either parameter. Now call the 
#function.
#Print what the function returns.

def answerOne(s,w):
    if s > w:
        return s 
    elif w > s: 
        return w 
    else: 
        return s 
s = 20 
w = 23 
print(answerOne(s,w))

#5) Define a function that has two string parameters. Make the function
#add the two strings together. And then return the combined string. Now call 
#the function.
#Print what the function returns.

def addingStrings(c,b):
    sumOfAdding = c + b 
    return sumOfAdding 
c = "Tiearney"
b = "beltz"
sumOfAdding = addingStrings(c,b)
print(sumOfAdding)

#6) Define a function that has three int parameters. If the first number is 
#equal to the second OR the third number, return true. Else, return false. Now 
#call the function.
#Print what the function returns.

def number_three(x,y,z):
    if x == y or x == z: 
        return True 
    else:
        return False 
x = 22
y = 24
z = 22 
print(number_three(x,y,z))

#7) Define a function that prints your name. It should have no parameters and 
#shouldn't return anything. Now call the function.

def name():
    print("Tiearney Beltz")
    return 
name()

#8) Define a function that has one string parameter. The string should be a
#color. If that string is equal to your favorite color, it prints "That's my 
#favorite color!". If it is not, it prints "That is not my favorite color. 
#Try again.". It shouldn't return anything. Now call the function.

def color(x):
    if x == "blue":
        print("That's my favorite color!")
    else:
        print("Try again.")
        return 
    color("blue")

#9) Define a function that has one int parameter. The int should be 
#positive. If the number is not equal to zero, the function runs a loop that
#decrements the parameter by 1 and prints it each time. Now call the function.

def numberFour(x):
    while (not x == 0):
        x = x - 1
        print(x)
        return 
    numberFour(8)  
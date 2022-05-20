'''
For this assignment you should read the task, then below the task do what it asks you to do
based on what the task tells you do first.
EXAMPLE TASK:
'''
#EX) Declare a variable set to 3. Make a while loop that prints the variable 
#    you just created and decrements the variable by one each time through
#    the loop. Meanwhile, make the loop run until the variable you created 
#    equals 0.
i = 3;
while i > 0:
    print(i)
    i -= 1

'''
END OF EXAMPLE
'''

'''
START HERE
'''

'''While Loops'''
#1) Declare a variable set to 4. Make a while loop that prints the variable 
#    you just created and decrements the variable by one each time through
#    the loop. Meanwhile, make the loop run until the variable you created 
#    equals 1.

x = 4
while (x > 1):
    print(x) 
    x -= 1 

#2) Declare a variable set to 14. Make a while loop that prints the variable 
#    you just created and increments the variable by one each time through
#    the loop. Meanwhile, make the loop run until the variable you created 
#    equals 20.

s = 14 
while (s < 20):
    print(s)
    s = s + 1 
#3) Declare a variable set to 55. Make a while loop that prints the variable 
#   you just created. Then make an if statement that makes the loop break when
#   the variable is equal to 50. 

e = 55
while (e < 100): 
    print(e)
    e = e + 1
    if (e == 50):
        break
 

'''For Loops'''
#4) Create a list named sports. Put three sports into the list. Create
#   a for loop that prints each sport in the list

sports = ["volleyball", "basketball", "tennis"]
for x in sports: 
    print(x)

#5) Create a for loop that loops through each letter in a string of one of your
#   favorite songs. Each iteration should print should a letter of the word. 

song = "waves"
for x in song:
    print(x)
#6) Create a list named movies. Put five of your favorite movies into the list.
#   However, make sure one of the movies is Avatar. 
#   Create a for loop that iterates over the list. In the loop print the movie
#   being looped over, but create an if statement that breaks out of the 
#   loop if it is Avatar.

movies = ["star wars", "Jurassic", "Avatar", "toy story", "barbie"]
for x in movies:
    print(x)
    if (x == "Avatar"):
        break




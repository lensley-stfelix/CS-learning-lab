#I'm now learning about looping. 
#this is a simple while loop
#it saying "while this expression is true"
#keep running the statememnt in the body of the loop, over and over again
#untill it is false and move on to the next statememnt outside te body of the loop.
myNum = 5 
while myNum > 0:
     myNum = myNum - 1
     print(myNum)
print("Our loop is done")

#Iteration Variable:
     #The variable that changes each time the loop executes
     #and controls when the loop finishes
myNum = 0
while myNum > 0:
     myNum = myNum - 1
     print(myNum)
print("Our loop did nothing")

#I'm now learing Basics of a for Loop
#Python’s for loop is a data collection-based iteration 
#(meaning it loops through iterable objects such as
#lists, sets, tuples, dictionaries, and even strings)

productList = ("card", "paper", "glue", "pencil")
for product in productList:
  print(product)
#I'm wrting a for loop using the range function
for counter in range(0,5):
    print("Counter is set to:",counter)
    
for counter in range(5):
   print("Counter is set to:",counter)
   
for counter in range(1,5):
    print("Counter is set to:",counter)

for counter in range(-2,3):
    print("Counter is set to:",counter)
#we can add a third parameter to cnage the increment or decrement
for counter in range(10,1,-2):
    print("Counter is set to:",counter)
    
# we can use a for loo through strings

for char in "Python":
   print(char)
   
for pet in ("dog","cat","fish"):
  print(pet)
  
  
 # Here is a simple program that counts down from five and then says “Blastoff!”
 
myNumber = 6 
while myNumber > 0: 
    myNumber = myNumber - 1
    print(myNumber)
print("Blastoff!")


textEntered = ""
stringBuilder = ""
while textEntered != "quit":
  textEntered = input("Enter in a string, enter quit to exit the loop:")
  if textEntered != "quit":
    stringBuilder += textEntered + " "
print(stringBuilder)

#im learning  break and continue Statements

myNumber = 6
while myNumber > 0:
    myNumber = myNumber - 1
    if myNumber == 2:
        break
    print(myNumber)
print('Blastoff!')

#The continue statement will end the current loop
#iteration, meaning that the execution jumps back 
#to the top of the loop. The expression is then evaluated 
#to determine if the
#loop will execute again or end there

myNumber = 6
while myNumber > 0:
    myNumber = myNumber - 1
    if myNumber == 2:
        continue
    print(myNumber)
print('Blastoff!')


kisses = 0
while kisses < 10:
    kisses = kisses + 1
    print(kisses)
print("No more kisess Mister wink, wink ")

#When we have a collection of things to loop through, 
#we can construct a definite loop using a for loop. 

friendsList = ['Joseph', 'Glenn', 'Sally']
for friend in friendsList:
    print('Happy New Year:', friend)
print('Done!')
#remember : Looking at the for loop, [[for]] and [[in]] are reserved Python keywords, 
#Any time that we need to look at each element
#within a list can be a scenario to use a for loop.

countItems = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    countItems = countItems + 1
print('Count: ', countItems)


#Another similar loop that computes 
#the total of a collection of numbers is as follows aka accumulator.

totalItems = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    totalItems = totalItems + itervar
print('Total: ', totalItems)

#im learning Nested loops (a loop within a loop)






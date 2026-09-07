#Im learning list, loops and complex funtions now 
# im also creating a tic tac toe program
#this is unit 2 of my python learning 
#list example 


petsList = ['dog', 'cat', 'fish']
print(petsList[-2])

#operators example of in 
petsList = ['dog', 'cat', 'fish']
print( "dog" in petsList)

#The assignment operator changed the value.
petsList = ['dog', 'cat', 'fish']
petsList[1] = 'hamster'
print(petsList)

petsList = ['dog', 'cat', "hotdog", "banana", "salmon", "dollar", 'fish']
petSLice = petsList[:3]
print(petSLice)


petsList = ['dog', 'cat', "hotdog", "banana", "salmon", "dollar", 'fish']
petSLice = petsList[1:5]
print(petSLice)

petsList = ['dog', 'cat', "hotdog", "banana", "salmon", "dollar", 'fish']
petSLice = petsList[:]
print(petSLice)

#We can also use the slices to replace and update multiple elements within a list at once.
petsList = ['dog', 'cat', 'fish','rabbit','hamster','bird']
petsList[1:3] = ['dinosaur','robot']
print(petsList)

#I'm learning about methods and functions 
#How to manipulate list after they are created in pyt
#this is really important 
#they are append,insert, extend, sort, pop, del, remove

petsList = ['dog', 'cat', "hotdog", "banana", "salmon", "dollar", 'fish']
petsList.append("elephant")
print(petsList)

petsList = ['dog', 'cat', "hotdog", "banana", "salmon", "dollar", 'fish']
petsList.insert(0,"crocodile")
print(petsList)

firstPetsList = [ "dog", "crocodile", "birds"]
secondPetsList = ["ants", "worms", "snakes", "kangaroo"]
firstPetsList.extend(secondPetsList)
print(firstPetsList)

petsList = ["dog", "zebra", "birds", "bees", "whales"]
petsList.sort()
print(petsList)

petsList = ["dog", "zebra", "birds", "bees", "whales"]
soldPets = petsList.pop(3)
print("Remaining: ", petsList)
print("Sold: " , soldPets)

petsList = ["dog", "zebra", "birds", "bees", "whales"]
soldPets = petsList.pop(0)
print("Remaining: ", petsList)
print("Sold: " , soldPets)

petsList = ["dog", "zebra", "birds", "bees", "whales"]
del petsList[4]
print( "Remaining : ", petsList)

petsList = ["dog", "zebra", "birds", "bees", "whales"]
del petsList[0]
petsList.sort()
print( "Remaining : ", petsList)


petsList = ["dog", "zebra", "birds", "bees", "whales"]
petsList.remove("zebra")
petsList.sort()
print( "Remaining : ", petsList)

#Im learing about functions used on list that are helpful
numList = [2, 45, 9, 17, 1, 4]
print("Max: ",max(numList))
print("Min: ",min(numList))
print("Length: ",len(numList))
print("Sum: ",sum(numList))
print("Average: ",sum(numList)/len(numList))


#I'm learing about Iterables and Iterators
# (sets, tuples, and dictionaries, are iterable types and use iterators.

numList = [99,1,14,35,46,28,21]
listElement = iter(numList)
print(next(listElement))
print(next(listElement))
print(next(listElement))
print(next(listElement))
print(next(listElement))
print(next(listElement))
print(next(listElement))

myString = "Lensley"
listElement = iter(myString)
print(next(listElement))
print(next(listElement))
print(next(listElement))

# im learning about sets, list, tuples, and dictionaries.

myPets = {"dog","cat","rabbit"} #this is the set
yourPets = ["dog","dog","fish"] #this is the list
myPets.update(yourPets)
print(myPets)

myPets = {"dog","cat","rabbit"}
myPets.discard("dog")
print(myPets)
myPets.discard("dinosaur")
print(myPets)

#Remember that a tuple cannot be changed. 
#If we tried to use the assignment operator
#to change an element, we’ll get an error.

myTuple = ("ice cream","frozen yogurt","sorbet")
print(myTuple)

lonelyTuple = ("ice cream",)
print(lonelyTuple)
print(type(lonelyTuple))

myTuple = ("fun",10,-2.0,"sun")
print(myTuple)
print(type(myTuple))


#here we turned a tuple into a list, added an item and return back to tuple
myTuple = ("ice cream","frozen yogurt","sorbet")
myList = list(myTuple)
myList[1] = "gelato"
myTuple = tuple(myList)
print(myTuple)


#Dictionaries = structured key:value storage


eng2span = dict()
eng2span['one'] = 'uno'
print(eng2span)

#this is a dictionary with three elements.
eng2span = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2span)


#I'm now learning about multiple dimensions 
#nestedList = [[1, 2], [3, 4, 5], [6]]

#A 2D list is a nested list where every inner list
#has the same number of element.
#twoDList = [[1, 2, 3],
#            [4, 5, 6],
 #           [7, 8, 9]]


multiplesList = [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
print(multiplesList)


multiplesList = [[1, 2, 3, 4, 5],
[2, 4, 6, 8, 10], 
[3, 6, 9, 12, 15], 
[4, 8, 12, 16, 20]]
print(multiplesList[0])


multiplesList = [[1, 2, 3, 4, 5], 
[2, 4, 6, 8, 10], 
[3, 6, 9, 12, 15], 
[4, 8, 12, 16, 20]]
print(multiplesList[0][2])

multiplesList = [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
print(multiplesList[2][3])

multiplesList = [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
print(multiplesList[1][4])


multiplesList = [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
multiplesList.append([5, 10, 15, 20, 25])
print(multiplesList)

#If we wanted to append an element to an inner list
#(a list within the outer list), we can use the .append() method and an index
#value like the following.

multiplesList = [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
multiplesList[0].append(6)
print(multiplesList)  


multiplesList = [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
multiplesList[0].extend([6, 7, 8])
print(multiplesList)

#Debugging is what im learning now 

myString = " Fun things for Us "
myString = myString.strip()
print(myString)


myList = ["ice cream","frozen yogurt","sorbet"]
myList.sort()
print(myList)



myFirstList = ["ice cream","frozen yogurt","sorbet"]
myElement = "gelato"
myFirstList.append(myElement)
print(myFirstList)


myFirstList = ["ice cream","frozen yoogurt","sorbet"]
myElement = "gelato"
myFirstList = myFirstList + myElement
print(myFirstList)

myFirstList = ["ice cream","frozen yogurt","sorbet"]
anotherList = myFirstList[:]
anotherList.sort()
print(anotherList)
print(myFirstList)








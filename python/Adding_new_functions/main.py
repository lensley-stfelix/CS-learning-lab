#remember a function takes an argument and return a results. 
#the result is called the return value
#The keyword def indicates that this is a function definition. 
#We are telling Python that we are defining a new function with this keyword.

#def myFunction():

def print_stuff():
    print("#######################")
    print('Using for comment block')
    print("#######################")
print(type(print_stuff))

#If we check the type of the print_stuff() function, we can see that type “function” is returned.

def print_stuff():
    print("#######################")
    print('Using for comment block')
    print("#######################")
print_stuff()

#here are examples of math functions, single arrguments and double arguments 
import math
print(math.sin(0))

import math
print(math.pow(3,3))

#im learning return functions
#Return values = reusable data
#Print statements = temporary display



def print_total(a, b):
    print(a + b)

def return_total(a, b):
    return a + b

print_total(5, 5)          # prints 10
x = return_total(5, 5)
print(x * 2)               # prints 20

# im learning Explicit Return

def calculate_average(numbers):
  return sum(numbers)/len(numbers)
print(calculate_average([10, 20, 30, 40]))

def calculate_average(numbers):
 my_avg = sum(numbers)/len(numbers)
 return my_avg
print(calculate_average([1,2,3,4]))


#⭐mlutiple return values work
def calculate_stats(numbers):
    total = sum(numbers)
    length = len(numbers)
    average = total / length
    return total, length, average

#Return With Conditionals
def calculate_absolute(number):
  if number >= 0:
    return number
  else:
    return -number 
print(calculate_absolute(-5))
print(calculate_absolute(5))
print(calculate_absolute(0))


# im learning nested functions 

def outer_func():
  def inner_func():
    print("Outputting from the inner function")
  inner_func() #call to the inner function
outer_func() #call to the outer function

def outer_func(what):
  def inner_func():
    print("I like", what)
  inner_func()
outer_func("Python")
# im learning nested recursions 

def countdown(n):
    if n == 0:        # base case
        return
    else:
        print(n)
        countdown(n - 1)   # recursive call
        
#im learning how to calculate factorial using recursion inside a nested function.     



#The isinstance() function checks whether a variable is a certain data type. It returns True or False. 
#isinstance(number, int)
#What raise does
#raise immediately stops the function and triggers an error.
#It’s like saying:“Stop everything — something is wrong.”

def factorial(number):
  if not isinstance(number, int):
    raise TypeError("Sorry. number must be an integer.")
  if number < 0:
     raise ValueError("Sorry. number must be zero or positive.")
  def inner_factorial(number): #nested function for calculation of factorial 
     if number <= 1:
        return 1
     return number * inner_factorial(number - 1)
  return inner_factorial(number)
print(factorial(4))

#Im learning debugging functions 
#we don’t always want to read from top to bottom. Sometimes it makes more
#sense if we follow the flow of execution.
#always remember A function must be defined before it is called

def function_4(num):
   if num > 1:
      num = num - 2
   else:
      num = num + 2
   return num
   
def function_3(num):
   if num > 1:
      num = num / 2
   else:
      num = num / -2
   return num
    
def function_2(num):
   if num > 1:
      num = num * 2
      num = function_3(num)
   else:
      num = num * -2
      num = function_4(num)
   return num
   
def function_1(num):
   if num > 0:
      num += 1
      num = function_2(function_3(num))
   else:
      num -=1
      num = function_2(function_4(num))
   return num
print('output = ', function_1(5))



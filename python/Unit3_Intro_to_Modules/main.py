import math
print(math.pi)
print(math.sqrt(25))

from math import pi, sqrt
print(pi)
print(sqrt(25))

import math as m 
print(m.pi)

from math import * 
print(pi)

import random

print("___________________________")

print("___________________________")


print("random():", random.random())
print("random():", random.random()*100)

print("randint(1, 5):", random.randint(1, 5))
print("randrange(1, 10):", random.randrange(1, 10))

print("___________________________")

import temperature
temp = 20

print(temp, "Celsius =", round(temperature.to_fahrenheit(temp)), "Fahrenheit")
print(temp, "Fahrenheit =", round(temperature.to_celsius(temp)), "Celsius")

help (temperature)
print("___________________________")

fhandler = open('poem.txt')
print(fhandler)

#im instructing python to read the file, line by line.
fhandler = open('poem.txt')
count = 0
for line in fhandler:   ##Give me each line in the file, one at a time.
    count = count + 1
print('Line Count:', count)

print("___________________________")

fhandler = open('poem.txt')   ##.read() loads the entire file into memory as one big string.
text = fhandler.read()
print(text)
print("___________________________")
#Opening a file in write (‘w’) mode clears out the old data and starts fresh.
fout = open('output.txt', 'w')

line1 = "Putting in a line of text,\n"
fout.write(line1)
fout.write("Another line!\n")

#all the same, different variable name
fout = open('output.txt', 'w')
file_out = open('output.txt', 'w')
output_file = open('output.txt', 'w')
myfile = open('output.txt', 'w')

#reading a file 
fin = open('poem.txt', 'r')
for line in fin:
    print(line)
#writing a file 
fout = open('output.txt', 'w')
fout.write("I just created a new file,\n")
fout.write( "with some text inside of it.\n")
fout.close()


fout = open('firstexample.txt', 'a')
fout.write('Putting in a line of text\n')
fout.close()


fout = open('myfile.txt', 'w')
fout.write('My first line of text\n')
fout.write('My second line of text\n')
fout.write('My third line of text\n')
fout.write('My fourth line of text\n')
fout.close()

##A file object behaves like a list of lines.
##So looping over it automatically 
##reads each line using .readline() internally.

print("__________0_________________")

fin = open('myfile.txt', 'r')
for line in fin: 
    print(line, end="")

print()
fin.close()
print("__________0_________________")

print("__________1_________________")

#.read() pulls everything into a single string, 
#including the newline characters (\n) that separate each line.
fin = open('myfile.txt', 'r')
contents = fin.read()
print(contents)
fin.close()
print("__________1_________________")

print("__________2_________________")

#.readline() returns just one line, 
#stopping at the newline character.
fin = open('myfile.txt', 'r')
line1 = fin.readline()
line2 = fin.readline()
print(line1)
print(line2)
fin.close()
print("__________2_________________")

print("_____________3______________")



#.readlines() loads every line from the file, 
#but instead of one big string, 
#it returns a Python list 
#where each element is one line.
fin = open('myfile.txt', 'r')
lines = fin.readlines()
print(lines)
fin.close()

print("_____________4______________")
#Now I’m learning how to take a Python list
#and write each item into a text file.
#I write a list 
#I open a new file in write mode.
#I loop through the list. 
#I write each name to the file.
#I close the file.

names = ["Lensley", "Lenes", "John"]
fout = open("names.txt", "w")
for m in names:            #m is the name (like "Sophia")
    fout.write(m + "\n")   #+ "\n" adds a newline character at the end
fout.close()
print("_____________3______________")
print("_____________4______________")

#“Now I’m learning how to read 
#the names back out of the names.txt
# I start with an empty list in read mode 
#I open the file in read mode
#Each line in the file stills end with a newline character. 
names = [] 
fin = open("names.txt", "r")
#i loop through each line in the file 
for line in fin:     #the newline character is still attach
    line = line.replace("\n", "")   #replace looks for("A", replace with "B") 
    names.append(line)     # i append the clean names (no newline character) to the list [A,B,C]
print(names)                # i print the list 

fin.close()  #I close the file
print("_____________4______________")
print("_____________5______________")

#I’m writing non‑string data to a file 
#(python has to convert interger, float into strings )

years = [1975, 1979, 1983]
fout = open('years.txt','w')

for year in years:
    fout.write(str(year) + "\n")

fout.close()

print("_____________5______________")
print("_____________6______________")



years = []  # I have an empty list called years
fin = open('years.txt','r')    #i open a file called years in read mode

for line in fin:                   # i run the for loop, it reads each line inside the file. the file by default contains "\n" 
    line = line.replace("\n", "")  # this replaces the "new line with an empty string. therefore all the values inside the files have no "\n".it clean
    years.append(int(line))        # i use the int function to turn each string read by the loop into an interger, 
                                    # i also append them into a list called years [ interger1, interger2, interger3]

print(years)                        # show me my list 

fin.close()                     # im closing the file now 







#Writing a List to a Text File

names = ["John", "Python", "Sallie"]
fout = open('names.txt','w')

for m in names:
    fout.write(m + "\n")

fout.close()

#Reading the List Back From the File
names = []
fin = open('names.txt','r')

for line in fin:
    line = line.replace("\n", "")
    names.append(line)

print(names)
fin.close()

print("_____________Writing/Reading interger/floats______________")

#Writing Integers and Floats

years = [1975, 1979, 1983, 2026]
fout = open('years.txt','w')

for year in years:
    fout.write(str(year) + "\n")

fout.close()

#Reading Numbers Back From the File
years = []
fin = open('years.txt','r')

for line in fin:
    line = line.replace("\n", "")
    years.append(int(line))

print(years)
fin.close()


"""   #im disabling this function since it requires input. 
working with files 
import sys #this module gives me access to system level functions
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    sys.exit()
count = 0
for line in fhand:
    count = count + 1
print('There were', count, 'lines in', fname)
"""
print("__________________________________________________________")

print("_____________My First Employee Class Program______________")

import csv                        
import sys
FILENAME = "employees.csv"
#exiting the program
def exit_program():
    print("Terminating program.")
    sys.exit()    
    
#read the employees from the file, it loads the list of employees 
def read_employees():
    try:
        employees = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                employees.append(row)
        return employees
    except FileNotFoundError as error:
        print(f"Could not find {FILENAME} file.")
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program()


# this will write & save the list of our employees to the csv 
def write_employees(employees):
    try:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(employees) #This writes all rows at once.
    except Exception as e:   #Use a Catch‑All Exception, to catch other errors and exit 
        print(type(e), e)
        exit_program()

def add_employee(employees):
    empid = input("Enter the employee ID: ")            
    sal = input("Enter the salary of the employee: ")
    employee = [empid, sal]
    employees.append(employee)
    write_employees(employees)  #opens employees.csv in write mode, overwrites the file, writes all employees, includes the new one ensures persistence, This is how my program “remembers” new employees between runs.
    print(f"Employee {empid}: {sal} was added.\n")


#the function that actually displays the employees in a readable format.
def list_employees(employees):
    for i, employee in enumerate(employees, start=1):   #**“Go through the employees list   one employee at a time. For each employee, give me two things: the employee itself, and a counter number starting at 1.”**
        print(f"{i} Employee ID: {employee[0]} (${employee[1]})")  #Print the row number, then the words “Employee ID:”, then the employee’s ID, then the salary inside parentheses with a dollar sign.
    print()                                                        # #remember f is is a formatted string.It Replace anything inside {} with the actual value.”  
employees = read_employees()

#delete an employee 
def delete_employee(employees):
    found = False
    number = input("Enter in the employee ID: ")
    for i, employee in enumerate(employees, start=0):
        if (employee[0] == number):
            print(f"Employee was deleted.\n") 
            employee = employees.pop(i)  #pop(i) removes an item by index
            found = True
    if (found == False):
        print("Employee was not found.\n")
    else:
        write_employees(employees)

#“Show the user what commands they can type.”
def display_menu():   #Show the menu
    print("The Employee Salary List program")
    print()
    print("LIST OF COMMANDS")
    print("list - List all employees")
    print("add -  Add an employee")
    print("del -  Delete an employee")
    print("exit - Exit program")
    print()
    
    
    
    
    
    
# MAIN PROGRAM    
display_menu()  #Show the menu
employees = read_employees() #Load the employees list

while True:    #“Keep asking the user for commands until they type exit.
    command = input("Command: ")
    if command.lower() == "list":
        list_employees(employees)
    elif command.lower() == "add":
        add_employee(employees)
    elif command.lower() == "del":
        delete_employee(employees)
    elif command.lower() == "exit":
        break
    else:
        print("Not a valid command. Please try again.\n")

print("Ending Salary Program")






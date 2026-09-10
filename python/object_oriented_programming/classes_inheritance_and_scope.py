
#im learning class which is just 
#A blueprint that describes what an object should look like
#and how it should behave. 



class Dog:
  def __init__(self,name,breed,age,color):
    self.name = name
    self.breed = breed
    self.age = age
    self.color = color
  def bark(self):
    print("Woof")
  def fetch(self):
    print(self.name," went to fetch.")
    
    

# an instance of theSnipping Dog class
my_dog = Dog("Fluffy","Beagle",2,"Brown")
print(my_dog.name)
print(my_dog.breed)
print(my_dog.age)
print(my_dog.color)

my_dog1 = Dog("Fluffy","Beagle",2,"Brown")
my_dog2 = Dog("Mochi","Mutt",5,"White")
my_dog3 = Dog("Wolfie","Maltese",10,"Black")

#Attributes = data stored inside each object.
#Methods = functions inside a class.They are the actions.What the objects can do.
#when we use self, we can access the attributes and methods of a class.
class PeopleCounter:
   x = 0
   def anotherOne(self) :
     self.x = self.x + 1
     print("So far",self.x)
counter = PeopleCounter()  # creation of an instance of the class PeopleCounter
counter.anotherOne()
counter.anotherOne()



#i'm learning initiator __init__
#“__init__" is the method that runs when an object is created.
#It lets you give each object its own data. 
#Without it, every object would be identical. 
#Use self to attach attributes to the object.”

class User:
    def __init__(self, uname, pword):
        self.username = uname
        self.password = pword
        
account = User("sophia", "mypass")
print(account)
print(account.username)
print(account.password)
print(type(account))

#im deleting an object 
# Delete is typically used if
#you need to manage memory for performance purposes
class User:
  def __init__(self, uname, pword):
    self.username = uname
    self.password = pword
account = User('sophia','mypass')
print(account)
print(account.username)
#del account
print(account.password)
print(type(account))

#I learned how to set values to attributes and change those values after the instances have been created.
# how to set default values for attributes and change them afterwards if needed. 
#looked at importing the datetime module 

import datetime 
class User:
  def __init__(self, uname, pword):
    self.username = uname
    self.password = pword
    self.activeUser = True
    self.numOfLogins = 0
    self.dateJoined = datetime.date.today()

account = User('sophia','mypass')
account.activeUser = False
print(account.username)
print(account.password)
print(account.activeUser)
print(account.numOfLogins)
print(account.dateJoined)


import datetime 
class User:
  def __init__(self, uname, pword):
    self.username = uname
    self.password = pword
    self.activeUser = True
    self.numOfLogins = 0
    self.dateJoined = datetime.date.today()
  #display number of logins
  def show_num_logins(self):
    return self.username + " logged in " + str(self.numOfLogins) + " times."
account = User('sophia','mypass') #creating the instance from class User
print(account.show_num_logins()) #here is our method call

#####here is an explanation of what is happening in the code below ####

import datetime 
class User:
  def __init__(self, uname, pword):
    self.username = uname
    self.password = pword
    self.activeUser = True
    self.numOfLogins = 0
    self.dateJoined = datetime.date.today()
  #display number of logins
  def show_num_logins(self):
    return self.username + " logged in " + str(self.numOfLogins) + " times."
  #increase number of logins
  def logged_in(self):
    self.numOfLogins = self.numOfLogins + 1
account = User('sophia','mypass')
account.logged_in()
account.logged_in()
print(account.show_num_logins())
account.logged_in()
print(account.show_num_logins())

####Wow, this is a beautiful explanation.###############################
#When I write account = User("sophia", "mypass"), I’m creating a new User object.
#Python uses the class to set up all the attributes for that user.
#When I call account.logged_in(), I’m telling Python to run the method inside the class that increases the login count for that same object.
#Each time I call logged_in(), the number goes up by 1.
#When I call print(account.show_num_logins()), I’m telling Python to run the method that returns a sentence showing the username and the current login count.
#So after calling logged_in() three times, the output becomes:sophia logged in 3 times.
###########################################################################
#I create a User object with account = User('sophia','mypass').
#Python uses the class to set up all the attributes for this new user.

#Then I call account.login('sophia','mypass').
#Python checks if the username and password match what’s stored inside the object.
#If they match, it prints “Login successful” and increases the login count by calling logged_in().

#Finally, when I call print(account.show_num_logins()), Python runs the method that returns a sentence showing the username and the current login count.

#Each time I call login(), the login count goes up by 1.
#I’m not creating new objects — I’m updating the same one.
###########################################################################
import datetime 
class User:
  def __init__(self, uname, pword):
    self.username = uname
    self.password = pword
    self.activeUser = True
    self.numOfLogins = 0
    self.dateJoined = datetime.date.today()
  #display number of logins
  def show_num_logins(self):
    return self.username + " logged in " + str(self.numOfLogins) + " times."
  #increase number of logins
  def logged_in(self):
    self.numOfLogins = self.numOfLogins + 1
  #logging into the user account
  def login(self, uname, pword):
    if (self.username == uname and self.password == pword):
      print("Login successful")
      self.logged_in()
    else:
      print("Incorrect username and password combination.")
account = User('lens','mypass')
account.login('lens','mypass')
print(account.show_num_logins())





#I'm learning base class and subclass

import datetime 
class Member:
  expiry_days = -365
  def __init__(self, first, last):
    self.first_name = first
    self.last_name = last
    self.expiry_date = datetime.date.today() + datetime.timedelta(days = self.expiry_days)
    
TestMember = Member('Sophia','Python')
print(TestMember.first_name)
print(TestMember.last_name)
print(TestMember.expiry_date)

#example of subclass, with pass 

import datetime 
class Member:
  expiry_days = 365
  def __init__(self, first, last):
    self.first_name = first
    self.last_name = last
    self.expiry_date = datetime.date.today() + datetime.timedelta(days = self.expiry_days)
#Subclass for us to use for administrators
class Admin(Member):
  pass
#Subclass for us to use for normal users
class User(Member):
  pass
TestMember = Member('Sophia','Python')
print(TestMember.first_name)
print(TestMember.last_name)
print(TestMember.expiry_date)
TestAdmin = Admin('root','admin')
print(TestAdmin.first_name)
print(TestAdmin.last_name)
print(TestAdmin.expiry_date)
TestUser = User('Artic','Smith')
print(TestUser.first_name)
print(TestUser.last_name)
print(TestUser.expiry_date)

#in this class im adding new methods and overiding methods
import datetime

class Member:
    expiry_days = 365
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
        self.expiry_date = datetime.date.today() + datetime.timedelta(days=self.expiry_days)
    def show_expiry(self):
        return f'{self.first_name} {self.last_name} expires on {self.expiry_date}'

class Admin(Member):
    expiry_days = 365 * 10
    def __init__(self, first, last, level, secret):
        super().__init__(first, last)
        self.access_level = level
        self.secret_code = secret 
        

class User(Member):
    def __init__(self, first, last):
        super().__init__(first, last)
        self.expiry_days = 30
        self.expiry_date = datetime.date.today() + datetime.timedelta(days=self.expiry_days)
TestAdmin = Admin('root','admin', 10 , 'ABRACADABRA')
print(TestAdmin.access_level)  # 10
print(TestAdmin.expiry_date)   # updated 10 year renewal for admin
print(TestAdmin.secret_code)   # my added secret code for admin only
print(TestAdmin.first_name)
print(TestAdmin.last_name)
print(TestAdmin.show_expiry())
print("--------")
TestUser = User('Artic','Smith')
print(TestUser.expiry_days)    # 30
print(TestUser.show_expiry())
print("-----------------------------------------")

#now im learning about GLOBAL AND LOCAL SCOPE

first_name = 'Lensley'

def display_name():
    last_name = 'Doe'
    first_name = 'Lensley'
    return f"Inside the function: first_name = {first_name}, last_name = {last_name}"

print(display_name())
print(f"Outside the function: first_name = {first_name}")
print("-----------------------------------------")

#modify the global variable”
first_name = 'Lensley'

def display_name():
    last_name = 'Doe'
    global first_name
    first_name = 'Linsley'
    return f"Inside the function: first_name = {first_name}, last_name = {last_name}"

print(display_name())
print(f"Outside the function: first_name = {first_name}")

# help(Admin)

#Admin.__dict__ shows ONLY the attributes 
#and methods that belong directly to Admin — nothing inherited.
print("-----------------------------------------")
#Im creating an Employee class program, applying all the concepts learned.  
print("-----------------------------------------")


import datetime 
class Employee:
  def __init__(self, fname, lname, empid, title, sal):
    self.firstname = fname
    self.lastname = lname
    self.employeeid = empid
    self.jobtitle = title
    self.salary = sal
    self.hiredate = datetime.date.today()
  #returns first name
  def get_firstname(self):
    return self.firstname
  #sets firstname if fname isn't an empty string
  def set_firstname(self,fname):
    if len(fname) > 0:
      self.firstname = fname
  #returns last name
  def get_lastname(self):
    return self.lastname
  #sets lastname if lname isn't an empty string
  def set_lastname(self,lname):
    if len(lname) > 0:
      self.lastname = lname
  #returns job title
  def get_jobtitle(self):
    return self.jobtitle
  #sets job title if job title isn't an empty string
  def set_jobtitle(self,title):
    if len(title) > 0:
      self.jobtitle = title
  #return employee id
  def get_employeeid(self):
    return "Employee ID: " + str(self.employeeid)
  #returns salary
  def get_salary(self):
    return "${:,.2f}".format(self.salary)
    #sets salary if salary isn't an empty string
  def set_salary(self,sal):
    if sal > 0:
      self.salary = sal
  #increase salary
  def increase_salary(self,percent):
    if percent > 0:
      self.set_salary(self.salary + self.salary * percent)
    else:
      print("Increase of salary must be greater than 0.")


print("-----------------------------------------")
#Im creating a person class program, applying all the concepts learned.  
print("-----------------------------------------")


import datetime

class Person : 
    def __init__(self,fname,lname,title):
        self.firstname = fname
        self.lastname = lname
        self.jobtitle = title
        self.hiredate = datetime.date.today()
        
    def get_firstname(self):
        return self.firstname
        
    def set_firstname(self,fname):
        if len(fname) > 0:
            self.firstname = fname
    
    def get_lastname(self):
        return self.lastname
        
    def set_lastname(slef,lname):
        if len(lname) > 0: 
            self.lastname = lname
            
    def get_jobtitle(self):
        return self.jobtitle

    def set_jobtitle(self, title):
        if len(title) > 0:
            self.jobtitle = title

class Employee(Person):
    def __init__(self, fname, lname, title, sal, empid):
        super().__init__(fname, lname, title)
        self.employeeid = empid
        self.salary = sal
        self.vacationdaysperyear = 14
        self.vacationdays = self.vacationdaysperyear
        
    def get_employeeid(self):
        return "Employee ID: " + str(self.employeeid)
    
    def get_salary(self):
        return "${:,.2f}".format(self.salary)
        
    def set_salary(self, sal):
        if sal > 0 : 
            self.salary = sal
            
    def increase_salary(self, percent):
        if percent > 0:
            self.set_salary(self.salary + self.salary * percent)
        else: 
            print("Increase of salary must be greater than 0.")
    
    #Increase vacation days per year 
    def increase_vacation_days_per_year(self, days):
        if days > 0:
            self.vacationdaysperyear = self.vacationdaysperyear + days 
    #increase actual vacation days 
    def increase_vacation_days(self, days):
        if days > 0:
            self.vacationdays = self.vacationdays + days
    #increase vacation days by yearly amount 
    def increase_vacation_days_yearly(self):
        self.vacationdays = self.vacationdays + self.vacationdaysperyear 
    
    # take vacation days
    def take_vacation_days(self, days):
        if days > 0 and self.vacationdays - days >= 0:
            self.vacationdays = self.vacationdays - days
        elif days <= 0:
            print("Vacation days taken must be greater than 0.")
        elif self.vacationdays - days < 0:
            print(f"Employee does not have enough vacation days to take off {days} days.")    
 
emp1 = Employee('Jack','Krichen','Manager',50000,1)
print(emp1.get_firstname())
print(emp1.get_lastname())
print(emp1.get_employeeid())
print(emp1.get_jobtitle())
print(emp1.get_salary())
emp1.take_vacation_days(10)
emp1.take_vacation_days(10)
emp1.take_vacation_days(-1)
 
    
class Contractor(Person): 
    def __init__(self, fname, lname, title, conid, hrate):
        super().__init__(fname, lname, title)
        self.contractorid = conid 
        self.hourlyrate = hrate
        
    def get_contractorid(self):
        return "Contractor ID: " + str(self.contractorid)
        
    def get_hourlyrate(self):
        return"${:,.2f}".format(self.hourlyrate)
        
    def set_hourlyrate(self, rate):
        if rate > 0 : 
            self.hourlyrate = rate 

con = Contractor('Temu','Epolo','Developer',60,2)
print(con.get_firstname())
print(con.get_lastname())
print(con.get_contractorid())
print(con.get_jobtitle())
print(con.get_hourlyrate())
con.set_hourlyrate(50)
print(con.get_hourlyrate())



#I am now learning modules in python 
#A module is a reusable Python file.
#A package is a folder containing modules.
#The Python Standard Library is a giant collection of packages 
#and modules that come with Python.


# inspect a module (dir())
# understand a module (help())
# import a module (import math)
# import employee
# print(dir(employee))
# help(employee)

import temperature.py 



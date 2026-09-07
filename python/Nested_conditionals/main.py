hungry = input("Are you hungry? Enter y if you are and n if you are not: ")
if hungry == "n":
  print("You are not hungry.")
else:
  healthy = input("Did you want a healthy meal? Enter y if you do and n if you do not: ")
  if healthy == "n":
    print("Getting some junk food.")
  else:
    print("Getting a healthy meal.")
print("All done!")




grade = 85
if grade > 90:
    print("You got an A")
elif grade > 80:
    print("You got a B")
elif grade > 70:
    print("You got a C")
elif grade > 60:
    print("You got a D")
elif grade <= 60:
    print("You got a F")
print("We are done")


#another example but with as reserved keyword 
inp = input('Enter Fahrenheit Temperature:')
try:
  fahr = float(inp)
  cel = (fahr - 32.0) * 5.0 / 9.0
  print(cel)
except ValueError as error:
  print(error)
  print('Oops, you did not enter in a number. Please enter a number next time.')



#another exapmple but with try and except 
inp = input('Enter Fahrenheit Temperature:')
try:
  fahr = float(inp)
  cel = (fahr - 32.0) * 5.0 / 9.0
  print(cel)
except ValueError:
  print('Oops, you did not enter in a number. Please enter a number next time.')
  
  
#another example
inp = input("Enter Fahrenheit Temperature: ")
try: 
    fahr = float(inp)
    cel = (fahr -32.0) * 5.0 / 9.0 
    print(cel)
except: 
    print("Oops, you did not enter in a number. Please enter a number next time.")


#we are learning how to hnadle errors in this example
prompt = "What is the speed of your car: "
speed = int(input(prompt))



hungry = input("Are you hungry? Enter y if you are and n if you are not: ")
healthy = input("Did you want a healthy meal? Enter y if you do and n if you do not: ")
if hungry == "n":
    print("You are not hungry.")
else :
    if healthy == "n":
        print("Getting some junk fod.")
    else:
        print("Gettign healthy food.")
        

        
#there's no point in asking the user if they want a healthy meal if 
#they already decline food.
#lets fix this 
hungry = input("Are you hungry? Enter y if you are and n if you are not: ")
if hungry == "n":
    print("You are not hungry.")
else: 
    healthy = input("Did you wnat to eat something healthy? Enter y for yes and n for no: ")
    if healthy == "n":
        print("Getting me some junk food today.")
    else: 
        print("Getting me a healthy meal today.")
    
#we are creating a drink order prgram where users
#will be first prompted with the choice of water, coffe or tea.
#Based on those selections there are additional prompts that are unique to each.
#As the user enters each options, a string will be built 
#to indicate the entire order to be output at the end. 

#Would you like to order a drink today? y or n 
#Would you like water? if yes offer hot or cold , if cold offer ice or no ice
#if no, offer coffee etc...

# here is the actual program 
drinkDetails=""
drink = input("What type of drink would you like to order today? \nWater\nCoffee\nTea\nEnter your choice: ")
if drink == "Water":
    drinkDetails=drink
    temperature = input("Would you like your water? Hot or Cold:  ")
    if temperature == "Hot":
        drinkDetails += " , " + temperature
    elif temperature == "Cold":
        drinkDetails += " , " + temperature
    else:
        drinkDetails += " , wrong temperature entered" 
    Ice = input("Would you like Ice with your water? Yes or No : ")
    if Ice == "Yes":
        drinkDetails += ", Ice "
    else:
        drinkDetails += " , unknown temperature entered."
elif drink == "Coffee":
    drinkDetails=drink 
    coffeeOptions = input(" How would you like you coffee? Cuban or Colombian : ")
    if coffeeOptions ==" Cuban":
        drinkDetails +=" , " + coffeeOptions
    elif coffeeOptions =="Colombian" :
        drinkDetails += " , " + coffeeOptions 
    else:
        drinkDetails += " , sorry, we dont have your coffee selcetion available, try again"
elif drink =="Tea":
    drinkDetails=drink
    teaOptions = input("How would you like your tea? Green or Black? :  ")
    if teaOptions == "Green":
        drinkDetails +=" , " + teaOptions
    elif teaOptions == "Black": 
        drinkDetails += " , " + teaOptions
    else: 
        drinkDetails += ", sorry, we don't have that tea option available, try again"
else:
    print("Sorry, we did not have that drink available in our menu selection.")
print("Your drink selection: ", drinkDetails)



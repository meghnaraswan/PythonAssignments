#Meghna Raswan
#2337415
#raswan@chapman.edu
#CPSC 230-10 (1515)
#Assignment 2
#total price of an item using if statements

#get puchase price and sales tax rate of item
#convert input to float
purchaseprice = float(input("What is the purchase price of your item? "))
salestaxrate = float(input("What is the sales tax rate? "))

#calculate the total price
total = ((salestaxrate * 0.01) + 1) * purchaseprice

#report the total price to the user if the purchase price and sales tax are greater than or equal to 0
if purchaseprice >= 0 and salestaxrate >= 0:
    print("Your total price is $", total)
else: #inform the user that they need to input positive values
    print("Sorry, I am not able to calculate your total price. "
          "Please make sure that your purchase price and sales tax is positive.")

#Meghna Raswan
#2337415
#raswan@chapman.edu
#CPSC 230-10 (1515)
#Assignment 1
#total price of an item

#get puchase price and sales tax rate of item
PurchasePrice_str = input("What is the purchase price of your item? ")
SalesTaxRate_str = input("What is the sales tax rate? ")

#convert input to float
PurchasePrice_float = float(PurchasePrice_str)
SalesTaxRate_float = float(SalesTaxRate_str)

#calculate the total price
Total = ((SalesTaxRate_float * 0.01) + 1) * PurchasePrice_float

#report the total price to the user
print("Your total price is $", Total)

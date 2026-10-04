# Ravager Snack Bar
import random

pirate_name = input("What's your name, pirate? ")
snack_name = input("What snack do you want? ")

price = random.randint(2, 8)  # random price in credits
quantity = int(input("How many would you like? "))#made it integer for avoiding runtime error 

total = price * quantity

discounted_total = total - (total * 0.10) #switched to total variable name fix

tax_rate = 0.08
total_with_tax = discounted_total + (discounted_total * tax_rate)

print("Hello, " + pirate_name + "! Here's your order summary:")
print("Snack: " + snack_name) #runtime error with  wrong variable thing
print("Price per snack: " + str(price) + " credits")
print("Total before tax: " + str(discounted_total))#switched to discounted_total variable name fix
print("Total with tax: " + str(round(total_with_tax, 2)) + " credits") #clsoing bracket

      
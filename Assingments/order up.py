#order up by SHree 1

#region Code
#region misc work
from datetime import datetime

now = datetime.now()
#endregion

#region special 7 am menu

if now.hour == 7 and now.minute == 00:
  menu = {
    "burger": {
        "Vegi Double":7.00,
        "Fry Potato Patty":7.00,
        "Chef's Special Vegetarian":7.00,
        "bread with cheese":7.00,
    },
    "Drink": {
        "Coke":7.00,
        "Wine": 7.00,
        "Sprite":7.00,
        "'I HATE PEP*I!' poster":7.00,
    },
    "burritoritos": {
        "Veg Burrito":7.00,
        "Gravy Burrito":7.00,
        "Saucy Burrito":7.00,
        "Tortilla with cheese rolled":7.00,
    },
    "sides": {
        "Spicy Fries":7.00,
        "waffle Fries":7.00,
        "Simple Fries":7.00,
        "BIG Fries":7.00,
        "BIG Spicy Fries":7.00,
        "BIG Waffle Fries":7.00,
        "Potato Nuggets":7.00,
        "Apple Slices":7.00,
        "Ranch":7.00,
        "Garlic-Butter Ranch":7.00,
        "Tomato Sauce":7.00,
    },
}
#endregion

#region normal menu
else:
  menu = {
    "burger": {
        "Vegi Double": 6.67,
        "Fry Potato Patty": 5.23,
        "Chef's Special Vegetarian": 8.99,
        "bread with cheese": 2.00,
    },
    "Drink": {
        "Coke": 1.00,
        "Wine": 10.00,
        "Sprite": 1.00,
        "'I HATE PEP*I!' poster": 5.00,
    },
    "burritoritos": {
        "Veg Burrito": 2.99,
        "Gravy Burrito": 2.99,
        "Saucy Burrito": 2.99,
        "Tortilla with cheese rolled": 1.99,
    },
    "sides": {
        "Spicy Fries": 1.99,
        "waffle Fries": 2.50,
        "Simple Fries": 1.99,
        "BIG Fries": 2.99,
        "BIG Spicy Fries": 2.99,
        "BIG Waffle Fries": 2.99,
        "Potato Nuggets": 2.99,
        "Apple Slices": 0.50,
        "Ranch": 0.69,
        "Garlic-Butter Ranch": 0.69,
        "Tomato Sauce": 0.69,
    },
}
#endregion

#region that prints the menu
def display_menu():
  for category, items in menu.items():
    print(f"_-_{category.upper()}_-_")

    for item, price in items.items():
      print(f"  {item}: ${price}")
#endregion

#region for placing order
def get_valid_item(prompt_text, allowed_categories):
  while True:
    choice = input(prompt_text)
    for cat in allowed_categories:
      if choice in menu[cat]:
        return choice
    print("Try again wrong input")

def take_order():
  order = []
  order.append(get_valid_item("\nSelect a Drink: ", ["Drink"]))
  order.append(get_valid_item("\nSelect a Main Course (burger or burritoritos): ", ["burger", "burritoritos"]))
  order.append(get_valid_item("\nSelect your 1st Side Dish: ", ["sides"]))
  order.append(get_valid_item("\nSelect your 2nd Side Dish: ", ["sides"]))

  #placing order
  while True:
    choice = input("\nWhat else do you want? (type 'done' to finish): ")
    if choice.lower() == "done":
      break

    found = False
    for items in menu.values():
      if choice in items:
        found = True

    if found:
      order.append(choice)
    else:
      print("Try again wrong input")
  return order
#endregion

#region for the final order Confirmation and total calculation
def confirm_and_pay(order):
  confirmation = input(f"\nYour order: {order}\n\nWould you like to continue type 1 for yes and 0 for no: ")

  if confirmation == "1":
    total = 0
    for choice in order:
      for items in menu.values():
        if choice in items:
          total += items[choice]

    tax = 4/100 * total

    while True:
      try:
        tip = int(input("How much tip do you want to give!: "))
        break
      except ValueError:
        print("Invalid input! Please enter a whole number for the tip.")
    
    print(f"Tax is {tax}")
    print(f"Tip is {tip}")
    totaltotal = total + tax + tip
    print(f"Total: ${totaltotal}")
  elif confirmation == "0":
    order.clear()
    print("Order canceled. but you didn't have to do this you could have bought please just try again bro come'on you can do this please buy from us thats how we pay our rent")
    return
  else:
    print("Invalid Input order cancelled try again")
    return

  #region payment method options
  payment_method = input("\n Cash or Card: ")

  if payment_method == "Cash":
    cash_machine = total
    money_inserted = total
    if cash_machine == money_inserted:
      print(f"ORDER PLACED!")
    if cash_machine >= total:
      print("Change Dropped!")
      # A function to drop change goes here
    else:
      print("Order failed")
  elif payment_method == "Card":
    print("Tap your card\n")
    #card machine software/function goes here including an if else statement to determine the transaction status
    print("Payment Succesful")
  else:
    print("Invalid input TRY ALL OVER AGAIN!")
  #endregion

display_menu()
customer_order = take_order()
confirm_and_pay(customer_order)
#endregion
#endregion
#^
#| The entire code lol

#very customizable

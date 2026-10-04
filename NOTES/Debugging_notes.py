#Shreenayan mehta Debugging notes

# syntax error


"""print("Hello)
      
#indentation error 
if True:
print("This is true") # <= indentation error 

people = 10
print(poeple)"""

#logic errors 
# read the code again 
apples = 20
people = 3

print(apples // people)

# run time errors 
while True:
    try:
        fav_num = int(input("What is your favorite number"))
    except:
        print("Thats not a number!")
    else:
        break
    
print(4 + fav_num)

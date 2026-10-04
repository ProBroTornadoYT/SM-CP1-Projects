#Unit 1 Final Andrew Petersen
print("Hello User")

#Asking user for name
name = input("What is your name, User? ")
print("Hello", name)

print("")#For a litle white space in the terminal

#Asking user what sport they play
sport = input("What sport do you play? ")
print("Wow!", sport, "is really cool!")

print("")#For a litle white space in the terminal

#Asking user for their record in their sport
record = input("What's your record in it? ")
print("WHAT? Your record is", record+ "!? That's insane!")
print("I wish I could play sports, but I'm just a program, so I can't")

print("")#For a litle white space in the terminal

#Asking user what their hobby is
hobby = input("What is your favorite passtime? ")
print("Huh...", hobby, "sounds interesting.")

print("")#For a litle white space in the terminal

#Asking user their age while making sure that it was an integer
while True:
    try:
        age = int(input("How old are you? (number not typed out pls) "))
    except:
        print("Processing...")
        print("Thats not a number!")
    else:
        print("Processing...")
        break

print("")#For a litle white space in the terminal

#Making comments based on the age
if age > 20:
	print("Did you ride a dinosaur to school??")
elif age < 20:
	print("wazzup yungin")
else:
    print("Bros almost unc")

print("")#For a litle white space in the terminal

#Double checking that everything is correct
print("Ok, so let me get this straight, your name is", name + ", you're", age, "years old, you do", sport + ", your record in", sport, "is", record, "and your hobby is", hobby + ". Is that correct? ")
final_check = input("")

if final_check == "yes" or final_check == "Yes" or final_check == "yep" or final_check == "Yep":
     print("YAY")
     print("I get it wrong waaaay too often")
else:
     print("Dang it!")
     print("Re-run the code to try again.")
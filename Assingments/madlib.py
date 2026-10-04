#Madlip assignment shreenayan mehta

#introduction to the game
print("Welcome to the Mad Lib game Please provide the following words:")

#getting user inputs for the mad lib story
first_name = input("Enter a first name: ")
last_name = input("Enter a last name: ")
noun = input("Enter a noun (a thing): ")
verb = input("Enter a verb (an action): ")
adjective = input("Enter an adjective (a describing word): ")
adverb = input("Enter an adverb (a word that describes a verb): ")
plural_noun = input("Enter a plural noun (more than one thing): ")

#concatenating first name and last name to create a full name for the assisngment 
full_name= first_name + " " + last_name

#story title
print("\nHere is your Mad Lib story:\n")

#story output 

print("Once upon a time, there was a person named "+ full_name +". "+ full_name +" loved to "+verb+" with their "+ adjective + " "+ noun + ". One day, "+ full_name +" decided to "+verb+" "+adverb+" with a group of "+plural_noun+".They had so much fun that they decided to " + verb + " together every day!")
print("The end.")
print("\nThank you for playing the Mad Lib game,  " + full_name + "!")

#the end coding

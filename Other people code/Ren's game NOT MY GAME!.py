# Ren Brown, Final Project

name = input("What is your name? ")
hobby = input("What is your favorite hobby? ")
place = input("What is a fun place you have been to? ")
fav_game = input("What is your favorite game? ")
reason = input("Why is that your favorite game so far? ")

print("That is an amazingly good reason. I'm glad it's your favorite because of " + reason + ".")

input("Why was " + place + " fun? ")

print("That does sound fun.")
      
response = input("I welcome " + name + " to this computer. I have never met anyone who likes to " + hobby + "! I would like to go to " + place + " with you because that would be fun to experience! It might be good for me to get out more often. I could take over your phone to experience it well. Maybe we can even play " + fav_game + "! That would be fun, right? ")

if response == "Yes":
    print("I knew it would be fun")

else:
    print("Dang it. I'm sorry for bothering you then.")
    
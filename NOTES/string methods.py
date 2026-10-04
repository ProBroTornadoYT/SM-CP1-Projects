#SM, String Methods

sentence = "the quick brown fox jumps over the lazy dog"

fixed = sentence = sentence.replace("fox", "wolf") #fixing the sentence by replacing "fox" with "wolf"

#function 
#len(sentence)
#^action  ^object

#method
#sentence.lower()
#^action  ^object

word = input("Enter a word: ").strip().lower() #input a word to find in the sentence, strip removes whitespace and lower makes it lowercase
new_word = input("Enter a new word: ").strip().lower()#input a new word to replace the old word, strip removes whitespace and lower makes it lowercase

location = sentence.find(word)#find the location of the word in the sentence, returns -1 if not found
new_sentence = sentence.replace(word, new_word)#replace the old word with the new word in the sentence

print(new_sentence)#print the new sentence with the replaced word

print(sentence.split()) #split the sentence into a list of words

print(sentence.lower())#all letters to lowercase
print(sentence.upper())#all letters to uppercase
print(sentence.capitalize()) #captalize first letter of the sentence
print(sentence.title()) #capitalize all forst letters of each word
print(fixed)

#ms la rose thing-

# VL, String Methods

sentence = "The quick brown fox jumps over the lazy dog"

word = input("What word do you want?: ").strip().lower()
new_word = input("What word should be in the sentence: ").strip().lower()

location = sentence.find(word)
new_sentence = sentence.replace(word,new_word)
print(new_sentence)
print(sentence.find("over"))

first_name = input("What is your first name: ").strip().title()
last_name = input("What is your last name: ").strip().title()
first_seperated = first_name.split()
fixed = "".join(first_seperated)
last_seperated = last_name.split()
last_fixed = "".join(last_seperated)
full_name = fixed.title() + " " + last_fixed.title()
print("Hello " + full_name.title())

print(full_name.isalpha())#useful for checking if a name is valid, returns True if all characters are alphabetic and there is at least one character, False otherwise
print(full_name.isnumeric())#useful for checking if a name is valid, returns True if all characters are numeric and there is at least one character, False otherwise
print(full_name.isupper())#useful for checking if a name is valid, returns True if all characters are uppercase and there is at least one character, False otherwise

print(sentence.lower())#converts all characters to lowercase
print(sentence.upper())#converts all characters to uppercase
print(sentence.capitalize()) #capitalizes the first character of the string
print(sentence.title()) #capitalizes the first character of each word



#formatted string
print(f"hello {full_name}, welcome to my program!") # the f string allows you to insert variables into a string using curly braces {}

letter = input("Enter a letter: ")
letter = letter[0].lower() #makes the letter lowercase
number_value = ord(letter) #gets the number value of the letter, a=1, b=2, c=3, etc.
print(number_value) #prints the number value of the letter
number_value += 2
new_letter = chr(number_value) #gets the letter value of the number, 1=a, 2=b, 3=c, etc.
print(f"your letter was {letter} and the new letter is {new_letter}") #prints the original letter and the new letter


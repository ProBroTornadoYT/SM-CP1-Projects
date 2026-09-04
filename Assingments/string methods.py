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

SyntaxWarning

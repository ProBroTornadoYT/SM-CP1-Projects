



password = input("Enter Password: ")

strength = 0

chars = list(password)
if any(char.islower() for char in chars):
    strength += 13.4

chars = list(password)
if any(char.upper() for char in chars):
    strength += 13.4

chars = list(password)
if any(char.isdigit() for char in chars):
    strength += 13.4

special_chars = ['!','@','#','$','%','^','&','*','(',')','_','+','-','=','[',']','{','}','|',';',':',',','.','<','>','?']
if any(char in special_chars for char in chars):
    strength += 13.4

if len(password):
    8 <= len(password)
    strength += 13.4

print (int(strength))

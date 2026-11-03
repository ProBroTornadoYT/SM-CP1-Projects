# Caesar Cipher

def caesar_cipher(message, shift_value, mode): #handles everything for the coding of this ciphering
    if mode == 'decode':
        shift_value = -shift_value

    result = []
    
    #math that codes it (googled this)
    for char in message:
        if char.isalpha():
            start = 65 if char.isupper() else 97
            new_char = chr((ord(char) - start + shift_value) % 26 + start)
            result.append(new_char)
        else:
            #this makes it so only like the alphabets are done
            result.append(char)

    return "".join(result)

def main():
    print("_-_*Caesar Cipher Coder*_-_")
    choice = input("Press 1 to encode press 2 to decode: ")
    if choice not in ['1', '2']:
        print("Use either 1 or 2")
        return

    message = input("Enter the code: ")
    
    try:
        user_input = input("By how much do you want to shift: ")
        shift_value = int(user_input)
    except ValueError:
        print(f"Choose a number not this '{user_input}' trash")
        return
    
    if choice == '1':
        encoded = caesar_cipher(message, shift_value, 'encode')
        print(f"Message encoded!: {encoded}")
    else:
        decoded = caesar_cipher(message, shift_value, 'decode')
        print(f"Message decoded: {decoded}")

main()

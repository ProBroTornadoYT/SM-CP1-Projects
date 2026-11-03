#cesar cypher

def caesar_cipher(message, shift_value, mode):
    if mode == 'decode':
        shift_value = -shift_value

    for char in message:
            if char.isalpha():
                start = 65 if char.isupper() else 97
                new_char = chr((ord(char) - start + shift_value) % 26 + start)
                result.append(new_char)
            else:
                # Leave non-alphabetic characters unchanged
                result.append(char)

    return "".join(result)

def main():
    print("_-_*Caesar Cypher Coder*_-_")
    choice = input("Press 1 to encode press 2 to decode: ")
    if choice not in ['1', '2']:
        print("Use either 1 or 2")
        return

    message = input("Enter the code: ")
    
    try:
        shift_value = int(input("By how much do you want to shift: "))
    except ValueError:
        print(f"Choose a number not this '{shift_value}' trash")
        return
    
    if choice == '1':
        encoded = caesar_cipher(message, shift_value, 'encode')
        print(f"Message encoded!: {encoded}")
    else:
        decoded = caesar_cipher(message, shift_value, 'decode')
        print(f"Message decoded: {decoded}")

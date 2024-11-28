def main():
    print("Do you want encod or decod?")
    user_input = input("e/d :" ).lower()
    print()
    if user_input=="e":
       print("your selection is encrept:")
       text = input("Enter the Text: ")
       shift = int(input("Enter the shift value: "))
    
    # Encrypted message
       encrypted_message = caesar_cipher(text, shift)
       print("Encrypted message:", encrypted_message)
    if user_input=="d":
       print("your selection is decoded :")
       text= input("Enter the decoded text: ")
       shift = int(input("enter the key : "))
    # Decrypted message
       decrypted_message = caesar_cipher(text, -shift)
       print("Decrypted message:", decrypted_message)

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            shifted_char = chr((ord(char) - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a'))
            result += shifted_char
        else:
            result += char
    return result
if __name__ == "__main__":
    main()
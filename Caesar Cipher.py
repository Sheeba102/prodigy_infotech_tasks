

#CAESAR CIPHER

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(text, shift):
    result = ""
    for i in text:
        if i in alphabet_list:
            position = alphabet_list.index(i)  # Getting the index of the letter
            new_position = (position + shift) % 26  # Shift the position based on the provided shift value
            result += alphabet_list[new_position]  # Adding the letter to the result string 
        else:
            result += i  # If the character is not in the alphabet list, leave it unchanged
    return result

end = False
while not end:
    a = input("Type 'encrypt' for encryption and 'decrypt' for decryption: ").lower()
    message = input("Type your message: ").lower()
    shift_key = int(input("Enter Shift Key length: "))

    if a == "decrypt":
        shift_key *= -1  # Reverse the shift for decryption

    result = caesar_cipher(text=message, shift=shift_key)
    if a == "encrypt":
        print("The Cipher Text is:", result)
    elif a == "decrypt":
        print("The Plain Text is:", result)
    
    again = input("Type 'YES' to continue or 'NO' to stop: ").lower()
    if again == 'no':
        end = True
        print("THANK YOU !!")









        
         
        




# Define shift value
shift = 8

def encrypt(text):
    # Define empty string for encrypted text
    encrypted_text = ""
    for char in text:
        # Check if character is letter
        if char.isalpha():
            if char.islower():
                # Get encrypted character for lowercase letter
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                # Get encrypted character for uppercase letter
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            # Add encrypted character to encrypted text
            encrypted_text += encrypted_char
        else:
            # If character is not letter, add it to encrypted text
            encrypted_text += char
    return encrypted_text

# Define decrypt function
def decrypt(encrypted_text):
    # Define empty string for decrypted text
    decrypted_text = ""
    for char in encrypted_text:
        # Check if character is letter
        if char.isalpha():
            if char.islower():
                # Get decrypted character for lowercase letter
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else:
                # Get decrypted character for uppercase letter
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            # Add decrypted character to decrypted text
            decrypted_text += decrypted_char
        else:
            # If character is not letter, add it to decrypted text
            decrypted_text += char
    return decrypted_text

def main():
    while True:
        choice = input("Encrypt (e) or Decrypt (d) text? (e/d/exit): ").strip().lower()

        if choice == 'e':
            text = input('Enter text to encrypt: ')
            text_encrypted = encrypt(text)
            print('Encrypted text:', text_encrypted)
        elif choice == 'd':
            text = input('Enter text to decrypt: ')
            text_decrypted = decrypt(text)
            print('Decrypted text:', text_decrypted)
        elif choice == 'exit':
            break
        else:
            print('Invalid choice. Please select a valid option (e/d/exit).')
    
if __name__ == "__main__":
    main()
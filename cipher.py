def encrypt_caesar_cipher(text, shift):
    encrypted_text = []
    for char in text:
        if char.isalpha():
            # Determine the start of the alphabet (either 'A' or 'a')
            start = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around the alphabet if necessary
            new_char = chr(start + (ord(char) - start + shift) % 26)
            encrypted_text.append(new_char)
        else:
            # Non-alphabetic characters remain the same
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def main():
    # Get input from the user
    plain_text = input("Enter the text to be encrypted: ")
    shift = 5  # Caesar cipher shift value
    encrypted_text = encrypt_caesar_cipher(plain_text, shift)
    print(f"Encrypted text: {encrypted_text}")

if __name__ == "__main__":
    main()

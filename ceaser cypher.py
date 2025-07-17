def ceaser_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine the case and base ASCII value
            ascii_base = ord('A') if char.isupper() else ord('a')
            # Apply shift based on mode (encryption or decryption)
            if mode == "encrypt":
                shifted = (ord(char) - ascii_base + shift) % 26 + ascii_base
            else:  # decrypt
                shifted = (ord(char) - ascii_base - shift) % 26 + ascii_base
            result += chr(shifted)
        else:
            # Preserve non-alphabetic characters
            result += char
    return result

# Main program
while True:
    print("\nCaesar Cipher Program")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == '3':
        print("Exiting program...")
        break
    
    if choice in ['1', '2']:
        mode = "encrypt" if choice == '1' else "decrypt"
        message = input("Enter the message: ")
        try:
            shift = int(input("Enter the shift value (1-25): "))
            if 1 <= shift <= 25:
                encrypted_text = ceaser_cipher(message, shift, mode)
                print(f"Result: {encrypted_text}")
            else:
                print("Shift value must be between 1 and 25.")
        except ValueError:
            print("Please enter a valid integer for the shift value.")
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

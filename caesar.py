def caesar_cipher(text, key, mode='encrypt'):
    result = ""
    
    if mode == 'decrypt':
        key = -key

    for c in text:
        result += chr(ord(c) + key)

    return result


plaintext = "ABC"
key = 3

encrypted_text = caesar_cipher(plaintext, key, mode='encrypt')
print("Encrypted Text:", encrypted_text)

decrypted_text = caesar_cipher(encrypted_text, key, mode='decrypt')
print("Decrypted Text:", decrypted_text)

def subcipher(text, key, mode='encrypt'):
    result = ""
    
    if mode == 'decrypt':
        key = [-k for k in key]

    for i in range(len(text)):
        c = text[i]
        shifted_char = chr(ord(c) + key[i])
        result += shifted_char

    return result


plaintext = "ABC"
key = [1, 3, 5]

encrypted_text = subcipher(plaintext, key, mode='encrypt')
print("Encrypted Text:", encrypted_text)

decrypted_text = subcipher(encrypted_text, key, mode='decrypt')
print("Decrypted Text:", decrypted_text)

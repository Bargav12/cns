import string

def vigenere_encrypt(plaintext, key):
    alphabet = string.ascii_uppercase
    # Repeat key to match the length of the plaintext
    key = (key * (len(plaintext) // len(key))) + key[:len(plaintext) % len(key)]
    
    # Encrypt the plaintext
    return ''.join([
        alphabet[(alphabet.index(p) + alphabet.index(k)) % 26] if p in alphabet else p
        for p, k in zip(plaintext.upper(), key)
    ])

def vigenere_decrypt(ciphertext, key):
    alphabet = string.ascii_uppercase
    # Repeat key to match the length of the ciphertext
    key = (key * (len(ciphertext) // len(key))) + key[:len(ciphertext) % len(key)]
    
    # Decrypt the ciphertext
    return ''.join([
        alphabet[(alphabet.index(c) - alphabet.index(k)) % 26] if c in alphabet else c
        for c, k in zip(ciphertext.upper(), key)
    ])

# Example usage
plaintext = "HELLO WORLD"
key = "KEY"
ciphertext = vigenere_encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext}")

decrypted_text = vigenere_decrypt(ciphertext, key)
print(f"Decrypted Text: {decrypted_text}")

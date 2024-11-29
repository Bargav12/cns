def vernam_encrypt_decrypt(text, key):
    """Encrypt or decrypt using Vernam Cipher (same process for both)"""
    if len(text) != len(key):
        raise ValueError("Key and text must be of the same length")
    
    # XOR each character of text with the corresponding character of the key
    return ''.join(chr(ord(t) ^ ord(k)) for t, k in zip(text, key))

# Example usage
plaintext = "HELLO"
key = "XMCKL"  # Key must be the same length as plaintext

# Encrypting the plaintext
ciphertext = vernam_encrypt_decrypt(plaintext, key)
print(f"Ciphertext: {repr(ciphertext)}")  # Use repr to view non-printable characters

# Decrypting is the same as encrypting
decrypted_text = vernam_encrypt_decrypt(ciphertext, key)
print(f"Decrypted Text: {decrypted_text}")

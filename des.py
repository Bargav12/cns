from Crypto.Cipher import DES
from secrets import token_bytes

# Function to pad the text to ensure it's a multiple of 8 bytes
def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

# Function to generate a random 8-byte key for DES
def generate_key():
    return token_bytes(8)

# Function to encrypt a plaintext message using DES
def encrypt(plaintext, key):
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext)
    ciphertext = des.encrypt(padded_text.encode('utf-8'))
    return ciphertext

# Function to decrypt a ciphertext message using DES
def decrypt(ciphertext, key):
    des = DES.new(key, DES.MODE_ECB)
    decrypted_text = des.decrypt(ciphertext).decode('utf-8')
    return decrypted_text.strip()

# Example usage of DES algorithm
if __name__ == '__main__':
    key = generate_key()
    print("Key:", key.hex())

    plaintext = "HELLO DES"
    print("Original text:", plaintext)

    # Encrypt the plaintext
    ciphertext = encrypt(plaintext, key)
    print("Encrypted text:", ciphertext.hex())

    # Decrypt the ciphertext
    decrypted_text = decrypt(ciphertext, key)
    print("Decrypted text:", decrypted_text)

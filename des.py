from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

# Padding function
def pad(text):
    while len(text) % 8 != 0:
        text += ''
    return text

def main():
    message = "This is a confidential message."
    message = pad(message)
    my_message = message.encode('utf-8')

    # Generate a random DES key (8 bytes)
    my_des_key = get_random_bytes(8)

    # Create DES cipher in ECB mode
    my_cipher = DES.new(my_des_key, DES.MODE_ECB)

    # Encrypt the message
    my_encrypted_bytes = my_cipher.encrypt(my_message)

    # Decrypt the message using the same key and cipher mode
    my_cipher = DES.new(my_des_key, DES.MODE_ECB)
    my_decrypted_bytes = my_cipher.decrypt(my_encrypted_bytes)

    encrypted_data = my_encrypted_bytes
    decrypted_data = my_decrypted_bytes.decode('utf-8').strip()

    print("Message: ", message.strip())
    print("Encrypted (in bytes): ", encrypted_data)
    print("Decrypted Message: ", decrypted_data)

if __name__ == "__main__":
    main()





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

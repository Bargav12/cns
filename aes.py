from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def main():
    message = "This is a confidential message"
    secret_key = get_random_bytes(16)  # AES key size of 128 bits (16 bytes)
    cipher = AES.new(secret_key, AES.MODE_ECB)

    while len(message) % 16 != 0:
        message += ' '  # Padding with spaces to make the message length a multiple of 16

    encrypted_message = cipher.encrypt(message.encode('utf-8'))
    encrypted_base64 = base64.b64encode(encrypted_message).decode('utf-8')
    print("Encrypted Message (Base64):", encrypted_base64)

    cipher = AES.new(secret_key, AES.MODE_ECB)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_base64)).decode('utf-8').strip()
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()




from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from secrets import token_bytes

# Function to generate a random key for AES (Rijndael algorithm)
def generate_key(key_size=32):
    return token_bytes(key_size)

# Function to encrypt plaintext using AES
def encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    padded_text = pad(plaintext.encode('utf-8'), AES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return iv + ciphertext

# Function to decrypt ciphertext using AES
def decrypt(ciphertext, key):
    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(actual_ciphertext), AES.block_size)
    return decrypted_text.decode('utf-8')

# Example usage of the Rijndael (AES) algorithm
if __name__ == '__main__':
    key = generate_key(32)
    print("Key:", key.hex())

    plaintext = "HELLO

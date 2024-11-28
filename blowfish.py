from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes
import base64

def main():
    message = "This is a confidential message"
    secret_key = get_random_bytes(16)
    cipher = Blowfish.new(secret_key, Blowfish.MODE_ECB)

    while len(message) % 8 != 0:
        message += ' '

    encrypted_message = cipher.encrypt(message.encode('utf-8'))
    encrypted_base64 = base64.b64encode(encrypted_message).decode('utf-8')
    print("Encrypted Message (Base64):", encrypted_base64)

    cipher = Blowfish.new(secret_key, Blowfish.MODE_ECB)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_base64)).decode('utf-8').strip()
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()




from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
from secrets import token_bytes

def generate_key():
    return token_bytes(16) 

def encrypt(plaintext, key):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB) 
    padded_text = pad(plaintext.encode('utf-8'), Blowfish.block_size) 
    ciphertext = cipher.encrypt(padded_text) 
    return ciphertext

def decrypt(ciphertext, key):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    decrypted_text = unpad(cipher.decrypt(ciphertext), Blowfish.block_size)  
    return decrypted_text.decode('utf-8')

if __name__ == '__main__':
    key = generate_key()
    print("Key:", key.hex())

    plaintext = "HELLO BLOWFISH"
    print("Original text:", plaintext)

    ciphertext = encrypt(plaintext, key)
    print("Encrypted text:", ciphertext.hex())

    decrypted_text = decrypt(ciphertext, key)
    print("Decrypted text:", decrypted_text)

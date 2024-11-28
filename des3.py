from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

key = get_random_bytes(24)
cipher = DES3.new(key, DES3.MODE_ECB)

plaintext = b"This is a secret message."
padded_text = pad(plaintext, DES3.block_size)
ciphertext = cipher.encrypt(padded_text)
print("Encrypted:", ciphertext)

decrypted_padded_text = cipher.decrypt(ciphertext)
decrypted_text = unpad(decrypted_padded_text, DES3.block_size)
print("Decrypted:", decrypted_text.decode('utf-8'))

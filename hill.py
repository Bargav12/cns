import numpy as np

def matrix_mod_inverse(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, modulus)
    minors = np.linalg.inv(matrix).T * det
    cofactors = minors.round().astype(int) % modulus
    adjugate = cofactors.T
    return (det_inv * adjugate) % modulus

def encrypt(plaintext, key_matrix):
    plaintext = plaintext.replace(" ", "").lower()
    n = key_matrix.shape[0]
    while len(plaintext) % n != 0:
        plaintext += 'x'
    plaintext_numbers = [ord(char) - ord('a') for char in plaintext]
    plaintext_matrix = np.array(plaintext_numbers).reshape(-1, n)
    ciphertext_matrix = (plaintext_matrix @ key_matrix) % 26
    ciphertext = ''.join(chr(num + ord('a')) for num in ciphertext_matrix.flatten())
    return ciphertext

def decrypt(ciphertext, key_matrix):
    inverse_key_matrix = matrix_mod_inverse(key_matrix, 26)
    ciphertext_numbers = [ord(char) - ord('a') for char in ciphertext]
    n = key_matrix.shape[0]
    ciphertext_matrix = np.array(ciphertext_numbers).reshape(-1, n)
    plaintext_matrix = (ciphertext_matrix @ inverse_key_matrix) % 26
    plaintext = ''.join(chr(num + ord('a')) for num in plaintext_matrix.flatten())
    return plaintext

# Example usage
if __name__ == "__main__":
    key_matrix = np.array([[6, 24, 1],
                           [13, 16, 10],
                           [20, 17, 15]])
    original_text = "hello world"
    encrypted_text = encrypt(original_text, key_matrix)
    print("Encrypted:", encrypted_text)
    decrypted_text = decrypt(encrypted_text, key_matrix)
    print("Decrypted:", decrypted_text)

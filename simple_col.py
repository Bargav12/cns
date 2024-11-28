# Function to encrypt plaintext using simple columnar transposition cipher
def simple_columnar_transposition_encrypt(plaintext, key):
    n = len(key)  # Number of columns based on the length of the key
    matrix = ['' for _ in range(n)]  # Initialize an empty list for each column
    
    # Fill columns in the matrix in a round-robin manner
    for i in range(len(plaintext)):
        matrix[i % n] += plaintext[i]
    
    # Concatenate columns to form the ciphertext
    ciphertext = ''.join(matrix)
    return ciphertext

# Function to decrypt ciphertext using simple columnar transposition cipher
def simple_columnar_transposition_decrypt(ciphertext, key):
    n = len(key)  # Number of columns based on the length of the key
    rows = len(ciphertext) // n  # Calculate the number of rows required
    
    # Initialize empty strings for each column
    matrix = ['' for _ in range(n)]
    idx = 0  # Index to keep track of characters in ciphertext
    
    # Populate columns in the matrix
    for i in range(n):
        for j in range(rows):
            matrix[i] += ciphertext[idx]
            idx += 1
    
    # Concatenate characters in each row to reconstruct plaintext
    plaintext = ''.join(matrix)
    return plaintext

if __name__ == "__main__":
    plaintext = "HELLOTHISISANEXAMPLE"
    key = "43125"
    
    # Encrypt the plaintext
    print(f"Plaintext: {plaintext}")
    simple_ciphertext = simple_columnar_transposition_encrypt(plaintext, key)
    print(f"Simple Columnar Transposition Ciphertext: {simple_ciphertext}")
    
    # Decrypt the ciphertext
    simple_decrypted = simple_columnar_transposition_decrypt(simple_ciphertext, key)
    print(f"Simple Columnar Transposition Decrypted: {simple_decrypted}")

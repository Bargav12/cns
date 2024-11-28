# Function to encrypt plaintext using advanced columnar transposition cipher
def advanced_columnar_transposition_encrypt(plaintext, key):
    n = len(key)  # Number of columns based on the length of the key
    sorted_key_indices = sorted(range(n), key=lambda x: key[x])  # Sort indices based on key order
    rows = (len(plaintext) + n - 1) // n  # Number of rows needed, rounding up
    matrix = ['' for _ in range(n)]  # Initialize columns

    # Fill columns in the matrix in a round-robin manner
    for i in range(len(plaintext)):
        col = i % n
        matrix[col] += plaintext[i]

    # Concatenate columns in sorted order of the key to form the ciphertext
    ciphertext = ''.join(matrix[i] for i in sorted_key_indices)
    return ciphertext

# Function to decrypt ciphertext using advanced columnar transposition cipher
def advanced_columnar_transposition_decrypt(ciphertext, key):
    n = len(key)  # Number of columns based on the length of the key
    sorted_key_indices = sorted(range(n), key=lambda x: key[x])  # Sort indices based on key order
    rows = (len(ciphertext) + n - 1) // n  # Calculate the number of rows needed
    column_lengths = [rows + 1 if i < len(ciphertext) % n else rows for i in range(n)]  # Column lengths based on ciphertext

    # Initialize empty strings for each column
    matrix = ['' for _ in range(n)]
    idx = 0  # Start index for filling columns

    # Populate each column in the matrix according to sorted key order
    for i in sorted_key_indices:
        matrix[i] = ciphertext[idx:idx + column_lengths[i]]
        idx += column_lengths[i]

    # Reconstruct plaintext row by row
    plaintext = ''
    for i in range(rows):
        for j in range(n):
            if i < len(matrix[j]):
                plaintext += matrix[j][i]
    
    return plaintext

if __name__ == "__main__":
    plaintext = "HELLOTHISISANEXAMPLE"
    key = "43125"
    
    # Encrypt the plaintext
    print(f"Plaintext: {plaintext}")
    advanced_ciphertext = advanced_columnar_transposition_encrypt(plaintext, key)
    print(f"Advanced Columnar Transposition Ciphertext: {advanced_ciphertext}")
    
    # Decrypt the ciphertext
    advanced_decrypted = advanced_columnar_transposition_decrypt(advanced_ciphertext, key)
    print(f"Advanced Columnar Transposition Decrypted: {advanced_decrypted}")

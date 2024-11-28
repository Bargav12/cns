def simple_columnar_transposition(message, key):
    message = message.replace(" ", "").upper()
    key = key.upper()
    
    num_columns = len(key)
    num_rows = (len(message) + num_columns - 1) // num_columns  # Equivalent to ceil(len(message) / num_columns)
    
    # Create a grid and fill it with the message, padding with 'X' if necessary
    grid = [['X' for _ in range(num_columns)] for _ in range(num_rows)]
    index = 0
    for r in range(num_rows):
        for c in range(num_columns):
            if index < len(message):
                grid[r][c] = message[index]
                index += 1
    
    # Read columns based on the grid
    cipher_text = ''.join(''.join(grid[r][c] for r in range(num_rows)) for c in range(num_columns))
    
    return cipher_text


# Driver Code
if __name__ == "__main__":
    message = input("Enter the message: ")
    key = input("Enter the key: ")
    
    cipher_text = simple_columnar_transposition(message, key)
    print("Simple Columnar Transposition Cipher Text:", cipher_text)






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

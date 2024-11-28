def create_playfair_matrix(key):
    key = key.replace("j", "i").lower()
    key = ''.join(sorted(set(key), key=key.index))
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    matrix = key + ''.join(c for c in alphabet if c not in key)
    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def find_position(char, matrix):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def prepare_text(text):
    text = text.replace(" ", "").replace("j", "i").lower()
    prepared = []
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            prepared.append(text[i] + 'x')
            i += 1
        else:
            prepared.append(text[i:i + 2])
            i += 2
    return prepared

def encrypt(plaintext, key):
    matrix = create_playfair_matrix(key)
    digraphs = prepare_text(plaintext)
    ciphertext = ""
    for digraph in digraphs:
        row1, col1 = find_position(digraph[0], matrix)
        row2, col2 = find_position(digraph[1], matrix)
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
    return ciphertext

def decrypt(ciphertext, key):
    matrix = create_playfair_matrix(key)
    digraphs = prepare_text(ciphertext)
    plaintext = ""
    for digraph in digraphs:
        row1, col1 = find_position(digraph[0], matrix)
        row2, col2 = find_position(digraph[1], matrix)
        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2] + matrix[row2][col1]
    return plaintext.replace("x", "")

# Example usage
if __name__ == "__main__":
    key = "playfair example"
    original_text = "hide the gold in the tree stump"
    encrypted_text = encrypt(original_text, key)
    print("Encrypted:", encrypted_text)
    decrypted_text = decrypt(encrypted_text, key)
    print("Decrypted:", decrypted_text)

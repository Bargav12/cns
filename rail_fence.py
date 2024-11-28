# Rail Fence Cipher Encryption
def rail_fence_encrypt(text, num_rails):
    if num_rails == 1:
        return text
    fence = ['' for _ in range(num_rails)]
    row, step = 0, 1

    # Build the rail fence by zig-zagging the characters across the rails
    for char in text:
        fence[row] += char
        if row == 0:
            step = 1
        elif row == num_rails - 1:
            step = -1
        row += step

    # Concatenate all rows to get the ciphertext
    return ''.join(fence)

# Rail Fence Cipher Decryption
def rail_fence_decrypt(cipher_text, num_rails):
    if num_rails == 1:
        return cipher_text
    fence = ['' for _ in range(num_rails)]
    row, step = 0, 1
    cipher_len = len(cipher_text)
    char_pos = [0] * num_rails

    # Mark the zig-zag pattern with '*'
    for i in range(cipher_len):
        fence[row] += '*'
        if row == 0:
            step = 1
        elif row == num_rails - 1:
            step = -1
        row += step

    # Fill the marked positions with the characters from the ciphertext
    idx = 0
    for i in range(num_rails):
        for j in range(len(fence[i])):
            if fence[i][j] == '*':
                fence[i] = fence[i][:j] + cipher_text[idx] + fence[i][j+1:]
                idx += 1

    # Read the characters in a zig-zag pattern to reconstruct the plaintext
    result, row, step = '', 0, 1
    for i in range(cipher_len):
        result += fence[row][char_pos[row]]
        char_pos[row] += 1
        if row == 0:
            step = 1
        elif row == num_rails - 1:
            step = -1
        row += step

    return result

# Example usage
text = "WEAREDISCOVEREDFLEEATONCE"
num_rails = 3
cipher_text = rail_fence_encrypt(text, num_rails)
print(f"Cipher Text: {cipher_text}")
decrypted_text = rail_fence_decrypt(cipher_text, num_rails)
print(f"Decrypted Text: {decrypted_text}")

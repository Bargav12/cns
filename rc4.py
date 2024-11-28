class RC4:
    def __init__(self, key):
        self.key = [ord(c) for c in key]
        self.S = list(range(256))
        self.init_permutation()

    def init_permutation(self):
        j = 0
        for i in range(256):
            j = (j + self.S[i] + self.key[i % len(self.key)]) % 256
            self.S[i], self.S[j] = self.S[j], self.S[i]

    def crypt(self, data):
        i = j = 0
        result = []
        for char in data:
            i = (i + 1) % 256
            j = (j + self.S[i]) % 256
            self.S[i], self.S[j] = self.S[j], self.S[i]
            K = self.S[(self.S[i] + self.S[j]) % 256]
            result.append(chr(ord(char) ^ K))
        return ''.join(result)

# Example usage
if __name__ == "__main__":
    key = "secret"
    plaintext = "Hello RC4"

    rc4 = RC4(key)
    ciphertext = rc4.crypt(plaintext)
    print("Encrypted:", ciphertext)

    rc4 = RC4(key)
    decrypted = rc4.crypt(ciphertext)
    print("Decrypted:", decrypted)

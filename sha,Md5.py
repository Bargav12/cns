import hashlib

def encrypt_this_string(input_string):
    sha1 = hashlib.sha1()
    sha1.update(input_string.encode('utf-8'))
    hashtext = sha1.hexdigest()
    return hashtext

def verify_hash(input_string, original_hash):
    return encrypt_this_string(input_string) == original_hash

# Driver code
if __name__ == "__main__":
    text = "GeeksForGeeks"
    hash_value = encrypt_this_string(text)
    print(hash_value)
    print("Match" if verify_hash(text, hash_value) else "No Match")



import hashlib

def encrypt_this_string(input_string):
    md5 = hashlib.md5()
    md5.update(input_string.encode('utf-8'))
    hashtext = md5.hexdigest()
    return hashtext

def verify_hash(input_string, original_hash):
    return encrypt_this_string(input_string) == original_hash

# Driver code
if __name__ == "__main__":
    text = "GeeksForGeeks"
    hash_value = encrypt_this_string(text)
    print(hash_value)
    print("Match" if verify_hash(text, hash_value) else "No Match")

import cv2
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256  # Import the SHA256 module

def create_signature(image_path, private_key):
    # Load the image and generate its hash
    image = cv2.imread(image_path)
    image_data = image.tobytes()

    # Create the SHA-256 hash object
    hash_object = SHA256.new(image_data)  # Use SHA256.new() to create the hash object

    # Create the signature
    signature = pkcs1_15.new(private_key).sign(hash_object)  # Use the hash object directly

    return signature

def load_private_key(key_path):
    with open(key_path, 'rb') as key_file:
        private_key = RSA.import_key(key_file.read())
    return private_key

# Example usage
private_key = load_private_key('private_key.pem')
signature = create_signature('tree.jpg', private_key)
print(f'Signature: {signature.hex()}')


# image encryption

import cv2
from Crypto.Cipher import AES
import os
import numpy as np

def pad(data):
    while len(data) % 16 != 0:
        data += b'\x00'
    return data

def encrypt_image(image_path, key):
    image = cv2.imread(image_path)
    image_data = image.tobytes()
    padded_data = pad(image_data)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(padded_data)

    return ciphertext, cipher.nonce

key = os.urandom(16)  # Generate a random key
encrypted_data, nonce = encrypt_image('tree.jpg', key)
print('Encrypted Data:', encrypted_data)
print('Nonce:', nonce)


# watermarking

import cv2
import os
import matplotlib.pyplot as plt
from google.colab import files

# Step 1: Upload an image
uploaded = files.upload()

# Step 2: Define the watermarking function
def add_watermark(image_path, watermark_text):
    image = cv2.imread(image_path)
    font = cv2.FONT_HERSHEY_SIMPLEX
    position = (10, 30)  # Top-left corner
    font_scale = 1
    color = (255, 255, 255)  # White color
    thickness = 2

    # Add the watermark
    cv2.putText(image, watermark_text, position, font, font_scale, color, thickness)

    return image

# Step 3: Use the uploaded image name
image_filename = list(uploaded.keys())[0]  # Get the uploaded image name
watermarked_image = add_watermark(image_filename, 'Sample Watermark')

# Step 4: Convert BGR to RGB for displaying
watermarked_image_rgb = cv2.cvtColor(watermarked_image, cv2.COLOR_BGR2RGB)

# Step 5: Display the watermarked image
plt.imshow(watermarked_image_rgb)
plt.axis('off')  # Hide the axes
plt.show()


# image hashing

import cv2
import hashlib

def hash_image(image_path):
    # Load the image and convert to bytes
    image = cv2.imread(image_path)
    image_data = image.tobytes()

    # Generate SHA-256 hash
    hash_object = hashlib.sha256(image_data)
    hash_hex = hash_object.hexdigest()

    return hash_hex

# Example usage
hash_value = hash_image('tree.jpg')
print(f'Hash of the image: {hash_value}')

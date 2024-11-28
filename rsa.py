import math
from sympy import mod_inverse

def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)

def main():
    p = 3
    q = 11
    n = p * q
    z = (p - 1) * (q - 1)
    print("The value of z =", z)
    
    # Finding e (public key exponent)
    for e in range(2, z):
        if gcd(e, z) == 1:
            break
    print("The value of e =", e)
    
    # Finding d (private key exponent)
    for i in range(1, 10):
        x = 1 + (i * z)
        if x % e == 0:
            d = x // e
            break
    print("The value of d =", d)
    
    msg = 12
    print("Original message:", msg)
    
    # Encryption
    c = pow(msg, e, n)
    print("Encrypted message is:", c)
    
    # Decryption
    msg_back = pow(c, d, n)
    print("Decrypted message is:", msg_back)

if __name__ == "__main__":
    main()

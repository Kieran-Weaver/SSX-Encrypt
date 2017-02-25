import random
def apply_cipher(plaintext,key):
    print("I don't feel like doing this today")
    random.seed(a=key)
    s2 = "".join([chr(random.randrange(255)) for i in range(len(plaintext))])
    print(''.join(chr(ord(a) ^ ord(b)) for a,b in zip(plaintext,s2)))
    print([ord(a) ^ ord(b) for a,b in zip(plaintext,s2)])
apply_cipher("doge",21)

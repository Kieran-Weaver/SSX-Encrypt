import random
ciphertextlist = []
i=0
def apply_cipher(plaintext,key):
    print("I don't feel like doing this today")
    random.seed(a=key)
    s2 = "".join([chr(random.randrange(255)) for i in range(len(plaintext))])
    print(''.join(chr(ord(a) ^ ord(b)) for a,b in zip(plaintext,s2)))
    print([dafunction(ord(a),ord(b)) for a,b in zip(plaintext,s2)])


def dafunction(plaintext1,key1):
    global i
    ciphertextlist.append(0)
    for j in range(random.randrange(250,255)):
        ciphertextlist[i] = ciphertextlist[i] ^ plaintext1 ^ key1
    i = i + 1
    return ciphertextlist[i-1]
print("".join([chr(x) for x in range(0,255)]))
apply_cipher("doge",21)

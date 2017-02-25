import random
import math
ciphertextlist = []
i=0
ind = 1
def stream_cipher(plaintext,key,length):
    random.seed(a=key)
    o = "".join(format(ord(x), 'b') for x in plaintext)
    p = "0b" + o
    b = sponge(int(o,2),length,1600)
    return " ".join([str(x) for x in b])

def pad(a,r):
    if a.bit_length() % r == 0:
        return a
    else:
        a = (((a * 2) + 1)*(2**(a.bit_length()))) + 1
        return a

def to_bits(a):
    b=[]
    while a > 0:
        if a % 2 ==0:
            b.append(0)
        else:
            b.append(1)
        a = a // 2
    b.reverse()
    return b

def from_bits(a):
    b = 0
    for i in range(len(a)):
        b = b + a[i]*(2**i)
    return b
def f(s):
    s = s * random.randrange(2342)
    s = s % 2342
    return s
def sponge(m,l,g):
    s = []
    r = 128
    s = to_bits(pad(random.randrange(234),256))
    p = to_bits(pad(m,r))
    for i in range(len(p)//r - 1):
        s = to_bits(from_bits(s) ^ from_bits(p[i*r:i*(r+1)]))
        s = to_bits(f(from_bits(s)))
        s.reverse()
    Z = s[0:len(s)-(len(s)%r)]
    while len(Z) < l:
        s = to_bits(f(from_bits(s)))
        Z.extend(s[0:r])
    return Z[0:l]
print(stream_cipher("Thisisthemostannoyingthingihavedonealldaybecausethisistheonlythingihavedonealld","Potato",16000))
    #Cardinality of set S = |S|
    #log(1+e) ~ e if e << 1
    #Length of a bitstring M = |M|
    #Number of blocks of M = |M|_l (length of l)
    #Truncation of a bitstring M to first l bits = |_ M_| l
    #n 0s = 0^n
    #Concatenation of M and N = M||N
    #Multi rate padding pad10*1 appends 1, many 0s, 1, until block size is satisfied
    #Simple padding pad10* appends 1, many 0s, until block size is satisfied
#r < b
#Z = sponge(M,l)
#P = concat(M,pad[r](|M|)) (Padding M into a sequence of r-bit blocks)
#s = 0^b (b zeroes)
#for i in range(|P|r - 1) (iterate through all blocks of P)
#   s = s xor (ith block of P)||(b-r zeroes)
#   s = f(s)
#Absorbing done
#
#Squeezing Start
#Z = |_ s _\ r (Truncate s so that s is of length r)
#while len(Z) < l
#   s = f(s)
#   Z = Z|| (|_ s _| r)
#
#return |_ Z _| l
#
#
#

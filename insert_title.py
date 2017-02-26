from decimal import *
import random
import math
with localcontext() as ctx:
    ctx.prec = 32  # desired precision
    ciphertextlist = []
    i=0
    ind = 1
    def stream_cipher(iv,plaintext,key,length):
        random.seed(a=key)
        o = "".join(format(int(pad(ord(x)*2,8)), 'b') for x in iv)
        p = "0b" + o
        s = "".join(format(int(pad(ord(x)*2,8)), 'b') for x in plaintext)
        k = pad(int(s,2),length)
        b = sponge(int(s,2),len(to_bits(k)),len(to_bits(k)))
        l=[]
        d=[]
        for i in range((len(to_bits(k))//length)+1):
            j =from_bits(to_bits(k)[i*length:(i+1)*length])
            d.append(from_bits(b[i*length:(i+1)*length]))
            l.append(int(j)^int(d[i]))
        return "\n".join([str(x) for x in l])

    def pad(a,r):
        if ((a.bit_length()+1) % r ==0) or (a.bit_length() % r == 0):
            a = (((a * 2) + 1)*(2**(r+r-1-(a.bit_length()%r)))) + 1
            return a
        else:
            a = (((a * 2) + 1)*(2**(r-1-(a.bit_length()%r)))) + 1
            return a
    def unpad(a):
        a = a-1
        while (a % 2 == 0):
            a = a//2
        a = (a-1)/2
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
        s = to_bits(pad(random.randrange(234),128))
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
    yy = stream_cipher("deadbeef",stream_cipher("deadbeef","ngthingihavedonealldaybecausethisistheonlythingihavedoneallday","Potato",128),"Potato",128)
    print(yy)
    print(pad(126,8))
    for i in range(256):
        print(unpad(pad(i,8)))

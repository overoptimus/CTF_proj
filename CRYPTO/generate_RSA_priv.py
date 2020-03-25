
# coding=utf-8
import math
import sys
from Crypto import PublicKey
arsa = PublicKey.RSA.generate(1024)
arsa.p = 275127860351348928173285174381581152299
arsa.q = 319576316814478949870590164193048041239
arsa.e = 65537
arsa.n = arsa.p * arsa.q
Fn = long((arsa.p - 1) * (arsa.q - 1))
i = 1
while(True):
    x = (Fn * i) + 1
    if(x % arsa.e == 0):
        arsa.d = x / arsa.e
        break
    i = i + 1

with open('private.pem', 'w') as private:
    private.write(arsa.exportKey())

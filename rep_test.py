from Crypto.PublicKey import RSA
from Crypto.Util import  number
import random
import sys



p = number.getPrime(int(sys.argv[1]))
q = number.getPrime(int(sys.argv[1]))

n = p*q
f = (p-1)*(q-1)

e = random.randint(1,f)
while number.GCD(e, f) != 1:
    e = random.randint(1, f)

d = number.inverse(e,f)

print("Running RSA with p = {}, q = {}, n = {}, e = {}, d = {}".format(str(p),str(q),str(n),str(e),str(d)))

p = random.randint(1,n)

print("Plain text : {0}".format(p))

def enc(p,e,n):
    return (p**e)%n

ci = enc(p,e,n)
print("Encrypted text : {}".format(str(ci)))
c = enc(ci,e,n)
while (c != ci):
    cp = c
    c = enc(c,e,n)
    print(c)

print("I have found it p = {0}".format(cp))




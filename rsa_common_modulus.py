from Crypto.Util import number

e1 = 17
e2 = 13

c1 = 75
c2 = 38

n = 77

print(number.GCD(e1,e2))

w = number.inverse(e1,e2)
v = number.inverse(e2,e1)
print w,v

# v = v - e2

# print w,v
# print("Checking : w*e1+v*e2 = {}".format(w*e2+v*e3))

# p1 = pow(c2,w,n)
# p2 = pow(number.inverse(c3,n),-v,n)

# res = (p1*p2)%n
# print(res)

# print("Checking c1 = : {}".format(pow(res,e3,n)))



w = w - e2

print w,v
print("Checking : w*e1+v*e2 = {}".format(w*e1+v*e2))

#p1 = pow(c2,w,n)
p1 = pow(number.inverse(c1,n),-w,n)
p2 = pow(c2,v,n)

res = (p1*p2)%n
print(res)

print("Checking c1 = : {}".format(pow(res,e1,n)))

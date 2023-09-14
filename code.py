
import random as ra

print("welcome to Password Generator!")
num = list(range(0,10))
alp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S',
       'T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l',
       'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
splc = ['~','`','!','@','#','$','%','^','&','*','(',')','-','+']

pasw = []

s = int(input("How many number you like in your password?:"))
for i in range(s):
    c = ra.choice(num)
    pasw.append(c)
d = int(input("How many characters you like in your password?:"))
for i in range(0,d):
    f = ra.choice(alp)
    pasw.append(f)
j = int(input("How many spl_char you like in your password?:"))
for i in range(0,j):
    g = ra.choice(splc)
    pasw.append(g)

ra.shuffle(pasw)

st = ''
for i in pasw:
    st+=str(i)

print("your Password is:",st)

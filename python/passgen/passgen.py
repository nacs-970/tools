import random
from sys import argv

upper = "ABCDEFGHIJKLMNOPQRSTUVVWXYZ"
lower = upper.lower()
digits = "0123456789"
punc = "~`!@#$%^&*()_+-=[]{}\\|;:,.<>?""'' "

u,l,d,p = True, True, True, True

var = ""

if u:
    var += upper
if l:
    var += lower
if d:
    var += digits
if p:
    var += punc

if len(argv) >= 2:
    password = "".join(random.sample(var,int(argv[1])))
    print(password)

else:
    length = int(input("Enter Length : "))
    amount = int(input("Enter Amount : "))
    for x in range(amount):
        password = "".join(random.sample(var,length))
        print(password)


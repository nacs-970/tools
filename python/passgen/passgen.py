import random

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

length = int(input("Enter Length : "))
amount = int(input("Enter Amount : "))

for x in range(amount):
    password = "".join(random.sample(var,length))
    print(password)


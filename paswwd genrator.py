import random
s = "tusharchavan143"
passwdlen = int(input("enter the length of password to genrate:-"))


n = int(input("number of passwds to be genrated:-"))
for i in range(n):
    passwd = "".join(random.sample(s,passwdlen))
    print(passwd)

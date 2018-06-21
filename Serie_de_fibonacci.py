b=2
c=0
a=1
while b<=4000000:
    if b%2==0:
        c+=b
    d=b
    b=b+a
    a=d
print(c)
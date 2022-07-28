n=int(input())
arr=[1,5,10,20,100]
c=0
while n>0:
    if n>=100:
        c=c+1
        n=n-100
        continue
    elif n>=20:
        c=c+1
        n=n-20
        continue
    elif n>=10:
        c=c+1
        n=n-10
        continue
    elif n>=5:
        c=c+1
        n=n-5
        continue
    else:
        c=c+1
        n=n-1

print(c)


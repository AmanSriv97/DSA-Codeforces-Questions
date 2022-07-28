n= int(input())
for i in range(n+1,n+1000):
    a=str(i)
    b=set(a)
    if len(b)==4:
        print(i)
        break
    else:
        continue
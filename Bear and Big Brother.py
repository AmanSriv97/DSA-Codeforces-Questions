l,b= map(int,input().split())
c=0
for i in range(1000):
    l=l*3
    b=b*2
    c=c+1

    if l>b:
        break

print(c)
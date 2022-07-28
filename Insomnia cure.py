k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())
c=0
if k>d or l>d or m>d or n>d:
    print(0)
else:
    for i in range(1,d+1):
        if i%k==0:
            c=c+1
            continue
        if i%l==0:
            c=c+1
            continue
        if i%m==0:
            c=c+1
            continue
        if i%n==0:
            c=c+1
            continue
    print(c)

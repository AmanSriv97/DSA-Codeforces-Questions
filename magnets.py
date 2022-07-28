n= int(input())
n1=int(input())
c=0
for i in range(1,n):
    n2=int(input())
    if n1!=n2:
        c=c+1
    n1=n2
print(c+1)
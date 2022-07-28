n=int(input())
s=len(str(n))

c=0
for i in range(s):
    a=n%10
    n=n//10
    if a==4 or a==7:
        c=c+1

if c==4 or c==7:
    print("YES")
else:
    print("NO")

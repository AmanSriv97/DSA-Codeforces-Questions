n,k,w= map(int,input().split())
a=0
for i in range(w):
    a=a+((i+1)*n)

if a>k:
    print(a-k)
else:
    print(0)
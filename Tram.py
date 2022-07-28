n=int(input())
s=0
a=0
for i in range(n):
    m,k= map(int,input().split())
    if i ==0:
        s=k
        if s>a:
            a=s  
    elif i==(n-1):
        s=s-(k+m)
        
    else:
        s=s+(k-m)
     
        if s>a:
            a=s
print(a)
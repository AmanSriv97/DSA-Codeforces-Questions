n,t= map(int,input().split())
s1= input()
s=list(s1)
s2=""
for i in range(t):
    m=1
    while m<n:
        if s[m-1]=="B" and s[m]=="G":
            a=s[m]
            s[m]=s[m-1]
            s[m-1]=a
            m=m+1
        m=m+1

print(s2.join(s))



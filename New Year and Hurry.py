n, k = map(int, input().split())
timeleft= 240-k
s=0
c=0
for i in range(1,n+1):
    
    s=s+(5*i)
    if s<=timeleft:
        c=c+1

print(c)
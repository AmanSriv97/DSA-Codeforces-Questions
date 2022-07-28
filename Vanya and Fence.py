n,h = map(int,input().split())
arr=[int(item) for item in input().split()]
c=0

for i in range(n):
    if arr[i]//h==0 or arr[i]==h:
        c=c+1
    else:
        c=c+2

print(c)

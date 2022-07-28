n= int(input())
c=0
for i in range (n):
    arr=[int(item) for item in input().split()]
    if arr[1]-arr[0]>=2:
        c=c+1

print(c)
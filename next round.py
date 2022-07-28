n,k = map(int, input().split())

arr=[int(item) for item in input().split()]
m=arr[k-1]
c=0
for i in range(n):
    if arr[i]==0:
        continue
    if arr[i]>=m:
        c+=1
    
print(c)
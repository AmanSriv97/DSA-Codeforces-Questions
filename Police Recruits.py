n= int(input())

arr=[int(item) for item in input().split()]
s=0
c=0
for i in range(len(arr)):
    s=s+arr[i]

    if arr[i]>0:
        c=c-arr[i]

    if s<0:
        c=c+1


print(c)
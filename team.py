a= int(input())
d=0
for i in range(a):
    arr= [int(item) for item in input().split()]
    c=0
    for j in range(len(arr)):
        if arr[j]==1:
            c+=1

    if c>1:
        d=d+1

print(d)    



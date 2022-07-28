arr=input().split("+")
arr.sort()
s=""
for i in range(len(arr)):
    s=s+arr[i]+"+"

print(s[:-1])
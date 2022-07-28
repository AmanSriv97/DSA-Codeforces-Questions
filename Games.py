n= int(input())
arr1=[]
arr2=[]
for i in range(n):
    h, k = map(int, input().split())
    arr1.append(h)
    arr2.append(k)
c=0
for j in range(n):
    c=c+arr1.count(arr2[j])

print(c)
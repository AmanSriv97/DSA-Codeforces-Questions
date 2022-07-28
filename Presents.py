n= int(input())
arr= [int(item) for item in input().split()]
#arr1=[]
s=""
for i in range(n):
    s=s+str((arr.index(i+1))+1)+ " "

print(s)
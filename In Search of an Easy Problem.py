n=int(input())
arr= [int(item) for item in input().split()]
a=set(arr)

if a =={0,1} or a=={1,0} or a=={1}:
    print("Hard")
else:
    print("Easy")


n= int(input())
arr=[int(item) for item in input().split()]
arr1=[int(item) for item in input().split()]
if arr==[0]:
    b=arr1[1:]
elif arr1==[0]:
    b=arr[1:]
else:
    b=arr[1:]+arr1[1:]

a=set(b)

if len(a)==n:
    print("I become the guy.")

else:
    print("Oh, my keyboard!")
n=int(input())
if n<=5:
    print(1)
else:
    if n%5==0:
        a=n//5
        print(a)
    else:
        a=(n//5)+1
        print(a)
n= int(input())

for i in range(n):
    n=int(input())

    a=n//2

    if n<=2:
        print(0)

    else:
        if n%2==1:
            print(a)

        else:
            print(a-1)
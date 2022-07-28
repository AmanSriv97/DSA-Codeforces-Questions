n,m = map(int, input().split())
a=1
b=3
for i in range(n):
    
    if i%2==0:
       print("#" * m)

    else:
        if i==a:
            print ("." *(m-1)+ "#")
            a=a+4
        if i==b:
            print ( "#" +"." *(m-1))
            b=b+4

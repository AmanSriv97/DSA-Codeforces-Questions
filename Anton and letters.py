s=input()

if len(s)==2:
    print(0)

else:
    a=s[1:len(s)-1]

    b=a.split(', ')

    x=len(set(b))

    print(x)


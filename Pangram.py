n= int(input())
s=input().lower()
if n<26:
    print("NO")
else:
    s1=list(s)
    se=set(s1)

    if len(se)==26:
        print("YES")
    else:
        print("NO") 
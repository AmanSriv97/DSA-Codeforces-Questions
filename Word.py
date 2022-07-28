s= input()
c=0
d=0
for i in range(len(s)):
    if s[i].isupper()== True:
        c=c+1
    if s[i].islower()==True:
        d=d+1

if c>d:
    print(s.upper())
elif c<=d:
    print(s.lower())


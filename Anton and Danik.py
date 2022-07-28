n= int(input())
s=input()
c=0
d=0
for i in range(n):
    if s[i]=="A":
        c=c+1
    else:
        d+=1

if c==d:
    print("Friendship")
elif c>d:
    print("Anton")
else:
    print("Danik")
s=input()
s1= input()
s2=""
for i in range(len(s)):
    if (s[i]=="1" and s1[i]=="0") or (s[i]=="0" and s1[i]=="1") :
        s2=s2+str(1)
    else:
        s2=s2+str(0)

print(s2)
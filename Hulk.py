n= int(input())
s1="I hate"
s2="I love"
s=""
if n==1:
    s=s1+" " +'it'
    print(s)

else:
    
    for i in range(1,n+1):
        if i<n:
            if i%2==0:
                s=s+s2 + " " + 'that'+ " "
            else:
                s=s+s1 + " " + 'that'+ " "
        else:
            if i%2==0:
                s=s+s2 +" "
            else:
                s=s+s1 +" "

    print(s+"it")

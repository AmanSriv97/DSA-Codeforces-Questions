number= int(input())

scores=[int(item) for item in input().split()]
max= scores[0]
min=scores[0]
c=0
for i in range(1,number):
    if scores[i]>max:
        c=c+1
        max=scores[i]
    elif scores[i]<min:
        c=c+1
        min=scores[i]

print(c)
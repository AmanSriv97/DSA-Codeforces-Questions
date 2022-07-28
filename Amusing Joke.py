name=input()
host=input()
shuffled=input()

final= name+host

if len(final)!= len(shuffled):
    print("NO")

else:

    sortedfinal=list(final)
    sortedshuffled= list(shuffled)

    sortedfinal.sort()
    sortedshuffled.sort()

    c=0

    for i in range(len(shuffled)):
        if sortedfinal[i]==sortedshuffled[i]:
            c=c+1
            continue
        else:
            break

    if c==len(shuffled):
        print("YES")

    else:
        print("NO")







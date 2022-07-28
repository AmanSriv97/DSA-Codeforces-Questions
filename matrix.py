for i in range(5):
    arr=[int(item) for item in input().split()]
    for j in range(5):
        if arr[j]==1:
            index=j+1
            row=i+1
print((abs(index-3))+(abs(row-3)))
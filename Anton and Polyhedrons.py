number=int(input())

dic={'Icosahedron':20,"Tetrahedron": 4 , "Cube": 6, "Dodecahedron":12, "Octahedron":8}
sum=0
for i in range(number):
    s= input()
    sum= sum+ dic[s]

print(sum)
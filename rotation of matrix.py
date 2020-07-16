num=int(input("Enter the number of rows or column :"))
i=num
j=num
x=num
y=num
list1=[[0 for u in range(i)]for v in range(j)]
list2=[[0 for a in range(x)]for b in range(y)]
for i in range(num):
    for j in range(num):
        list1[i][j]=int(input("Enter the number for string[{0}][{1}] :".format(i,j)))
for x in range(num):
    for y in range(num):
        list2[y][num-x-1]=list1[x][y]
print("Your matrix is : {0}".format(list1))
print("Rotation of matrix is : {0}".format(list2))

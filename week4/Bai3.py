n = int(input("Nhap so phan tu list 1 = "))
list1 = [int(input("Nhap phan tu cua list1: ")) for i in range(n)]
m = int(input("Nhap so phan tu list 2 = "))
list2 = [int(input("Nhap phan tu cua list2: ")) for i in range(m)]

list3 = []

for i in range(n):
    for j in range(m):
        if list1[i] == list2[j] and list1[i] not in list3:

            list3.append(list1[i])
print(list3)
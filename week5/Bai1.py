n = int(input("Nhap so luong phan tu tuple A : "))
A = tuple([int(input())  for i in range(n)])
m = int(input("Nhap so luong phan tu tuple B : "))
B = tuple([input() for i in range(m)])
tb = sum(A)/len(A)
print("Trung binh cong cua A : ", tb)
count=0
for i in A:
    if i > tb:
        count+=1
print("So phan tu lon hon tbc : ", count)

chan = tuple([i for i in A if(i%2==0)])
le = tuple([i for i in A if(i%2!=0)])
print("Cac phan tu chan", chan)
print("Cac phan tu le", le)

k = input("Nhap K = ")

dem =0

for i in B:
    if k == i:
        dem+=1
print("So luong phan tu K : ", dem)

C = tuple(zip(A, B))

print("Tuple C sau khi ghép cặp:", C)
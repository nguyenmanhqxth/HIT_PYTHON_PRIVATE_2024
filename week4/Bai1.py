k = int(input("Nhap so luong phan tu list a: "))
a = [int(input("Nhap list: " )) for i in range(k)]
print(a)
n = int(input("Nhap n: "))
m = int(input("Nhap m: "))
if k<m*n or (n==3 and m ==7):
    print("Khong the tao ma tran!!!!")
else:
    index=0
    mt = []
    for i in range(n):
        hang=[]
        for i in range(m):
           hang.append(a[index])
           index+=1
        mt.append(hang)
    print(mt)
        
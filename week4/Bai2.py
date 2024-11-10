n = int(input("Nhap n = "))
a = [input("Nhap phan tu cua a: ") for i in range(n)]
m = int(input("Nhap m = "))
b = [input("Nhap phan tu cua b: ") for i in range(m)]
"""zip_ab= zip(a,b)
print(list(zip_ab))"""
c=[]
for i in range(max(n,m)):
    if i < n:
        c.append(a[i])
    if i< m:
        c.append(b[i])
print(c)
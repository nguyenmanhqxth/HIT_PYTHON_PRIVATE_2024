n = int(input("Nhap so luong phan tu: "))
a = [int(input("Nhap phan tu: ")) for i in range(n)]
print(a)
a.sort()
print(a)
x = int(input("Nhap x = "))
l = 0
r = len(a) - 1
found = False

while l <= r:
    mid = (l+r)//2
    if a[mid] == x:
        found = True
        break
    elif a[mid] > x:
        r = mid -1 
        
    else:
        l = mid +1
if not found:
    mid = -1        
print(mid)



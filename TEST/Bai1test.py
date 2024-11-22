def gt(n):
    if(n==0):
        return 1
    gth = 1
    for i in range(1,n+1):
        gth*=i
    return gth

n = int(input("Nhap n = "))
x = float(input("Nhap x = "))
tong = 0
for i in range(n+1):
    tong+=x**i/gt(i)
print("e**x = ", tong)

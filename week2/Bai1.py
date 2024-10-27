a = int(input("Nhap a= "))
b = int(input("Nhap b= "))
print("a+b=", a+b)
print("a-b=",a-b)
print("a*b=",a*b)
print("a//b=",a//b) # chia nguyen
print("a**b=",a**b)
print("a%b=",a%b) # chia du
if a>b:
    print("a lớn hơn b")
elif a<b:
    print("a be hon b")
else:
    print("a bang b")
print("a AND b = ",a & b)
print("a OR b = ", a | b)
print("a XOR b = ", a ^ b)
print("NOT a==b = ", not(a==b))
print("a dich phai 5 bit : ", a >> 5)
print("a dich trai 6 bit : ", a << 6)
daonguoc = bin(a)[2:][::-1]
print("Hệ số 2 đảo ngược của a :", daonguoc)
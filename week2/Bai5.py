a = int(input("Nhap a = "))
octal_a = oct(a)[2:]
sobit = len(octal_a)*3
print("So bit can thiet : ", sobit)

x = dir(a)
print("danh sách thuộc tính và phương thức của a:")
for i in x:
    print(i)

print("Chao mung den CLB Tin Hoc HIT")
print("CLB Tin Hoc HIT truc thuoc Khoa CNTT - 10 diem")

chuoi = "CLB Tin Hoc HIT truc thuoc Khoa CNTT"

for i in chuoi:
    if(i.isupper()):
        print(i, end=" ")
print()

for i in chuoi:
    if(i.islower()):
        print(i, end =" ")
print()

if "CNTT" in chuoi:
    print("YES")
else:
    print("NO")

doi = chuoi.swapcase()
print("CHuoi sau khi doi hoa thuong", doi)

coded_str = "2[abc]3[cd]ef"

codesautach = list(coded_str)

a=""
number = 0
vitri1 = 0
vitri2 = 0

for i in range(len(codesautach)) :
    if codesautach[i] == "[":
        number = int(codesautach[i-1])
        vitri1 = i+1
    if codesautach[i] == "]":
        vitri2 = i-1
        for z in range(number):
            for j in range(vitri1,vitri2+1):
                a+=codesautach[j]

vitricuoi = coded_str.rindex("]")
if vitricuoi < len(codesautach):
    for i in range(vitricuoi+1,len(codesautach)):
        a+=codesautach[i]

print(a)






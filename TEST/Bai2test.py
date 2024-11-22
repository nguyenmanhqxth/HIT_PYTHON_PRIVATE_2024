str = input("Nhap chuoi : ")

a = list(str)

b =[]

for i in a:
    if i  not in b:
        b.append(i)
        count = 0 
        for j in a:
            if i == j:
                count+=1
        b.append(count)
print(b)


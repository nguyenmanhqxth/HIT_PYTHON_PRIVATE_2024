n = int(input('Nhập n: '))
dict = {}


for i in range(n):
    key = input("Nhập key: ")
    value = input("Nhập value: ")
    dict[key] = value


print("Dictionary ban đầu:", dict)


dict2 = {}
for k, v in dict.items():
    if v in dict2: 
        dict2[v] = "None"
    else:
        dict2[v] = k

print("Dictionary sau khi hoán đổi:", dict2)
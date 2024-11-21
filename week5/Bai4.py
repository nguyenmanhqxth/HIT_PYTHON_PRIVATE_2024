import random

majors = ["CNTT", "KHMT", "KTPM", "HTTT", "DAPT"]
N = int(input("Nhap so luong tai khoan can tao (1 <= N <= 100): "))

accounts = {
    f"Account{i+1}": {
        "Username": f"202360{i+1:04d}",
        "Password": random.choice(majors) + f"202360{i+1:04d}"
    }
    for i in range(N)
}

print("Danh sach tai khoan :")
for acc, info in accounts.items():
    print(f"{acc}: {info}")

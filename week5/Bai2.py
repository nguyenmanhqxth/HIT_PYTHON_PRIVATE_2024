A = {"Manh","Huy","Tuyet","An","Minh","Chinh"}
B = {"Huy","Tuyet","An"}
C=A-B
print("Cac ban chua check in : ", C)
print("Cac ban da dang ky va check in", len(A-C))

D =  list(A)
D.sort()
print("Sau khi sapws xeeps", D)
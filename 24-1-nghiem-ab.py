a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
if a == 0:
    if b == 0:
        print("Phuong trinh vo so nghiem")
    else:
        print("Phuong trinh vo nghiem")
else:
    x = -b/a
    print("Phuong trinh co nghiem: ",x)
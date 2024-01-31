a = float(input("nhập số thứ nhất:"))
b = float(input("nhập số thứ hai:"))
c = float(input("nhập số thứ ba:"))
if a == b and a == c:
    print("Ba số bằng nhau với giá trị bằng",a)
elif a >= b and a >= c:
    if a == b:
        print("Số thứ nhất và số thứ hai là số lớn nhất với giá trị bằng",a)
    elif a == c:
        print("Số thứ nhất và số thứ ba là số lớn nhất với giá trị bằng",a)
    else:
        print("Số thứ nhất là số lớn nhất với giá trị bằng",a)
elif b > a and b >= c:
    if b == c:
        print("Số thứ hai và số thứ ba là số lớn nhất với giá trị bằng",b)
    else:
        print("Số thứ hai là số lớn nhất với giá trị bằng",b)
else:
    print("Số thứ ba là số lớn nhất với giá trị bằng",c)
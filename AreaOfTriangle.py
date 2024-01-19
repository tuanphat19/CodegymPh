#import thư viện math
import math
#Nhập các cạnh tam giác
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
#Xuất ra màn hình
print(" Area of the triangle is: ", area)
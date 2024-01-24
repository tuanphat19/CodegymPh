#input pi
#S=diện tích hình tròn
#display S
import math,turtle
R = float(input("Nhập bán kính hình tròn (cm): "))
S = math.pi*R*R
print("S=",S)

turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(R)
turtle.end_fill()
turtle.done()
import turtle as t

n = int(input("Enter the no. of sides of Polygon: "))
length = int(input("Enter the length of sides: "))
angle = 360/n

for i in range(n):
    t.left(angle)
    t.fd(length)

def convert(radian):
    pi = 3.1415

    degree = radian * (180/pi)
    return degree

radian = int(input("Enter radians: "))
print("The angle in degrees is: ",(convert(radian)))
# angle1=int(input("Enter angle1:"))
# angle2=int(input("Enter angle2"))
# angle3=int(input("Enter angle3"))
# if angle1+angle2+angle3==180:
#     print("It is a triangle")
# else:
#     print("It is not an triangle")


angle1=int(input("enter angle1:-"))
angle2=int(input("enter angle2:-"))
angle3=180-(angle1+angle2)

if angle1+angle2+angle3==180:
    print("the third angle is:-",angle3)
else:
    print("error")

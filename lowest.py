num1=int(input("enter the number1:-"))
num2=int(input("enter the number2:-"))
num3=int(input("enter the number3:-"))

if num1<num2 and num1<num3:
    print("lowest number is:-",num1)
elif num2<num3 and num2<num1:
    print("lowest number is:-",num2)
elif num3<num2 and num3<num1:
    print("lowest number is:-",num3)
if num1>num2 and num1>num3:
    print("greatest number is:-",num1)
elif num2>num1 and num2>num3:
    print("greatest number is:-",num2)
elif num3>num1 and num3>num2:
    print("greatest number is:-",num3)
else:
    print("wrong data")
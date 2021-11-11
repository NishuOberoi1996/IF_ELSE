month=input("enter the month:-")
if int(month)==2:
    print("If the year is leap year,Your month has 29days,Else 28 days")
elif int(month)%2==0 :
    print("carry 30 days")
elif int(month)%2!=0:
    print("carry 31 days")
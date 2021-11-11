salary=int(input("enter the salary:-"))
year_of_service=int(input("enter the year:-"))
bonus=year_of_service*salary*5/100

if year_of_service>=5:
    print(salary+bonus)
else:
    print(salary)
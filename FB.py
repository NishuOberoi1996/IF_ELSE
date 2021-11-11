print("WELCOME TO FACEBOOK")
name=input("enter your name:-")
if name>="a to z" or name>="A TO Z":
    print("your name is:-",name)
    last_name=input("enter your last name:-")
    if last_name>="a to z" or last_name>="A TO Z":
        print("your last name is:-",last_name)
        birthday=input("enter birthdate:-")
        if birthday>="0" and birthday<="9" or birthday=="/":
            print(birthday)
            gender=input("enter your genter:-")
            if gender=="female" or gender=="male" or gender=="transgender":
                print(gender)
                mobile_number=int(input("enter your mobile number:-"))
                if mobile_number>=0 or mobile_number<=9:
                    print(mobile_number)
                    password=input("create your password:-")
                    if password>="1 to 99" and password>="a to z" and password=="!" or"@" or "#" or"$" or "&" or "*":
                        print(password)
                    else:
                        print("password is invalid")
                else:
                    print("mobile number is incorrect")
            else:
                print("error")
        else:
            print("you are not eligible")
    else:
        print("something went wrong")
else:
    print("name error")
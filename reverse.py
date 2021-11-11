num=int(input("enter the number:-"))
first=(num//1)%10
second=(num//10)%10
third=(num//100)%10
fourth=(num//1000)%10
reverse=(first*1000)+(second*100)+(third*10)+(fourth*1)

if num>1000:
    print(reverse)
else:
    print("error")
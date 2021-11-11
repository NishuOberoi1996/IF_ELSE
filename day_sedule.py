day=input("enter the day:-")
meal=input("enter the meal :-") 

if day=="monday":
    if meal=="breakfast":
        print("chai or bread")
    elif meal=="lunch":
        print("daal bhaat bhujia")
    elif meal=="dinner":
        print("gobhi ki sabji and bhaat")
    else:
        print("milk")
elif day=="tuesday":
    if meal=="breakfast":
        print("milk")
    elif meal=="lunch":
        print("daal bhaat chokha")
    elif meal=="dinner":
        print("mashroom rice")
    else:
        print("nothing")
elif day=="wednesday":
    if meal=="breakfast":
        print("paranthe")
    elif meal=="lunch":
        print("daal bhaat raita")
    elif meal=="dinner":
        print("aloo matter and roti")
    else:
        print("milk with horlicks")
elif day=="thursday":
    if meal=="breakfast":
        print("dalia")
    elif meal=="lunch":
        print("kadi chawal")
    elif meal=="dinner":
        print("pav bhaji")
    else:
        print("coffee")
elif day=="friday":
    if meal=="breakfast":
        print("gobhi ke paranthe")
    elif meal=="lunch":
        print("rajma chawal")
    elif meal=="dinner":
        print("aloo puri")
    else:
        print("plan milk")
elif day=="saturday":
    if meal=="breakfast":
        print("paneer ka paratha")
    elif meal=="lunch":
        print("chole chawal")
    elif meal=="dinner":
        print("chole bhature")
    else:
        print("kheer")
else:
    print("sunday holiday")
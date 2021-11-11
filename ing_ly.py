name=input("enter any name:-")

if "ingly" in name:
    print(name.replace("ingly", ""))
elif "ly" in name:
    print(name + "ing")
elif "ing" not in name  and "ly" not in name:
    print(name + "ingly")
elif "ing" in name:
    print(name + "ly")
else:
    print("wrong data")

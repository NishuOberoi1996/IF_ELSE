# print("WELCOME TO THE BANK OF INDIA")
# atm_card=input("PLEASE ENTER YOUR ATM CARD:-")
# total_amount=int(input("enter the total amount"))
# if atm_card=="debit" or atm_card=="credit":
#     print("this is your card",atm_card)
#     language=input("enter your language:-")
#     if language=="hindi" and language=="english":
#         print("english")
#         account=input("enter your account:-")
#         if account=="saving" or account=="current":
#             print(account,"enter your account")
#             pin_number=input("enter your pin :-")
#             if pin_number>="1 to 99":
#                 print(pin_number)
#                 total_amount=int(input("enter the total amount:-"))
#                 if total_amount>=1-99:
#                     print(total_amount)
#                     amount=int(input("enter the amount:-"))
#                     if amount==1-99:
#                         print(total_amount-amount)
#                         # balance_amount=float(input("balance amount:-"))
#                         # if total_amount-amount==balance_amount:
#                         #     print(total_amount-amount)
#                         slip=input("do you want slip:-")
#                         if slip=="yes" or slip=="no":
#                                 print(slip)
#                                 remove=input("please remove your card thank you")
#                                 if remove=="card is removed":
#                                     print("yes")
#                                 else:
#                                     print("card is stucked")
#                         else:
#                             print("nothing")
#                         # else:
#                         #     print("your transaction is successful")
#                     else:
#                         print("thank you")
#                 else:
#                     print("wrong data")
#             else:
#                 print("something wrong")
#         else:
#             print("your pin is incorrect")
#     elif language=="hindi":
#         print("hindi")
#         khata=input("apne khate ka prakar dale:-")
#         if khata=="chalu" or khata=="bachat":
#             print(khata)
#             pin_number=input("apne 4 anko ka pin dale :-")
#             if pin_number>="1 to 9":
#                 print(pin_number)
#                 total_amount=int(input(":-"))
#                 if total_amount>=1-99:
#                     print(total_amount)
#                     amount=int(input("enter the amount:-"))
#                     if amount==1-99:
#                         print(total_amount-amount)
#                         # balance_amount=float(input("balance amount:-"))
#                         # if total_amount-amount==balance_amount:
#                         #     print(total_amount-amount)
#                         slip=input("do you want slip:-")
#                         if slip=="yes" or slip=="no":
#                                 print(slip)
#                                 remove=input("please remove your card thank you")
#                                 if remove=="card is removed":
#                                     print("yes")
# else:
#     print("no cash")

print("WELCOME TO THE BANK OF INDIA")
atm_card=input("PLEASE ENTER YOUR ATM CARD:-")
total_amount=int(input("enter the total amount:-"))

if atm_card=="debit" or atm_card=="credit":
    print(atm_card)
    language=input("enter the language:-")
    if language=="hindi" and language=="english":
        print("english")
        account=input("enter the account:-")
        if account=="saving" or account=="current":
            print(account)
            transaction=input("enter the transaction:-")
            if transaction=="withdrawal" or transaction=="balance enquiry":
                print(transaction)
                pin_number=int(input("enter pin:-"))
                if pin_number>=0 or pin_number<=9:
                    print(pin_number)
                    withdrawal=float(input("enter the withdral amount:-"))
                    if withdrawal>0 or withdrawal==total_amount:
                        print(total_amount-withdrawal)
                        slip=input("do you want the slip:-")
                        if slip=="no":
                            print("no")
                            remove=input("please remove your card:-")
                            if remove=="ok":
                                print("removed")
                            else:
                                print("error")
                        else:
                            print("thank you")
                    else:
                        print("amount is insufficient")
                else:
                    print("wrong pin")
            elif transaction=="balance enquery":
                print(total_amount)
        else:
            print("nothing")
    elif language=="hindi":
        print(language)
        khata=input("apne khate ka prakar daale:-")
        if khata=="chalu" or khata=="bachat":
            print(khata)
            lenden=input("apna vikalp chune:-")
            if lenden=="nikashi" or lenden=="pese ki jaankaari":
                print(lenden)
                pin_number=int(input("apne khate ke 4 ank daale:-"))
                if pin_number>0 or pin_number>=9:
                    print(pin_number)
                    nikashi=int(input("jitne pese aapko nikaalne hai wo daale:-"))
                    if nikashi>0 or nikashi<=9:
                        print(total_amount-nikashi)
                        parchi=input("aapko nikashi ki purchi chahiye:-")
                        if parchi=="no":
                            print("no")
                            remove=input("apna card nikal le")
                            if remove=="ji":
                                print("thik hai")
                            else:
                                print("card fass gaya")
                        else:
                            print("dhanyawad")
                    else:
                        print("itne ank aapke khate me ni hai")
                else:
                    print("ye galat pin hai")
            elif lenden=="pese ki jaankaari":
                print(total_amount)
            else:
                print("khate me pese ni hai")
        else:
            print("khata band hai")
    else:
        print("ye language ni hai")
else:
    print("atm card kharab h scan ni ho sakta")    

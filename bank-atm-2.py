#Name:Soundharya
# Date:02-11-2021
# ATM MACHINE STYLE
print("-----------------WELCOME TO ATM MACHINE----------------------")
amount=[100000]
x=amount[0]
users=[{"pin":1234,"Name":"Aarthi","Account no":1212121212,"Bank":"SBI","Account type":"Savings","Account balance":4000},
       {"pin":5678,"Name":"Alya","Account no":1234567890,"Bank":"IOB","Account type":"Savings","Account balance":5000},
       {"pin":9012,"Name":"Ammu","Account no":1987654321,"Bank":"IFSC","Account type":"Business","Acconut balance":8000}]
Accountbalance=[]

def login():
    while True:
        tp = input("Login Admin/Login User [Type A to Login in the Admin/ Type U to Login in the User] : ")
        admin=["aarthi","ammu","anu"]
        password=["aarthi123","ammu123","anu123"]
        if tp == 'A' or tp == 'a':
            a=input("enter admin name:")
            b=input("enter password:")
            if a in admin:
                c=admin.index(a)
                d=password.index(b)
                
                if c == d:
                    admin_operation()
                    
                else:
                    print("Invalid username or ,password Please enter valid username or password")
                    login()
            else:
                print("Invalid")
                login()

        elif tp == 'U' or tp == 'u':
            print("-----------------Please insert your card---------------------")
            user_option()





def user_option():
    u_pin= int(input("Please enter your pin : "))
    u_Account=int(input("Please enter your A/c no: "))
    for detail in users:
        if detail["pin"] == u_pin or detail["Account no"] == u_Account:
            print(f'{detail["pin"]}\t{detail["Name"]}\t{detail["Account no"]}\t{detail["Bank"]}\t{detail["Account type"]}\t{detail["Account balance"]}')
        while True:    
            try:
                print("\n1.Balance\n2.Deposite\n3.Withdraw\n4.Exit")
                option=int(input("please enter your choice : "))
            except:
                print("please enter valid choice")
                user_option()
            
            
            if option ==1:
                if True:
                    print(f'Your current balance is {detail["Account balance"]}INR')
                    print("BALANCE CHECKING IS SUCCESSFULLY!")                     

            elif option==2:
                deposit_amount=int(input("Please enter the deposit amount : "))
                detail["Account balance"]=detail["Account balance"]+deposit_amount
                print(f"{deposit_amount}INR is credited from your account")
                print(f'Your current balance is {detail["Account balance"]}INR')
                print(detail["Account balance"])
                amount[0]=int(amount[0])+int(deposit_amount)
                print("CREDITED SUCCESSFULLY!")
                    
                                
            elif option==3:
                withdraw_amount=int(input("Please enter the withdraw amount : "))
                detail["Account balance"]=detail["Account balance"]-withdraw_amount
                print(f"{withdraw_amount}INR is debited from your account")
                print(f'Your current balance is {detail["Account balance"]}INR')
                amount[0]=int(amount[0])-int(withdraw_amount)
                print("DEBITED SUCCESSFULLY!")
                    
                                
            elif option==4:
                print("---------------THANK YOU!----------------")
                print("Please take your card")
                break
def admin_operation():
    print("-------------------WELCOME TO ADMIN PAGE------------------------ ")
    print("--------------------ATM DETAILS-------------------")
    print("\n1.ATM Balance")
    print(f"Total balance is {amount}INR")
             
            
login()

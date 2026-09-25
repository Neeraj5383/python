#To make basic payment for bank
import data
amount_balance = 10000


# pay to other person 
#over 2000 charge 0.4%

def debit():
    global amount_balance
    print("//" * 10, "\n")
    print("PAYMENT\n")
    print("//" * 10, "\n")
    amount_send = int(input("Enter amount : "))
    other_person = amount_balance + amount_send
    if amount_send >= 2000:
        print("0.4 charge over 2000")
        charge = (amount_balance-amount_send) * 0.4 / 100
        amount_balance -= charge + amount_send
        print(f'total amount send {amount_send} or {charge} amount charge.')
        print(f'Remaning balance {amount_balance}')
    else:
        amount_balance -= amount_send

        print(f'{amount_send} Payment successfully!!!!')
        print(f'Remaning Amount : {amount_balance}')


#Receive money from other person

def credit():
    global amount_balance
    print("//" * 10, "\n")
    print("RECEIVE\n")
    print("//" * 10, "\n")
    
    amount_rs = int(input("Enter Amount : "))
    amount_balance += amount_rs
    print(f'Amount {amount_rs} added in wallet')
    print(f'Total Amount : {amount_balance}')
    

    

def histroy():
    print("//" * 10)
    print("HISTROY")
    print("//" * 10)

    print("Enter Option")
    print("1 : last payment")
    print("2: all payment")
    hist_op = input("Enter your option : ")
    if hist_op == "1":
        pass
    elif hist_op == "2":
        pass
    else:
        print("wrong option")








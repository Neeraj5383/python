import data 


max_attempt, attempt,data1 = data.data()
def login():
    print("//" * 10, "\n")
    print("LOGIN\n")
    print("//" * 10, "\n")
    global attempt, max_attempt, data1
    while attempt < max_attempt:
        user_name : str = input("Enter Username : ")
        pass_ward = input("Enter Passward : ")
        if user_name in data1:
            for k,v in data1.items():
                
                if k == user_name and v == pass_ward:
                    print("login successfully")
                    bank()
                    
                   
                else:
                    print("wrong passward")
                    break
            break
            
        else:
            print("Wrong Username and Passward")
            attempt += 1
            if attempt < max_attempt:
                print("Try Again!!!!")
            else:
                print("Try Again after 24 hours")
                        
            
def signup():
    print("//" * 10, "\n")
    print("SIGNUP\n")
    print("//" * 10, "\n")
    global attempt, max_attempt, data1
    while attempt < max_attempt:

        
        new_user = input("Enter username : ")
        new_passward = input("Enter passward : ")


        #if user name and passward already exist in data 
        if new_user in data1:
            print("this username is all ready exist")

        #if user name and passward are not exist in date.
        else:
            print("not exist")
            print(new_user)
            print(new_passward)
            print(f"\nif this user name {new_user} or {new_passward} is correct or not ")
            print("1 : not correct")
            print("2 : correct")
            checking = input("Enter Option : ")
            match checking:
                case "1" :
                        attempt +=1
                        if attempt < max_attempt:
                            print("try again!!!")
                        else:
                            print("try after 24 hours later")
                case "2":
                    print("Here user name {",new_user, "} and passward {", new_passward,"}")
                    add_data(new_user, new_passward)
                    break
                case _:
                    print(f"wrong credential")


#add username and passward in date.
def add_data(username, passward):
    global data1
    data1[username] = passward
    print(f'Your data are save successfully!!!!!')


def bank():
    cur_bal = 5000


    while True:
        print("Select option")
        print("1 : Check your balance")
        print("2 : Do your transition")
        print("3 : Apply for loan")
        print("4 : Signout")

        user_input = input("Enter option : ")
    
        match user_input :
            case "1":
                print("Your balance is ", cur_bal, "\n")
                

            case "2":
                print("Enter option")
                print("1 : Debit")
                print("2 : credit")
                deb_cre = input("Enter your option : ")

                match deb_cre:
                    case "1":
                        debit_amount = int(input("Enter your amount : "))
                        if debit_amount <= cur_bal:
                            cur_bal = cur_bal - debit_amount 
                            print("Your current balance is ", cur_bal , "\n")
                        else:
                            print("Insufficient balance")
                            print("Your current balance is ", cur_bal ,"\n")

                    case "2":
                        credit_amount = int(input("Enter your amount : "))
                        cur_bal = credit_amount + cur_bal
                        print("Your current balance is ", cur_bal, "\n")
                    case _:
                        print("Wrong selection!!!\n")
                
            
            case "3":
                print("appling for load\n")
                

            case "4":
                print("Signout")
                break
            case _:
                print("Wrong selection!!!\n")


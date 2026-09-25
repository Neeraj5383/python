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
                    break
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
                        
            print("login successfully")
            break
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
            if checking == "1":
                attempt +=1
                if attempt < max_attempt:
                    print("try again!!!")
                else:
                    print("try after 24 hours later")
            elif checking == "2":
                print("Here user name {",new_user, "} and passward {", new_passward,"}")
                add_data(new_user, new_passward)
                break
            else:
                print(f"wrong credential")


#add username and passward in date.
def add_data(username, passward):
    global data1
    data1[username] = passward
    print(f'Your data are save successfully!!!!!')
    print(data1)
    print(len(data1))

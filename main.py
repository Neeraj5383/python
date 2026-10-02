import start

print("//" * 15, "\n")
print("WELCOME TO ALL IN ONE BANK", "\n")
print("//" * 15, "\n")


def excut():
    while True:
        print("select option")
        print("1: login")
        print("2: Signup")
        user = input("Enter option : ")

        # if user == '1':
        #    start.login()
        # elif user == '2':
        #    start.signup()

        # else:
        #    print(f'Wrong Credential!!!!')
        match user:
            case "1": start.login()
            case "2": start.signup()
            case _: print("Wrong Credential!!!!!")
if __name__ == "__main__":
    excut()
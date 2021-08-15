import getuser
import os
username = getuser.lookup_username()

def wsl():
    while True:
        command = input(r""+username+" |> ")
        if command != "stop":
            if command != "cls":
                if command != "brr":
                    if command != "ide":
                        print(command)
                    else:
                        os.system('' if os.name == 'nt' else 'clear')
                else:
                    print("BRRRRRRRRRRRRRRRRR")
                    print("BRRRRRRRRRRRRRRRRR")
                    print("BRRRRRRRRRRRRRRRRR")
                    print("BRRRRRRRRRRRRRRRRR")
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
        else:
            exit(0)         
wsl()

i = 1
while i <= 5:
    username = input("ENTER USERNAME: ")
    password = input("ENTER PASSWORD: ")
    if username == "python" and password == "rules":
        print("WELCOME")
        break
    else:
        print("You entered Wrong Credentials for the " + str(i) + " times")
        i = i + 1
else:
    print("ACCESS DENIED")
while True:
    determined_username = "irem"
    determined_password = "010101cs"
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    if username == determined_username and password == determined_password:
        print("You entered the correct username and password!")
        exit()
    elif username !=determined_username or password !=determined_password:
        print("You entered the incorrect username and password!")
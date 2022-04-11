from Entities.user import User


def register_user(movies, users):
    print("*** Welcome to registration page ***")
    name = input("Name = ")
    email = input("Email = ")

    password = input("Password = ")
    if email in users.ulist:
        print("User Already present, you can perform login")
    else:
        users.add_user(User(name, email, password))
        print("User successfully registered")
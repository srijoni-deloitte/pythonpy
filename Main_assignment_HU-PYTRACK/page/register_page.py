from Entities.user import user


def register_user(movies, users):
    print("*** Welcome to registration page ***")
    name = input("[str] Name = ")
    email = input("[str] Email = ")

    password = input("[str] Password = ")
    if email in users.ulist:
        print("user Already present, you can perform login")
    else:
        users.add_user(user(name, email, password))
        print("user successfully registered")
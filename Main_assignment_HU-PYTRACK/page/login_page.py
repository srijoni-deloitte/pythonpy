from db_package.db_shows import MovieList
from db_package.db_customer import UserList
from Admin_Functionality.function import Admin

def user_login(movies, users,username,password):
    print("*** Welcome to User Login page")
    email = username

    if email not in users.ulist.keys():
        print("No user present with this username or email address. Register yourself")
        return
    if users.ulist[email].details['password'] != password:
        print("Wrong password")
        return

    print("Login successful")
    user = users.ulist[email]

    print(f"Welcome ",user.details['name'])
    while True:
        print("***** Movie List *****")
        lst = movies.get_movie_list()
        if len(lst) == 0:
            print("No movie has been registered yet")
            return
        for i in range(len(lst)):
            print(i+1," ", lst[i])
        inp = int(input("Enter the number corresponds to the movie = ")) - 1
        if inp >= len(lst) or inp < 0:
            print("Not a proper movie index")
            continue
        mv = movies.mlist[lst[inp]]
        print(mv)

        print("1. Book ticket")
        print("2. Cancel ticket")
        print("3. Give user rating")
        print("4. exit")
        inp = int(input())
        if inp == 1:
            print("choose timing")
            slots = mv.get_timings()
            for i in range(len(slots)):
                print(i+1,". ", slots[i][0], ", has ",slots[i][1], ", seats")
            inp = int(input()) - 1
            user.book_show(mv, slots[inp][0], int(input("No of Seats = ")))
        elif inp == 2:
            print("choose timing")
            slots = mv.get_timings()
            for i in range(len(slots)):
                print(i+1,". ", slots[i][0], ", has ",slots[i][1], ", seats")
            inp = int(input()) - 1
            print("number of seats to be cancelled")
            user.cancel_show(mv, slots[inp][0], int(input("NO of seats = ")))
        elif inp == 3:
            user.give_user_rating(int(input("Give a number between 1 to 10 = ")), mv)
            print("Avg movie rating = ", mv.get_user_rating())
        else:
            break

def admin_login(movies,username,password):
    admin = Admin()
    print("*** ADMIN LOGIN ***")
    try:

        if not admin.login(username , password):
            raise Exception("Admin Login data not matching")
    except Exception as e:
        print(e)
        return
    while True:
        print("**Welcome Admin***", username)
        print("1. Add new Movie")
        print("2. Edit movie")
        print("3. Delete Movie")
        print("4. Logout")
        ip = input()
        if ip == '1':
            admin.add_movie(movies)
        elif ip == '2':
            admin.edit_movie(movies)
        elif ip == '3':
            admin.delete_movie(movies)
        else:
            admin.logout()
            return



def ipUPASS():
    username=input("Username = ")
    password=input("Password = ")
    return username,password
def login(movies, users):
    while True:
        print("****** Welcome to BookMyShow Login *******")
        print("1. Admin Login")
        print("2. User Login")
        print("3. exit")

        inp = input()
        if inp == '1':
            username,password=ipUPASS()
            admin_login(movies,username,password)
        elif inp == '2':
            username, password = ipUPASS()
            user_login(movies, users,username,password)
        else:
            break

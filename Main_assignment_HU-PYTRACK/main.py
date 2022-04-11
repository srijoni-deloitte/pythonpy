from tkinter import TOP, RIGHT, LEFT

from page.login_page import login
from page.register_page import register_user
from db_package.db_shows import MovieList
from db_package.db_customer import UserList
import tkinter as tk

movies = MovieList()
users = UserList()
frame = tk.Tk()
frame.title("Welcome to INOX")
frame.geometry('400x200')
while True:

    def log():
        login(movies, users)
        print(*movies.mlist.values())

    def RegisterNewAccount():
        print(register_user(movies, users))
    def exit1():
        frame.destroy()
        exit(0)

    b1 = tk.Button(frame, text="Login", command=log, activeforeground="red", activebackground="pink", pady=10)

    b2 = tk.Button(frame, text="Register New Account", command=RegisterNewAccount, activeforeground="blue", activebackground="pink", pady=10)

    b3 = tk.Button(frame, text="EXIT", command=exit1, activeforeground="green", activebackground="pink", pady=10)
    b1.pack(side=LEFT)

    b2.pack(side=RIGHT)

    b3.pack(side=TOP)

    frame.mainloop()

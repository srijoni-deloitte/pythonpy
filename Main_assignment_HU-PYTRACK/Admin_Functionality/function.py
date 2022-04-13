from db_package.db_shows import MovieList
from Entities.movie import movie
import csv


def getMins(s) -> int:
    s = s.split(",")
    hr, mins = s[0], s[1]
    if int(hr)==0:
        return int(mins)
    else:
        return hr*60+mins


class Admin:
    def __init__(self):
        data = list(csv.reader(open('C:\\Users\\srijochakraborty\\Documents\\codes\\pythonpy\\Main_assignment_HU-PYTRACK\\admin_details.csv')))
        self.username = data[1][0]
        self.password = data[1][1]

    def login(self, username, password) -> bool:
        return self.username == username and self.password == password

    def create_movie(self) -> movie:
        title = input("[str] Title = ")
        genre = input("[str] Genre = ")
        length = getMins(input("([hr.min] Length = "))
        cast = input("[str] Cast = ")
        director = input("[str] Director = ")
        rating = input("[int|10] Admin Rating = ")
        language = input("[str] Language = ")
        showCnt = int(input("[int]No of shows in a day = "))
        fs = getMins(input("[hr,min] First Show = "))
        interval = input("[int| mins]Interval timing = ")
        gap = getMins(input("[hr,min] Gaps = "))
        cap = int(input("[int] Capacity = "))
        return movie(title, genre, length, cast, director, rating, language, showCnt, fs, interval, gap, cap)

    def add_movie(self, movies: MovieList):
        print("***** Welcome admin to add movie *****")
        mv = self.create_movie()
        title = mv.movie_details['title']
        if title not in movies.mlist.keys(): movies.add_movie(mv)
        else: print("movie already listed")

    def edit_movie(self, movies: MovieList):
        print("***** Admin Edit movie *****")
        mv = self.create_movie()
        if mv.movie_details['title'] in movies.mlist.keys():
            movies.mlist[mv.movie_details['title']] = mv
            print("Update successful")
        else:
            print("NO movie of this title")

    def delete_movie(self, movies: MovieList):
        print("***** Admin Delete movie *****")
        lst = list(movies.mlist.keys())
        for i in range(len(lst)):
            print(str(i+1),". ",str(lst[i]))
        inp = int(input("Enter the movie index to delete = ")) - 1
        movies.mlist.pop(lst[inp])

    def logout(self):
        print("Admin successfully logged out")
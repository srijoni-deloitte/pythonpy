from db_package.db_shows import MovieList
from Entities.movie import Movie
import csv


def getMins(s: str, foundHr: bool) -> int:
    s = s.split()
    hr, mins = 0, 0
    for i in s:
        if '0' <= i[0] <= '9':
            if not foundHr: hr, foundHr = int(i), True
            else: mins = int(i)
    return hr*60+mins


class Admin:
    def __init__(self):
        data = list(csv.reader(open('C:\\Users\\srijochakraborty\\Documents\\codes\\pythonpy\\Main_assignment_HU-PYTRACK\\admin_details.csv')))
        self.username = data[1][0]
        self.password = data[1][1]

    def login(self, username, password) -> bool:
        return self.username == username and self.password == password

    def get_movie(self) -> Movie:
        title = input("Title = ")
        genre = input("Genre = ")
        length = getMins(input("Length = "), False)
        cast = input("Cast = ")
        director = input("Director = ")
        rating = input("Admin Rating = ")
        language = input("Language = ")
        showCnt = int(input("No of shows in a day = "))
        fs = getMins(input("First Show = "), False)
        interval = getMins(input("Interval timing = "), True)
        gap = getMins(input("Gaps = "), True)
        cap = int(input("Capacity = "))
        return Movie(title, genre, length, cast, director, rating, language, showCnt, fs, interval,gap, cap)

    def add_movie(self, movies: MovieList):
        print("***** Welcome admin to add movie *****")
        mv = self.get_movie()
        title = mv.movie_details['title']
        if title not in movies.mlist.keys(): movies.add_movie(mv)
        else: print("Movie already listed")

    def edit_movie(self, movies: MovieList):
        print("***** Admin Edit Movie *****")
        mv = self.get_movie()
        if mv.movie_details['title'] in movies.mlist.keys():
            movies.mlist[mv.movie_details['title']] = mv
            print("Update successful")
        else:
            print("NO movie of this title")

    def delete_movie(self, movies: MovieList):
        print("***** Admin Delete Movie *****")
        lst = list(movies.mlist.keys())
        for i in range(len(lst)):
            print(f"{i+1}. {lst[i]}")
        inp = int(input("Enter which movie you want to delete = ")) - 1
        movies.mlist.pop(lst[inp])

    def logout(self):
        print("Admin successfully logged out")
from Entities.movie import Movie


class MovieList:
    def __init__(self):
        self.mlist = dict()

    def __str__(self):
        return str(list(self.mlist.keys()))

    def get_movie_list(self) -> list:
        return list(self.mlist.keys())

    def add_movie(self, movie: Movie):
        self.mlist[movie.movie_details['title']] = movie

    def del_movie(self, movie_name: str):
        try:
            self.mlist.pop(movie_name)
        except:
            print("Movie not found")

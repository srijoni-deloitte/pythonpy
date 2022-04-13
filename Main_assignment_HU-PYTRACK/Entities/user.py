from Entities.movie import movie

class user:
    def __init__(self, name, email, password):
        self.details = {'name': name, 'email': email, 'password': password}
        self.bookings = dict()

    def show_booking_details(self):
        for k, v in self.bookings.items():
            print(str(k) ," => ",str(v))

    def show_all_bookings(self) :
        res = list(self.bookings.keys())
        for i in range(len(res)):
            print(str(i+1),". ",str(res[i]))
        return res

    def show_timings(self, title: str):
        res = list(self.bookings[title].keys())
        for i in range(len(res)):
            print(str(i+1),". ",str(res[i]))
        return res

    def book_show(self, movie: movie, timing: str, seats: int):
        if movie.time_slot[timing] >= seats:
            movie.time_slot[timing] -= seats
            title = movie.movie_details['title']
            if title in self.bookings:
                if timing in self.bookings[title]:
                    self.bookings[title][timing] += seats
                else:
                    self.bookings[title][timing] = seats
            else:
                self.bookings[title] = {timing: seats}
        else:
            print("NOT ENOUGH SEATS IS PRESENT AS PER YOUR REQUIREMENT")

    def cancel_show(self, movie: movie, timing: str, seats: int):
        print(self.bookings)
        title = movie.movie_details['title']
        if title not in self.bookings:
            print("No booking of "+str(title)," movie")
            return
        if timing not in self.bookings[title]:
            print("You have no booking of ",str(title)," at ",str(timing),", slot")
            return

        if seats > self.bookings[title][timing]:
            print("You are trying to cancel more seats than you have booked")
        else:
            self.bookings[title][timing] -= seats
            movie.time_slot[timing] += seats
            if self.bookings[title][timing] == 0:
                self.bookings[title].pop(timing)
            if len(self.bookings[title]) == 0:
                self.bookings.pop(title)
            print("Cancellation successful")

    def give_user_rating(self, rating, movie):
        rating = max(1, rating)
        rating = min(10, rating)
        title = movie.movie_details['title']
        if title not in self.bookings:
            print("You haven't watch the movie yet")
            return
        movie.add_user_rating(rating)
        print("user rating added")
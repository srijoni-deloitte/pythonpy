class movie:
    def __init__(self, title, genre, length, cast, director, rating, language, showcnt, firstShow, interval, gap, cap):
        self.movie_details = {'title': title, 'genre': genre, 'len': length, 'rating': rating, 'lan': language}
        self.makers = {'cast': cast, 'director': director}
        self.time_slot = dict()
        self.user_rating = []
        cur, cnt = firstShow, 0
        while cur <= 24*60 and cnt < showcnt:
            st, en = cur, cur+interval+length
            if en > 24*60:
                break
            key = str(st//60)+":"+str(st%60) + " - " + str(en//60) + ":" + str(en%60)
            self.time_slot[key] = cap
            cur = en + gap
            cnt += 1

    def __str__(self):
        res = ""
        for k, v in self.movie_details.items():
            res += str(k)+" = "+str(v)+"\n"
        for k, v in self.makers.items():
            res += str(k)+" = "+str(v)+"\n"
        for k, v in self.time_slot.items():
            res += str(k)+ " slot has "+ str(v)+ "seats\n"
        return res

    def get_timings(self) -> list:
        return [[k, v] for k, v in self.time_slot.items()]

    def add_user_rating(self, rating: int):
        self.user_rating.append(rating)
        print(rating)
        print(self.user_rating)

    def get_movie_rating(self):
        ans = 0
        try:
            ans = round(sum(self.user_rating)/len(self.user_rating), 1)
        except ZeroDivisionError:
            print("No ratings available")
        finally:
            return ans
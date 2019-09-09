


class Recommender:.
    def __init__(self, naborusers):
        users = 0
        naborusers = dict()
        self.naborusers = naborusers

    def get_next(self, user_id):
        picture = random.choice()  # в скобках будет массив картин любимого жанра пользователя
        return picture

    def update(self, user_id):
        naborusers = ([a for a in range(10)])  # сам выберешь сколько у нас будет юзеров это я сделал как пример
        for users in naborusers:
            naborusers[
                users] = user_id  # я не знаю как сделать так чтобы программа запоминала сколько в данный момент юзеров у нас. Это сам сделаешь
            break

    def new_user(self):
        self.users += 1
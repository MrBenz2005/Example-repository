class Man(object):
    def __init__(self, name=""):
        self.name = name

    def walk(self):
        print(self.name, "i am walking")

    def human(self):
        print("i wanna human")

    def eat(self):
        print("i like eat meal of cow")

class BatMan(Man):
    def walk(self):
        print(self.name, "i am flying")

    def human(self):
        print("i wanna human")

    def eat(self):
        super().eat()
        print("I like eat meal of bat")


class LazyDict(dict):
    def __delitem__(self, key):
        if key not in super().keys():
            return None
        else:
             super().__delitem__(key)

    def __getitem__(self, item):
        if item not in super().items():
            return None
        else:
            return super().__getitem__(item)



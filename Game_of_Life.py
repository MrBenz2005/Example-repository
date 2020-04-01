from copy import deepcopy

class LifeGame:
    def __init__(self, array: list):
        self.__array = array
        self.array = deepcopy(array)
        self.height = len(array)
        self.length = len(array[0])

    def get_next_generation(self):
        for i in self.__array:
            for j in self.__array[i]:
                num = self._number_of_neighbours(i,j)
                if self.array[i][j] == 1:
                    if num == 3 or num == 2:
                        self.array[i][j] = 1
                    else:
                        self.array[i][j] = 0
                if self.array[i][j] == 0:
                    if num == 3:
                        self.array[i][j] = 1


    def _number_of_neighbours(self, x, y):
        count = 0
        """ЕСЛИ КЛЕТКА НЕ НА КРАЯХ"""
        if y != 0 and x != 0:
            for j in range(self.array[x - 1][y - 1], self.array[x - 1][y + 1]):
                if j == 1:
                    count += 1
            for j in range(self.array[x + 1][y - 1], self.array[x + 1][y + 1]):
                if j == 1:
                    count += 1
            if self.array[x][y - 1] == 1:
                count += 1
            if self.array[x][y + 1] == 1:
                count += 1
        """ЕСЛИ КЛЕТКА НА В ЛЕВОМ ВЕРХНЕМ УГЛУ"""
        if x == 0 and y == 0:
            for j in range(self.array[x - 1][y], self.array[x - 1][y + 1]):
                if j == 1:
                    count += 1
            if self.array[x][y + 1] == 1:
                count += 1
        """ЕСЛИ КЛЕТКА В ЛЕВОМ НИЖНЕМ УГЛУ"""
        if y == 0 and x == self.height:
            for j in range(self.array[self.height - 1][y], self.array[self.height - 1][y + 1]):
                if j == 1:
                    count += 1
            if self.array[self.height][y + 1] == 1:
                count += 1
        """ЕСЛИ КЛЕТКА В ПРАВОМ НИЖНЕМ УГЛУ"""
        if x == self.height and y == self.length:
            for j in range(self.array[self.height - 1][self.length - 1], self.array[self.height - 1][self.length]):
                if j == 1:
                    count += 1
            if self.array[self.height][self.length - 1] == 1:
                count += 1
        """ЕСЛИ КЛЕТКА В ПРАВОМ ВЕРХНЕМ УГЛУ"""
        if y == self.length and x == 0:
            for j in range(self.array[x + 1][self.length - 1], self.array[x - 1][self.length]):
                if j == 1:
                    count += 1
            if self.array[x][self.length - 1]:
                count += 1
        """ЕСЛИ КЛЕТКА НА ЛЕВОЙ СТОРОНЕ"""
        if x != 0 and y == 0:
            for j in range(self.array[x - 1][y], self.array[x - 1][y + 1]):
                if j == 1:
                    count += 1
            for j in range(self.array[x + 1][y], self.array[x + 1][y + 1]):
                if j == 1:
                    count += 1
            if self.array[x][y + 1]:
                count += 1
        """ЕСЛИ КЛЕТКА НА НИЖНЕЙ СТОРОНЕ"""
        if y != 0 and x == self.height:
            for j in range(self.array[self.height - 1][y - 1], self.array[self.length - 1][y + 1]):
                if j == 1:
                    count += 1
            if self.array[self.height][y - 1]:
                count += 1
            if self.array[self.height][y + 1]:
                count += 1
        """ЕСЛИ КЛЕТКА НА ПРАВОЙ СТОРОНЕ"""
        if x != 0 and y == self.length:
            for j in range(self.array[x - 1][self.length - 1], self.array[x - 1][self.length]):
                if j == 1:
                    count += 1
            for j in range(self.array[x + 1][self.length - 1], self.array[x + 1][self.length]):
                if j == 1:
                    count += 1
            if self.array[x][self.length - 1]:
                count += 1
        """ЕСЛИ КЛЕТКА НА ВЕРХНЕЙ СТОРОНЕ"""
        if y != 0 and x == 0:
            for j in range(self.array[x + 1][y - 1], self.array[x + 1][y + 1]):
                if j == 1:
                    count += 1
            if self.array[x][y + 1]:
                count += 1
            if self.array[x][y - 1]:
                count += 1
        return count
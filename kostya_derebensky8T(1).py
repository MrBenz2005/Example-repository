import copy
class MyMatrix:
    def __init__(self, data: list):
        self.__data = copy.deepcopy(data)

    def __repr__(self) -> str:
        spisok = ""
        for i in range(len(self.__data)):
            for j in range(len(self.__data[i])):
                if self.__data[i][j] == self.__data[i][-1]:
                    spisok += str(self.__data[i][j]) + "\n"
                else:
                    spisok += str(self.__data[i][j]) + " "
        return spisok
        #Hint: use '\n' for line break
        #raise NotImplementedError

    def size(self) -> tuple:
        hight = len(self.__data)
        lenght = len(self.__data[0])
        return hight,lenght
        #raise NotImplementedError

    def flip_up_down(self):
        flipnuty = copy.deepcopy(self.__data)
        flipnuty[0] = self.__data[1]
        flipnuty[1] = self.__data[0]
        spisok = ""
        for i in range(len(flipnuty)):
            for j in range(len(flipnuty[i])):
                if flipnuty[i][j] == flipnuty[i][-1]:
                    spisok += str(flipnuty[i][j]) + "\n"
                else:
                    spisok += str(flipnuty[i][j]) + " "
        return spisok
        #raise NotImplementedError

    def flip_left_right(self):
        """
        E.g. modify
        1, 2, 3, 4   to   4, 3, 2, 1
        5, 6, 7, 8        8, 7, 6, 5
        """
        raise NotImplementedError

    # методы flip_ ИЗМЕНЯЮТ матрицу
    # методы flipped_ по сути делают то же самое,
    # но возвращают изменённую КОПИЮ матрицы
    def flipped_up_down(self):
        raise NotImplementedError

    def flipped_left_right(self):
        raise NotImplementedError

    def transpose(self):
        """
        E.g. modify
                          1, 5
        1, 2, 3, 4   to   2, 6
        5, 6, 7, 8        3, 7
                          4, 8
        """
        raise NotImplementedError
    def transposed(self):
        """
        Return transposed copy of MyMatrix.
        """
        raise NotImplementedError

datas = [[1,20,3],[23,4,1]]
klass = MyMatrix(datas)
print(repr(klass)) # klass.__repr__()
print(klass.size())
print(klass.flip_up_down())
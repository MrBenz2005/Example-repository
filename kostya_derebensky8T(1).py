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

    def norm_wyvod(self,cpicsok):
        spisok = ""
        for i in range(len(cpicsok)):
            for j in range(len(cpicsok[i])):
                if cpicsok[i][j] == cpicsok[i][-1]:
                    spisok += str(cpicsok[i][j]) + "\n"
                else:
                    spisok += str(cpicsok[i][j]) + " "
        return spisok

    def size(self) -> tuple:
        hight = len(self.__data)
        lenght = len(self.__data[0])
        return hight,lenght
        #raise NotImplementedError

    def flip_up_down(self):
        flipnuty = copy.deepcopy(self.__data)
        self.__data[0] = flipnuty[1]
        self.__data[1] = flipnuty[0]
        return self.norm_wyvod(self.__data)

    def flip_left_right(self):
        flipnuty = copy.deepcopy(self.__data)
        spicok = ""
        for i in range(len(flipnuty)):
            for j in range(len(flipnuty[i])):
                if self.__data[i][j] == self.__data[i][-1]:
                    self.__data[i][j] = flipnuty[i][-j-1]
                else:
                    self.__data[i][j] = flipnuty[i][-j-1]

        return self.norm_wyvod(self.__data)

    # методы flip_ ИЗМЕНЯЮТ матрицу
    # методы flipped_ по сути делают то же самое,
    # но возвращают изменённую КОПИЮ матрицы
    def flipped_up_down(self):
        raise NotImplementedError

    def flipped_left_right(self):
        flipnuty = copy.deepcopy(self.__data)
        spicok = ""
        for i in range(len(flipnuty)):
            for j in range(len(flipnuty[i])):
                if self.__data[i][j] == self.__data[i][-1]:
                    flipnuty[i][j] = self.__data[i][-j - 1]
                else:
                    flipnuty[i][j] = self.__data[i][-j - 1]
        return self.norm_wyvod(flipnuty)


    def transpose(self):
        trans = copy.deepcopy(self.__data)
        spicok = ""
        for i in range(len(trans) // 2):
            for j in range(len(trans[i])):
                spicok += str(trans[0][j]) + ',' + str(trans[1][j]) + "\n"

        return spicok
    def transposed(self):
        trans = copy.deepcopy(self.__data)
        spicok = ""
        for i in range(len(trans) // 2):
            for j in range(len(trans[i])):
                spicok += str(trans[0][j]) + ',' + str(trans[1][j]) + "\n"
        raise NotImplementedError

datas = [[1,2,3],[4,5,6]]
klass = MyMatrix(datas)
print(repr(klass)) # klass.__repr__()
print(klass.size())
print(klass.flip_up_down())
print(klass.flip_left_right())
print(klass.transpose())
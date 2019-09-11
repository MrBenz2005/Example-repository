class MyMatrix:
    def __init__(self, data: list):
        self.__data = data

    def __repr__(self) -> str:
        spisok = ""
        for i in range(len(self.__data)):
            for j in range(len(self.__data[i])):
                spisok += str(self.__data[i][j])
        return spisok
        #Hint: use '\n' for line break
        #raise NotImplementedError


    def size(self) -> tuple:
        """
        Return tuple(height, width) for matrix.
        Example: (2, 4)
        """
        raise NotImplementedError


    def flip_up_down(self):
        """
        E.g. modify
        1, 2, 3, 4   to   5, 6, 7, 8
        5, 6, 7, 8        1, 2, 3, 4
        """
        raise NotImplementedError

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
klass = MyMatrix()
datas = [[1,20,3],[23,4,1]]
klass.__init__(datas)
print(klass.__repr__())
import copy

class MyMatrix:
    def __init__(self, data: list):
        self.__data = copy.deepcopy(data)

    def __repr__(self) -> str:
        data_str = ''
        for i in range(len(self.__data)):
            for j in range(len(self.__data[i])):
                if j < 0:
                    data_str += str(self.__data[i][j]) + ' '
                if j == 0:
                    data_str += str(self.__data[i][j])
                if j > 0:
                    data_str += ' ' + str(self.__data[i][j])
                if i != len(self.__data) - 1 and j+1 == len(self.__data[i]):
                    data_str += '\n'
        return data_str

    def norm_wyvod(self, cpicsok):
        spisok = ""
        for i in range(len(cpicsok)):
            for j in range(len(cpicsok[i])):
                if j == 3:
                    spisok += str(cpicsok[i][j]) + "\n"
                else:
                    spisok += str(cpicsok[i][j]) + " "
        return spisok

    def size(self) -> tuple:
        return len(self.__data), len(self.__data[0])

    def flipped_up_down(self):
        if len(self.__data) > 0:
            size = int(len(self.__data) / 2)
            data2 = copy.deepcopy(self.__data)
            data = copy.deepcopy(self.__data)
            for i in range(size):
                data[i] = data2[len(data2) - 1 - i]
                data[len(data2) - 1 - i] = data2[i]
            return MyMatrix(data)
        else:
            return MyMatrix([])


    def flipped_left_right(self):
        if len(self.__data) > 0:
            size = int(len(self.__data[0]) / 2)
            data2 = copy.deepcopy(self.__data)
            data = copy.deepcopy(self.__data)
            for i in range(len(data)):
                for j in range(size):
                    data[i][j] = data2[i][len(data2[i]) - 1 - j]
                    data[i][len(data2[i]) - 1 - j] = data2[i][j]
            return MyMatrix(data)
        else:
            return MyMatrix([])


    def transpose(self):
        transposed_data = []
        datac = self.__data
        for j in range(len(datac[0])):
            tmp = []
            for i in range(len(datac)):
                tmp += [datac[i][j]]
            transposed_data += [tmp]
        self.__data = transposed_data
        return self.__data


    def transposed(self):
        if (len(self.__data) != 0):
            data = [[] for i in range(len(self.__data[0]))]
            for i in range(len(self.__data[0])):
                for j in range(len(self.__data)):
                    data[i].append(self.__data[j][i])
            return MyMatrix(data)
        else:
            return MyMatrix([])


    def data(self):
        return copy.deepcopy(self.__data)

    def __add__(self, matrix2):
        matrix1 = copy.deepcopy(self.__data)
        matrix3 = []
        rows1 = 0
        rows2 = 0
        columns1 = 0
        columns2 = 0
        for i in range(len(matrix1)):
            for j in range(len(matrix1[i])):
                columns1 += 1
            rows1 += 1
        if columns1 != 0 and rows1 != 0:
            columns1 = int(columns1 / rows1)

        for i in range(len(matrix2)):
            for j in range(len(matrix2[i])):
                columns2 += 1
            rows2 += 1
        if columns2 != 0 and rows2 != 0:
            columns2 = int(columns2 / rows2)

        if columns1 == columns2 and rows1 == rows2:
            if matrix3 != []:
                del matrix3[:]
        for i in range(rows1):
            matrix3.append([])

        for i in range(rows1):
            for j in range(columns1):
                x = matrix1[i][j] + matrix2[i][j]
                matrix3[i].append(x)

        del matrix1[:]
        for i in matrix3:
            matrix1.append(i)
        return self.norm_wyvod(matrix3)

    def __sub__(self, matrix2):
        matrix1 = copy.deepcopy(self.__data)
        matrix3 = []
        rows1 = 0
        rows2 = 0
        columns1 = 0
        columns2 = 0
        for i in range(len(matrix1)):
            for j in range(len(matrix1[i])):
                columns1 += 1
            rows1 += 1
        if columns1 != 0 and rows1 != 0:
            columns1 = int(columns1 / rows1)

        for i in range(len(matrix2)):
            for j in range(len(matrix2[i])):
                columns2 += 1
            rows2 += 1
        if columns2 != 0 and rows2 != 0:
            columns2 = int(columns2 / rows2)

        if columns1 == columns2 and rows1 == rows2:
            if matrix3 != []:
                del matrix3[:]
        for i in range(rows1):
            matrix3.append([])

        for i in range(rows1):
            for j in range(columns1):
                x = matrix1[i][j] - matrix2[i][j]
                matrix3[i].append(x)

        del matrix1[:]
        for i in matrix3:
            matrix1.append(i)
        return self.norm_wyvod(matrix3)


    def __isub__(self, other):
        self.__data = (MyMatrix(self.__data) - other).data()
        return self.__data


    def __iadd__(self, other):
        self.__data = (MyMatrix(self.__data) + other).data()
        return self.__data




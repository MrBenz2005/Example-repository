import copy
class MyMatrix:
    def __init__(self, matric2: list):
        self.__data = copy.deepcopy(matric2)

    def __repr__(self) -> str:
        spisok = ""
        for i in range(len(self.__data)):
            for j in range(len(self.__data[i])):
                if j == 3:
                    spisok += str(self.__data[i][j]) + "\n"
                else:
                    spisok += str(self.__data[i][j]) + " "
        return spisok

    def norm_wyvod(self,cpicsok):
        spisok = ""
        for i in range(len(cpicsok)):
            for j in range(len(cpicsok[i])):
                if j == 3:
                    spisok += str(cpicsok[i][j]) + "\n"
                else:
                    spisok += str(cpicsok[i][j]) + " "
        return spisok

    def __add__(self,matrix2):
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

    def __sub__(self,matrix2):
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

    def __iadd__(self, matrix):
        matrix1 = copy.deepcopy(self.__data)
        pass


    def __isub__(self, matrix):
        pass

    def foo3(self):  # change the name!
        raise NotImplementedError
        # этот метод должен позволять ИЗМЕНЯТЬ элемент по индексу,
        # например, matrix[1, 2] = 5
        # какие у них должны быть названия, опять же вопрос к вам

    def foo4(self):  # change the name!
        raise NotImplementedError

def test_add():
    matric = [[1, 2, 3, 4], [5, 6, 7, 8]]
    matric1 = [[9, 10, 11, 12], [13, 14, 15, 16]]
    stack = MyMatrix(matric1)
    matric3 = stack + matric
    assert(matric3 == '10 12 14 16\n18 20 22 24')
#test_add()

def test_sub():
    matric = [[1, 2, 3, 4], [5, 6, 7, 8]]
    matric1 = [[9, 10, 11, 12], [13, 14, 15, 16]]
    stack = MyMatrix(matric1)
    matric3 = stack - matric
    assert(matric3 == '0 0 0 0\n0 0 0 0')
#test_sub()

def test_foo1():
    stack = MyMatrix()
    assert(stack.size() == 0)
    stack.push(1)
    assert(stack.size() == 1)
    stack.push(2)
    assert(stack.size() == 2)
    stack.pop()
    assert(stack.size() == 1)
#test_foo1()

def test_foo2():
    stack = MyMatrix()
    assert (stack.size() == 0)
    stack.push(1)
    assert (stack.size() == 1)
    stack.is_empty()
    stack.pop()
    stack.is_empty()
    assert (stack.is_empty() == True)
#test_foo2()

def test_foo3():
    stack = MyMatrix()
    stack.push(1)
    assert (stack.top() == 1)
    stack.push(2)
    stack.top()
    assert (stack.top() == 2)
#test_foo3()

def test_foo4():
    stack = MyMatrix()
    stack.push(1)
    assert (stack.pop() == 1)
    stack.push(7)
    assert (stack.pop() == 7)
#test_foo4()

def test_push():
    stack = MyMatrix()
    stack.push(1)
    assert (stack.top() == 1)
    stack.push(3)
    assert (stack.pop() == 3)
#test_push()



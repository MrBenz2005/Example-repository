# https://colab.research.google.com/drive/1YR-D8XJ3uLIHzOy6LW8v-QlN6lO8zTwk
class MyStack:
    # следующие два метода класса нужны для того,
    # чтобы можно было делать
    # matrix3 = matrix1 + matrix2, matrix3 = matrix1 - matrix2
    # если матрицы не одного размера, кидайте ошибку MatrixError с разумным сообщением
    def __add__(self,matrix1,matrix2):
        matrix3 = []
        rows1 = 0
        rows2 = 0
        columns1 = 0
        columns2 = 0
        for i in range(len(matrix1)):
            for j in range(len(matrix1[i])):
                columns1 += 1
            rows1 += 1
        columns1 = int(columns1 / rows1)

        for i in range(len(matrix2)):
            for j in range(len(matrix2[i])):
                columns2 += 1
            rows2 += 1
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
        return matrix3

    def __sub__(self,matrix1,matrix2):
        matrix3 = []
        rows1 = 0
        rows2 = 0
        columns1 = 0
        columns2 = 0
        for i in range(len(matrix1)):
            for j in range(len(matrix1[i])):
                columns1 += 1
            rows1 += 1
        columns1 = int(columns1 / rows1)

        for i in range(len(matrix2)):
            for j in range(len(matrix2[i])):
                columns2 += 1
            rows2 += 1
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
        return matrix3


        # здесь вы должны реализовать ещё два метода,
        # которые позволяют делать
        # matrix4 += matrix3
        # matrix4 -= matrix3
        # Как должны называться эти функции -- вопрос к вам!

    def foo1(self, matrix1, matrix):  # change the name!
        raise NotImplementedError


    def foo2(self, other):  # change the name!
        """self -= other."""
        raise NotImplementedError

        # этот метод должны позволять ПОЛУЧАТЬ элемент по индексу,
        # например, print(matrix[1, 2])

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
    stack = MyStack()
    assert(stack.__add__(matric,matric1) == [[10, 12, 14, 16], [18, 20, 22, 24]])
test_add()

def test_foo1():
    stack = MyStack()
    assert(stack.size() == 0)
    stack.push(1)
    assert(stack.size() == 1)
    stack.push(2)
    assert(stack.size() == 2)
    stack.pop()
    assert(stack.size() == 1)
#test_foo1()

def test_foo2():
    stack = MyStack()
    assert (stack.size() == 0)
    stack.push(1)
    assert (stack.size() == 1)
    stack.is_empty()
    stack.pop()
    stack.is_empty()
    assert (stack.is_empty() == True)
#test_foo2()

def test_foo3():
    stack = MyStack()
    stack.push(1)
    assert (stack.top() == 1)
    stack.push(2)
    stack.top()
    assert (stack.top() == 2)
#test_foo3()

def test_foo4():
    stack = MyStack()
    stack.push(1)
    assert (stack.pop() == 1)
    stack.push(7)
    assert (stack.pop() == 7)
#test_foo4()

def test_push():
    stack = MyStack()
    stack.push(1)
    assert (stack.top() == 1)
    stack.push(3)
    assert (stack.pop() == 3)
#test_push()

matric = [[1,2,3,4], [5,6,7,8]]
matric1 = [[9,10,11,12], [13,14,15,16]]
matric3 = []
k = MyStack()
print(k.__add__(matric,matric1))

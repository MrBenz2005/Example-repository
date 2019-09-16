# https://colab.research.google.com/drive/1YR-D8XJ3uLIHzOy6LW8v-QlN6lO8zTwk
class MyStack:
    # следующие два метода класса нужны для того,
    # чтобы можно было делать
    # matrix3 = matrix1 + matrix2, matrix3 = matrix1 - matrix2
    # если матрицы не одного размера, кидайте ошибку MatrixError с разумным сообщением
    def __add__(self, other):
        matrix1 = other

        """
        Return self + other matrix. Do not modify self and other.
        """
        raise NotImplementedError

    def __sub__(self, other):
        """
        Return self - other matrix. Do not modify self and other.
        """
        raise NotImplementedError

        # здесь вы должны реализовать ещё два метода,
        # которые позволяют делать
        # matrix4 += matrix3
        # matrix4 -= matrix3
        # Как должны называться эти функции -- вопрос к вам!

    def foo1(self, other):  # change the name!
        """self += other."""
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

def test_foo1():
    stack = MyStack()
    assert(stack.size() == 0)
    stack.push(1)
    assert(stack.size() == 1)
    stack.push(2)
    assert(stack.size() == 2)
    stack.pop()
    assert(stack.size() == 1)
test_foo1()

def test_foo2():
    stack = MyStack()
    assert (stack.size() == 0)
    stack.push(1)
    assert (stack.size() == 1)
    stack.is_empty()
    stack.pop()
    stack.is_empty()
    assert (stack.is_empty() == True)
test_foo2()

def test_foo3():
    stack = MyStack()
    stack.push(1)
    assert (stack.top() == 1)
    stack.push(2)
    stack.top()
    assert (stack.top() == 2)
test_foo3()

def test_foo4():
    stack = MyStack()
    stack.push(1)
    assert (stack.pop() == 1)
    stack.push(7)
    assert (stack.pop() == 7)
test_foo4()

def test_push():
    stack = MyStack()
    stack.push(1)
    assert (stack.top() == 1)
    stack.push(3)
    assert (stack.pop() == 3)
test_push()

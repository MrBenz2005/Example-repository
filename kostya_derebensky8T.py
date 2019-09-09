# https://colab.research.google.com/drive/1YR-D8XJ3uLIHzOy6LW8v-QlN6lO8zTwk
class MyStack:
    def __init__(self):
        self.__data = []

    def is_empty(self) -> bool:
        mas = self.__data
        if len(mas) == 0:
            return True
        else:
            return False

        """Check if stack is empty."""

    def size(self) -> int:
        return len(self.__data)

    def top(self) -> int:
        return self.__data[-1]

    def pop(self) -> int:
        last_element = self.__data[-1]
        self.__data.pop()
        return last_element

    def push(self, variable: int) -> None:
        self.__data.append(variable)
        return None

    def __repr__(self) -> str:
         a = ''
         for i in range(len(self.__data)):
             a += str(self.__data[i])
             a += ','
         return "MyStack(",a,')'

        # MyStack(1, 2, 3)

klass = MyStack()
print(klass.is_empty())
x = int(input())
print(klass.push(x))
print(klass.push(x+1))
print(klass.push(x+2))
print(klass.top())
print(klass.size())
print(klass.is_empty())
print(klass.pop())
print(klass.__repr__())

def test_size():
    stack = MyStack()
    assert(stack.size() == 0)
    stack.push(1)
    assert(stack.size() == 1)
    stack.push(2)
    assert(stack.size() == 2)
    stack.pop()
    assert(stack.size() == 1)
test_size()

def test_is_empty():
    stack = MyStack()
    assert (stack.size() == 0)
    stack.push(1)
    assert (stack.size() == 1)
    stack.is_empty()
    stack.pop()
    stack.is_empty()
    assert (stack.is_empty() == True)
test_is_empty()

def test_top():
    stack = MyStack()
    stack.push(1)
    assert (stack.top() == 1)
    stack.push(2)
    stack.top()
    assert (stack.top() == 2)
test_top()

def test_pop():
    stack = MyStack()
    stack.push(1)
    assert (stack.pop() == 1)
    stack.push(7)
    assert (stack.pop() == 7)
test_pop()

def test_push():
    stack = MyStack()
    stack.push(1)
    assert (stack.top() == 1)
    stack.push(3)
    assert (stack.pop() == 3)
test_push()

from kostya_derebensky8T1 import MyStack
import pytest
def test_add():
    matric = [[1, 2, 3, 4], [5, 6, 7, 8]]
    matric1 = [[9, 10, 11, 12], [13, 14, 15, 16]]
    stack = MyStack()
    assert(stack.__add__(matric,matric1) == [[10, 12, 14, 16], [18, 20, 22, 24]])
test_add()

def test_sub():
    matric = [[1, 2, 3, 4], [5, 6, 7, 8]]
    matric1 = [[9, 10, 11, 12], [13, 14, 15, 16]]
    stack = MyStack()
    assert(stack.__add__(matric,matric1) == [[10, 12, 14, 16], [18, 20, 22, 24]])
test_add()
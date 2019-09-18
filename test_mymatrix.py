from klass_mymatrix import MyMatrix

def test_add():
    matric = [[1, 2, 3, 4], [5, 6, 7, 8]]
    matric1 = [[9, 10, 11, 12], [13, 14, 15, 16]]
    stack = MyMatrix(matric1)
    matric3 = stack + matric
    assert(matric3 == '10 12 14 16','\n','18 20 22 24')


def test_sub():
    matric = [[1, 2, 3, 4], [5, 6, 7, 8]]
    matric1 = [[9, 10, 11, 12], [13, 14, 15, 16]]
    stack = MyMatrix(matric1)
    matric3 = stack - matric
    assert(matric3 == '0 0 0 0','\n','0 0 0 0')

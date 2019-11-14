from klass_mymatrix import MyMatrix

def test_add():
    matric = [[1, 2, 3, 4], [5, 6, 7, 8]]
    matric1 = [[9, 10, 11, 12], [13, 14, 15, 16]]
    matrix = MyMatrix(matric1)
    matric3 = matrix + matric
    assert(matric3 == '10 12 14 16\n18 20 22 24')
test_add()


def test_sub():
    matric = [[1, 2, 3, 4], [5, 6, 7, 8]]
    matric1 = [[9, 10, 11, 12], [13, 14, 15, 16]]
    matrix = MyMatrix(matric1)
    matric3 = matrix - matric
    assert(matric3 == '8 8 8 8\n8 8 8 8')
test_sub()

def test_iadd():
    matric = [[1, 2, 3, 4], [5, 6, 7, 8]]
    matric1 = [[9, 10, 11, 12], [13, 14, 15, 16]]
    stack = MyMatrix(matric1)
    matric3 = stack + matric
    assert(matric3 == '10 12 14 16\n18 20 22 24')
test_iadd()

def test_isub():
    matric = [[1, 2, 3, 4], [5, 6, 7, 8]]
    matric1 = [[9, 10, 11, 12], [13, 14, 15, 16]]
    stack = MyMatrix(matric1)
    matric3 = stack - matric
    assert(matric3 == '0 0 0 0\n0 0 0 0')
test_isub()


def test_repr():
    mymatrix = MyMatrix([[1, 2], [3, 4]])
    assert (repr(mymatrix) == '1 2 3 4 ')
    mymatrix = MyMatrix([[], []])
    assert (repr(mymatrix) == '')
    mymatrix = MyMatrix([[-1, -2], [-3, -4]])
    assert (repr(mymatrix) == '-1 -2 -3 -4 ')
    mymatrix = MyMatrix([[-1, 556], [989, -4]])
    assert (repr(mymatrix) == '-1 556 989 -4 ')
test_repr()

def test_flip_up_down():
    mymatrix = MyMatrix([[1, 2], [3, 4]])
    mymatrix.flip_up_down()
    assert (repr(mymatrix) == '3 4 1 2')
    assert (mymatrix.size() == (2, 2))
    mymatrix = MyMatrix([[1, 2, 3, 4], [5, 6, 7, 8]])
    mymatrix.flip_up_down()
    assert (repr(mymatrix) == '5 6 7 8 1 2 3 4')
    assert (mymatrix.size() == (2, 4))
    mymatrix = MyMatrix([[0, 2], [3, 0]])
    mymatrix.flip_up_down()
    assert (repr(mymatrix) == '3 0 0 2')
    mymatrix = MyMatrix([[0], [0]])
    mymatrix.flip_up_down()
    assert (repr(mymatrix) == '0 0')
test_flip_up_down()

def test_flip_left_right():
    mymatrix = MyMatrix([[1, 2], [3, 4]])
    mymatrix.flip_left_right()
    assert (repr(mymatrix) == '2 1 4 3')
    assert (mymatrix.size() == (2, 2))
    mymatrix = MyMatrix([[1, 2, 3, 4], [5, 6, 7, 8]])
    mymatrix.flip_left_right()
    assert (repr(mymatrix) == '4 3 2 1 8 7 6 5')
    assert (mymatrix.size() == (2, 4))
    mymatrix = MyMatrix([[0, 2], [3, 0]])
    mymatrix.flip_left_right()
    assert (repr(mymatrix) == '2 0 0 3')
    mymatrix = MyMatrix([[0], [0]])
    mymatrix.flip_left_right()
    assert (repr(mymatrix) == '0 0')
test_flip_left_right()

def test_flipped_up_down():
    mymatrix = MyMatrix([[1, 2], [3, 4]])
    mymatrix.flipped_up_down()
    assert (mymatrix.flipped_up_down() == [[3, 4], [1, 2]])
    mymatrix = MyMatrix([[1, 2, 3, 4], [5, 6, 7, 8]])
    mymatrix.flipped_up_down()
    assert(mymatrix.flipped_up_down() == [[5, 6, 7, 8],[1, 2, 3, 4]])
    mymatrix = MyMatrix([[0, 2], [3, 0]])
    mymatrix.flipped_up_down()
    assert (mymatrix.flipped_up_down() == [[3, 0], [0, 2]])
    mymatrix = MyMatrix([[0], [0]])
    mymatrix.flipped_up_down()
    assert (mymatrix.flipped_up_down() == [[0], [0]])
    mymatrix = MyMatrix([[0], [0]])
    mymatrix.flipped_up_down()
    assert (mymatrix.flipped_up_down() == [[0], [0]])
test_flipped_up_down()

def test_flipped_left_right():
    mymatrix = MyMatrix([[1, 2], [3, 4]])
    mymatrix.flipped_left_right()
    assert (mymatrix.flipped_left_right() == [[2, 1], [4, 3]] )
    mymatrix = MyMatrix([[1, 2, 3, 4], [5, 6, 7, 8]])
    mymatrix.flipped_left_right()
    assert (mymatrix.flipped_left_right() == [[4, 3, 2, 1], [8, 7, 6, 5]])
    mymatrix = MyMatrix([[0, 2], [3, 0]])
    mymatrix.flipped_left_right()
    assert (mymatrix.flipped_left_right() == [[2, 0], [0, 3]])
    mymatrix = MyMatrix([[0], [0]])
    mymatrix.flipped_left_right()
    assert (mymatrix.flipped_left_right() == [[0], [0]])
test_flipped_left_right()

def test_transpose():
    mymatrix = MyMatrix([[1, 2], [3, 4]])
    mymatrix.transpose()
    mymatrix.transposed()
    assert (repr(mymatrix) == '1 3 2 4')
    assert (mymatrix.size() == (2, 2))
    mymatrix = MyMatrix([[1, 2, 3, 4], [5, 6, 7, 8]])
    mymatrix.transpose()
    mymatrix.transposed()
    assert (mymatrix.size() == (4, 2))
    assert (repr(mymatrix) == '1 5 2 6 3 7 4 8')
    mymatrix = MyMatrix([[0, 2], [3, 0]])
    mymatrix.transpose()
    assert (repr(mymatrix) == '0 3 2 0')
    mymatrix = MyMatrix([[0], [0]])
    mymatrix.flip_left_right()
    assert (repr(mymatrix) == '0 0')
test_transpose()

def test_transposed():
    mymatrix = MyMatrix([[1, 2], [3, 4]])
    mymatrix.transposed()
    assert (mymatrix.transposed() == [[1, 3], [2, 4]])
    mymatrix = MyMatrix([[1, 2, 3, 4], [5, 6, 7, 8]])
    mymatrix.transposed()
    assert (mymatrix.transposed() == [[1, 5], [2, 6], [3, 7], [4, 8]])
    mymatrix = MyMatrix([[0, 2], [3, 0]])
    mymatrix.transposed()
    assert (mymatrix.transposed() == [[0, 3], [2, 0]])
    mymatrix = MyMatrix([[0], [0]])
    mymatrix.transposed()
    assert (mymatrix.transposed() == [[0, 0]])
test_transposed()

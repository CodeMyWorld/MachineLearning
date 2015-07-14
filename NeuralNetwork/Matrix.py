__author__ = 'alex'

class Matrix(object):
    column = 0
    row = 0
    matrix = [[]]

    def __init__(self, row, column):
        self.matrix = [[0 for i in range(column)] for i in range(row)]
        self.column = column
        self.row = row

    def get_column(self,column):
        result = []
        for i in range(self.row):
            # column - 1
            result.append(self.matrix[i][column - 1])
        return result

    def get_row(self,row):
        #row - 1
        return self.matrix[row - 1]

    def dot_product(self,input_vector):
        result_vector = []
        for row_index in range(self.row):
            result = 0
            for index in range(len(input_vector)):
             result += self.get_row(row_index + 1)[index] * input_vector[index]
            result_vector.append(result)
        return result_vector

list = [Matrix]
testMatrix = Matrix(3, 3)
testMatrix.matrix[2][0] = 1
testMatrix.matrix[2][1] = 2
list.append(testMatrix)
input_vector = [1, 2, 3]
print testMatrix.matrix
print testMatrix.dot_product(input_vector)



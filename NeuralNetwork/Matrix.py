__author__ = 'alex'

class Matrix(object):
    column = 0
    row = 0
    matrix = [[]]

    def __init__(self, *args):
        if len(args) == 2:
            self.matrix = [[0 for i in range(column)] for i in range(row)]
            self.column = column
            self.row = row
        if len(args) == 1:
            self.matrix = args[0]
            self.column = len(args[0][0])
            self.row = len(args[0])
        else:
            print "I dont know"
    def get_column(self,column):
        result = []
        for i in range(self.row):

            result.append(self.matrix[i][column])
        return result

    def get_row(self,row):
        return self.matrix[row]

    def dot_product(self,input_vector):
        result_vector = []
        for row_index in range(self.row):
            result = 0
            for index in range(len(input_vector)):
             result += self.get_row(row_index)[index] * input_vector[index]
            result_vector.append(result)
        return result_vector





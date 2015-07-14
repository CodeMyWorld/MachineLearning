__author__ = 'alex'

class Matrix(object):
    column = 0
    row = 0
    matrix = [[]]

    def __init__(self, *args):
        if len(args) == 2:
            self.matrix = [[0 for i in range(args[1])] for i in range(args[0])]
            self.column = args[1]
            self.row = args[0]
        elif len(args) == 1:
            self.matrix = args[0]
            self.column = len(args[0][0])
            self.row = len(args[0])
        else:
            print "I dont know"
            print len(args)
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

class DataInstance(object):
    x = 0
    y = 0
    label = 0
    def __init__(self, label, x, y):
        self.x = x
        self.y = y
        self.label = label

class DataBuilder(object):
    count = 0
    dataset = []
    def __init__(self, filePath):
        data = open(filePath)
        for line in data:
            lineList = line.split()
            if lineList[0] == "3":
                lineList[0] = 0
            data_instance = DataInstance(float(lineList[0]), float(lineList[1]), float(lineList[2]))
            self.dataset.append(data_instance)
            self.count += 1


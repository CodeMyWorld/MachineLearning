# encoding: utf-8
__author__ = 'alex'
import math
from Tool import Matrix
from Tool import DataBuilder
from Tool import DataInstance

class NeuralNetwork(object):

    matrix_list = [Matrix]
    #this is a matrix
    activation_value = []
    #this is a matrix
    z_value = []
    #number of layers
    nl = 0
    #error matrix 这是残差 名字搞错了
    error_list = []
    #误差矩阵 每次都要重设为0
    error_matrix_list=[]


    def __init__(self, matrix_list):
        self.matrix_list = matrix_list
        self.nl = len(matrix_list)
        self.error_list = [[] for i in range(self.nl+1)]
        for item in matrix_list:
            error_matrix_instance = Matrix(item.row, item.column)
            self.error_matrix_list.append(error_matrix_instance)

    @classmethod
    def z_function(cls, input_vector, weights):
        # integer? or float?
        result = 0
        for index in range(len(input_vector)):
            result += input_vector[index] * weights[index]
        return result

    @classmethod
    def activation_function(cls, x):
        result = 1 / (1 + math.exp(-1 * x))
        return result

    def derivative_of_activation(self, z):
        result = self.activation_function(z) * (1 - self.activation_function(z))
        return result

    # def nl_error_term(self, weights, input_vector, label):
    #     result = -(label - self.activation_function(self.z_function(input_vector, weights))) * self.derivative_of_activation(self.z_function(input_vector, weights))
    #     return result

    #only one output unit
    def nl_error_term(self,label):
        result = -(label - self.activation_value[self.nl][0]) * self.derivative_of_activation(self.z_value[self.nl][0])
        current_error_list = []
        current_error_list.append(result)
        self.error_list[self.nl] = current_error_list
        return result

    def l_error_term(self, iteration):
        sum_error = 0
        current_error_list = []
        # numbers of column in other word , it means next layer number of unit
        #行数代表后一层有几个神经元 列数代表本层有几个神经元 跟行数没关系！！
        for index in range(self.matrix_list[iteration - 1].column):#有几列
            column_vector = self.matrix_list[iteration - 1].get_column(index)
            sum_error = 0
            #每一列的个数 不懂啊
            for column_index in range(len(column_vector)):
                sum_error += column_vector[column_index] * self.error_list[iteration][column_index]
            error = sum_error * self.derivative_of_activation(self.z_value[iteration-1][index])
            current_error_list.append(error)
        self.error_list[iteration - 1] = current_error_list

    def forward_propagation(self, input_vector):
        self.activation_value.append(input_vector)
        #the z_value is not activation notice
        self.z_value.append(input_vector)
        current_layer_activation = []
        for index in range(len(self.matrix_list)):
            current_matrix = self.matrix_list[index]
            z_vector = current_matrix.dot_product(input_vector)
            self.z_value.append(z_vector)
            current_activation = []
            for index in range(len(z_vector)):
                current_activation.append(self.activation_function(z_vector[index]))
            current_layer_activation.append(current_activation)
            # this is an list (current_activation)
            input_vector = current_activation
            self.activation_value.append(current_activation)
        return current_activation

    def update_weight(self):
        #这个循环是整个神经网络层次循环
        for index in reversed(range(self.nl)):
            #这个循环是误差 每个列的循环 也就是下标i   Wij
            for column_index in range(len(self.error_list[index + 1])):
                #这个循环是激励函数值的循环 也就是下标j
                for row_index in range(len(self.activation_value[index])):
                    #差值 还没有更新
                    self.error_matrix_list[index].matrix[column_index][row_index] \
                        += self.error_list[index + 1][column_index] * self.activation_value[index][row_index]

    def gradient_descent_iteration(self, filePath, interation_number):
        data = DataBuilder(filePath)
        for interation in range(interation_number):
            for data_instance in data.dataset:
                self.forward_propagation([data_instance.x, data_instance.y])
                self.nl_error_term(data_instance.label)
                self.l_error_term(2)
                self.l_error_term(1)
                self.update_weight()
                # print self.activation_value
                #重置 为下一次做准备
                del self.activation_value[:]
                del self.error_list[:]
                self.error_list = [[] for i in range(self.nl+1)]
                del self.z_value[:]
            for index in range(len(self.error_matrix_list)):
                for row_index in range(self.error_matrix_list[index].row):
                    for column_index in range(self.error_matrix_list[index].column):
                        self.matrix_list[index].matrix[row_index][column_index] \
                            -= self.error_matrix_list[index].matrix[row_index][column_index]
                        self.error_matrix_list[index].matrix[row_index][column_index] = 0




matrix_list = []
matrix_list.append(Matrix([[-3.1348981767236928, -4.7288592542851005], [-1.9983016330542622, 3.8320060001852716]]))
matrix_list.append(Matrix([[34.209633358739715, -1.706200089626425]]))
neural_network = NeuralNetwork(matrix_list)

data = DataBuilder("trainset.txt")
for data_instance in data.dataset:
    neural_network.forward_propagation([data_instance.x, data_instance.y])
    print "%d %f" %(data_instance.label, neural_network.activation_value[2][0])
    del neural_network.activation_value[:]
# neural_network.gradient_descent_iteration("trainset.txt",500)
# print neural_network.matrix_list[0].matrix
# print neural_network.matrix_list[1].matrix

# [[0.4865102932949667, 0.5745293509682485], [0.4865132703850679, 0.574532802636167]]
# [[1.516911995270143, 1.516908445822694]]







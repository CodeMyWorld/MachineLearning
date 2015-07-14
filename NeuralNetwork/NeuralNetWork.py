# encoding: utf-8
__author__ = 'alex'
import math
from Matrix import Matrix

class NeuralNetwork(object):

    matrix_list = [Matrix]
    #this is a matrix
    activation_value = []
    #this is a matrix
    z_value = []
    #number of layers
    nl = 0
    #error matrix
    error_list = []


    def __init__(self, matrix_list):
        self.matrix_list = matrix_list
        self.nl = len(matrix_list)
        self.error_list = [[] for i in range(self.nl+1)]

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

    @classmethod
    def l_error_term(cls, pre_error_term, weights, input_vector):
        sum_error = 0
        # haven't been completed
        for index in range(len(weights)):
            sum_error += weights[index] * pre_error_term[index]

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

matrix_list = []
matrix_list.append(Matrix([[1,2],[1,3]]))
matrix_list.append(Matrix([[1,2]]))
neural_network = NeuralNetwork(matrix_list)
result = neural_network.forward_propagation([1,1])
print neural_network.nl_error_term(1)
print neural_network.z_value
neural_network.l_error_term(2)
neural_network.l_error_term(1)
print neural_network.error_list









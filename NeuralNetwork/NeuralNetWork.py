__author__ = 'alex'
import math
from Matrix import Matrix

class NeuralNetwork(object):

    matrix_list = [Matrix]
    activation_value = []

    @classmethod
    def z_function(cls, input_vector, weights):
        # integer? or float?
        result = 0
        for index in range(len(input_vector)):
            result += input_vector[index] * weights[index]
        return result

    @classmethod
    def activation_function(cls, x):
        result = 1 / (1 + math.exp(-x))
        return result

    def derivative_of_activation(self, z):
        result = self.activation_function(z) * (1 - self.activation_function(z))
        return result

    def nl_error_term(self, weights, input_vector, label):
        result = -(label - self.activation_function(self.z_function(input_vector, weights))) * self.derivative_of_activation(self.z_function(input_vector, weights))
        return result

    @classmethod
    def l_error_term(cls, pre_error_term, weights, input_vector):
        sum_error = 0
        # haven't been completed
        for index in range(len(weights)):
            sum_error += weights[index] * pre_error_term[index]

    def forward_propagation(self, input_vector):
        current_layer_activation = []
        for index in range(len(self.matrix_list)):
            current_matrix = self.matrix_list[index]
            current_layer_activation.append(current_matrix.dot_product(input_vector))








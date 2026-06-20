from matrix import Matrix
import random
class Dense:
    def __init__(self, input_size, output_size):
        self.input_size = input_size
        self.output_size = output_size

        self.weights = Matrix.random(input_size, output_size, -1, 1)
        self.bias = Matrix.zeros(1, output_size)

    def forward(self, input_matrix):
        output = input_matrix.dot(self.weights) + self.bias
        return output
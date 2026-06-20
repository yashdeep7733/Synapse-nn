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
    
if __name__ == "__main__":
    layer1 = Dense(3, 4)
    layer2 = Dense(4, 2)

    x = Matrix([[1, 2, 3]])

    print(x.shape)

    out = layer1.forward(x)
    print(out.shape)

    out = out.relu()
    print(out.shape)

    out = layer2.forward(out)
    print(out.shape)
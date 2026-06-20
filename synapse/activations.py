import math

class Activations:

    @staticmethod
    def relu(x):
        return max(0, x)

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + math.exp(-x))

    @staticmethod
    def tanh(x):
        return math.tanh(x)
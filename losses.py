from matrix import Matrix

class Losses:
    @staticmethod
    def mse(predicted, actual):
        if predicted.shape != actual.shape:
            raise ValueError("Predicted and actual matrices must have the same shape.")
        if not isinstance(predicted, Matrix) or not isinstance(actual, Matrix):
            raise TypeError("Predicted and actual must be Matrix instances.")
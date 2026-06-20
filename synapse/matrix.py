from activations import Activations
import random
class Matrix:
    def __init__(self, data):
        if data == []: # Checking if the matrix is empty
            raise ValueError("Matrix cannot be empty.") 
        
        if data[0] == []: # Checks later so incase  data = [] it doesn't throw an index error
            raise ValueError("Matrix cannot have empty rows.") # Checking if the first row is empty

        self.data = data
        self.rows = len(data)
        self.columns = len(data[0])

        length_first_row = len(data[0])
        for row in data:
            if len(row) != length_first_row: # Checking if all rows have the same number of columns
                raise ValueError("All rows must have the same number of columns.")
            
    def __str__(self): # This method defines how the matrix is represented as a string when printed. It converts each row of the matrix to a string and joins them with newlines to create a visual representation of the matrix.
        rows_as_strings = [str(row) for row in self.data] # Converting each row to a string
        return '\n'.join(rows_as_strings) # Making it look like a matrix by joining rows with newlines
    
    def __add__(self, other): # Adds another matrix to this matrix and returns the result as a new Matrix object
        if not isinstance(other, Matrix):
            raise TypeError("Can only add another Matrix.")
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrices must have the same dimensions for addition.")
        
        result_data = []
        for i in range(self.rows):
            current_row = []
            for j in range(self.columns):
                current_row.append(self.data[i][j] + other.data[i][j])
            result_data.append(current_row)
        return Matrix(result_data)
    
    def __sub__(self, other): # Subtracts another matrix from this matrix and returns the result as a new Matrix object
        if not isinstance(other, Matrix):
            raise TypeError("Can only subtract another Matrix.")
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrices must have the same dimensions for subtraction.")
        
        result_data = []
        for i in range(self.rows):
            current_row = []
            for j in range(self.columns):
                current_row.append(self.data[i][j] - other.data[i][j])
            result_data.append(current_row)
        return Matrix(result_data)
    
    def __mul__(self, other): # Multiplies the matrix by a number (scalar multiplication) and returns the result as a new Matrix object
        if not isinstance(other, (int, float)):
            raise TypeError("Can only multiply a matrix by a number.")
        
        result_data = []
        for i in range(self.rows):
            current_row = []
            for j in range(self.columns):
                current_row.append(self.data[i][j] * other)
            result_data.append(current_row)
        return Matrix(result_data)
    
    def __rmul__(self, other): # This method allows for multiplication with the number on the left (e.g., 2 * A). It simply calls the __mul__ method since multiplication is commutative in this case.
        return self.__mul__(other)
    
    def transpose(self): # Transposes the matrix (swaps rows and columns) and returns the result as a new Matrix object
        result_data = []
        for i in range(self.columns):
            current_row = []
            for j in range(self.rows):
                current_row.append(self.data[j][i])
            result_data.append(current_row)
        return Matrix(result_data)
    
    def dot(self, other): # Performs the dot product of this matrix with another matrix and returns the result as a new Matrix object
        if not isinstance(other, Matrix):
            raise TypeError("Can only perform dot product with another Matrix.")
        if self.columns != other.rows:
            raise ValueError("Number of columns in the first matrix must equal the number of rows in the second matrix for dot product.")
        
        result_data = []
        for i in range(self.rows):
            current_row = []
            for j in range(other.columns):
                sum_product = 0
                for k in range(self.columns):
                    sum_product += self.data[i][k] * other.data[k][j]
                current_row.append(sum_product)
            result_data.append(current_row)
        return Matrix(result_data)
    
    @property
    def shape(self): # Returns the shape of the matrix as a tuple (number of rows, number of columns)
        return (self.rows, self.columns)
    
    @staticmethod
    def random(rows, columns, min_value=0, max_value=1): # Creates a matrix of the given size filled with random values between min_value and max_value and returns it as a new Matrix object
        result_data = []
        for i in range(rows):
            current_row = []
            for j in range(columns):
                current_row.append(random.uniform(min_value, max_value))
            result_data.append(current_row)
        return Matrix(result_data)
    
    @staticmethod
    def zeros(rows, columns): # Creates a matrix of the given size filled with zeros and returns it as a new Matrix object
        result_data = []
        for i in range(rows):
            current_row = [0] * columns
            result_data.append(current_row)
        return Matrix(result_data)
    
    @staticmethod
    def ones(rows, columns): # Creates a matrix of the given size filled with ones and returns it as a new Matrix object
        result_data = []
        for i in range(rows):
            current_row = [1] * columns
            result_data.append(current_row)
        return Matrix(result_data)
    
    def apply_function(self, func): # Applies a function to each element of the matrix and returns a new matrix with the results
        result_data = []
        for i in range(self.rows):
            current_row = []
            for j in range(self.columns):
                current_row.append(func(self.data[i][j]))
            result_data.append(current_row)
        return Matrix(result_data)
    
    def relu(self):
        return self.apply_function(Activations.relu) # Applies the ReLU activation function to each element of the matrix and returns a new matrix with the results
    def sigmoid(self):
        return self.apply_function(Activations.sigmoid) # Applies the sigmoid activation function to each element of the matrix and returns a new matrix with the results
    def tanh(self):
        return self.apply_function(Activations.tanh) # Applies the tanh activation function to each element of the matrix and returns a new matrix with the results

if __name__ == "__main__":
    # Example usage
    A = Matrix([
        [1,2],
        [3,4]
        ])

    B = Matrix([
        [5,6],
        [7,8]
        ])
    
    C = A + B
    D = A - B
    
    print(C)
    print(D)
    E = A * 2
    print(E)
    F = 3 * A
    print(F)
    G = A.transpose()
    print(G)
    H = A.dot(B)
    print(H)

    I = Matrix.random(2, 3, 0, 10)
    print(I)
    J = Matrix.zeros(3, 4)
    print(J)
    K = Matrix.ones(2, 5)
    print(K)
    L = A.relu()
    print(L)
    M = A.sigmoid()
    print(M)
    N = A.tanh()
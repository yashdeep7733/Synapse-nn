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
            
    def __str__(self):
        rows_as_strings = [str(row) for row in self.data] # Converting each row to a string
        return '\n'.join(rows_as_strings) # Making it look like a matrix by joining rows with newlines
    
    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrices must have the same dimensions for addition.")
        
        result_data = []
        for i in range(self.rows):
            current_row = []
            for j in range(self.columns):
                current_row.append(self.data[i][j] + other.data[i][j])
            result_data.append(current_row)
        return Matrix(result_data)
    
    def __sub__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrices must have the same dimensions for subtraction.")
        
        result_data = []
        for i in range(self.rows):
            current_row = []
            for j in range(self.columns):
                current_row.append(self.data[i][j] - other.data[i][j])
            result_data.append(current_row)
        return Matrix(result_data)
    
    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Can only multiply a matrix by a number.")
        
        result_data = []
        for i in range(self.rows):
            current_row = []
            for j in range(self.columns):
                current_row.append(self.data[i][j] * other)
            result_data.append(current_row)
        return Matrix(result_data)
    
    def __rmul__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Can only multiply a matrix by a number.")
        
        result_data = []
        for i in range(self.rows):
            current_row = []
            for j in range(self.columns):
                current_row.append(self.data[i][j] * other)
            result_data.append(current_row)
        return Matrix(result_data)

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
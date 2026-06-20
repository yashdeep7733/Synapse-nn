
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

if __name__ == "__main__":
    # Example usage
    matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(matrix)
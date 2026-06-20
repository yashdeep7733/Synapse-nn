from synapse import Matrix, Dense

x = Matrix([[1, 2]])

layer = Dense(2, 4)

output = layer.forward(x).relu()

print(output)
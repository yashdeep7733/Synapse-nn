# Synapse-nn

A pure Python neural network framework built from scratch, featuring a custom matrix engine, dense layers, and activation functions. Synapse is designed as an educational project to explore how modern deep learning systems work under the hood.

## Features

- Custom Matrix implementation
- Dense (Fully Connected) Layers
- ReLU Activation
- Sigmoid Activation
- Tanh Activation
- No external deep learning frameworks

![PyPI](https://img.shields.io/pypi/v/synapse-nn)
[Documentation](https://synapse-nn.netlify.app/)
[PyPI](https://pypi.org/project/synapse-nn/)

## Installation

```bash
pip install synapse-nn
```

## Quick Example

```python
from synapse import Matrix, Dense, ReLU

x = Matrix([[1, 2]])

layer = Dense(2, 4)
activation = ReLU()

output = activation.forward(layer.forward(x))

print(output)
```

## Project Roadmap

### Current
- [x] Matrix Engine
- [x] Dense Layers
- [x] ReLU
- [x] Sigmoid
- [x] Tanh

### Upcoming
- [ ] Loss Functions
- [ ] Backpropagation
- [ ] Optimizers
- [ ] Sequential API
- [ ] XOR Training Example
- [ ] Iris Dataset Training
- [ ] Model Saving & Loading

## Why Synapse?

Neural networks are inspired by biological neurons connected through synapses. This project aims to recreate the core building blocks of modern deep learning frameworks from first principles, providing a deeper understanding of the mathematics and implementation behind AI systems.

## Repository Structure

```text
synapse/
├── matrix.py
├── layers.py
├── activations.py
├── losses.py
├── optimizers.py
└── examples/
```
Methods of Synapse-NN Library

import: <br>
from synapse import Matrix, Dense<br>
Imports main classes from the library.

Matrix:<br>
Matrix([[...]])<br>
Creates a matrix from a 2D list of numbers.

shape:<br>
x.shape<br>
Returns dimensions of matrix as (rows, columns).

add:<br>
A + B<br>
Adds two matrices element-wise (same shape required).

sub:<br>
A - B<br>
Subtracts second matrix from first element-wise.

mul (scalar):<br>
A * n<br>
n * A<br>
Multiplies every element of matrix by a number.

dot:<br>
A.dot(B)<br>
Performs matrix multiplication between two matrices.

transpose:<br>
A.transpose()<br>
Swaps rows and columns of the matrix.

relu:<br>
A.relu()<br>
Applies ReLU activation (sets negative values to 0).

sigmoid:<br>
A.sigmoid()<br>
Applies sigmoid activation (values between 0 and 1).

tanh:<br>
A.tanh()<br>
Applies tanh activation (values between -1 and 1).

random:<br>
Matrix.random(rows, cols, -1, 1)<br>
Creates matrix with random values in given range.

zeros:<br>
Matrix.zeros(rows, cols)<br>
Creates matrix filled with zeros.

ones:<br>
Matrix.ones(rows, cols)<br>
Creates matrix filled with ones.

apply_function:<br>
A.apply_function(func)<br>
Applies a custom function to each element.

Dense:<br>
Dense(input_size, output_size)<br>
Creates a fully connected neural network layer.

forward:<br>
layer.forward(x)<br>
Performs forward pass: x.dot(weights) + bias.

usage:<br>
from synapse import Matrix, Dense

x = Matrix([[1, 2]])

layer = Dense(2, 4)

output = layer.forward(x).relu()

print(output)

example:
```python

from synapse import Matrix, Dense

x = Matrix([[1, 2]])

layer = Dense(2, 4)

output = layer.forward(x).relu()

print(output)
```

## License

MIT License

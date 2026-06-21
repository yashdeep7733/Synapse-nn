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

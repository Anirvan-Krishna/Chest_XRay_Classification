import torch
import numpy as np

# Create a list of NumPy arrays
numpy_arrays = [np.array([1, 2, 3]), np.array([4, 5, 6])]

# Convert the list of NumPy arrays to a Torch tensor
torch_tensor = torch.stack(numpy_arrays)

# Print the Torch tensor
print(torch_tensor)

import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn

# Example training data
# Replace these with your course's X_train and Y_train if already defined
X_train = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
Y_train = np.array([0, 0, 0, 1, 1, 1])

# Convert NumPy arrays into PyTorch tensors
X = torch.tensor(X_train, dtype=torch.float32).reshape(-1, 1)
Y = torch.tensor(Y_train, dtype=torch.float32).reshape(-1, 1)


# 1. Create a logistic neuron
model = nn.Sequential(
    nn.Linear(1, 1),
    nn.Sigmoid()
)

print(model)

# 2. Display model parameters
print("\nModel parameters:")
print(model.state_dict())

# Linear layer has one weight and one bias
linear_layer = model[0]

w = linear_layer.weight.detach().numpy().T
b = linear_layer.bias.detach().numpy()

print("\nInitial weight:", w)
print("Initial bias:", b)
print("Weight shape:", w.shape)
print("Bias shape:", b.shape)

# 3. Set known weight and bias
set_w = np.array([[2.0]], dtype=np.float32)
set_b = np.array([-4.5], dtype=np.float32)

with torch.no_grad():
    linear_layer.weight.copy_(torch.tensor(set_w.T))
    linear_layer.bias.copy_(torch.tensor(set_b))

print("\nUpdated weight and bias:")
print(linear_layer.weight.detach().numpy().T)
print(linear_layer.bias.detach().numpy())

# 4. Predict using the PyTorch model
x_sample = X[0].reshape(1, 1)

with torch.no_grad():
    a1 = model(x_sample)

print("\nPyTorch prediction:", a1.item())

# 5. Calculate the same output using NumPy
def sigmoidnp(z):
    return 1 / (1 + np.exp(-z))

alog = sigmoidnp(np.dot(set_w, X_train[0].reshape(1, 1)) + set_b)

print("NumPy prediction:", alog.item())

# 6. Predict probabilities for all training examples
with torch.no_grad():
    predictions = model(X).numpy().flatten()

print("\nPredicted probabilities:")
print(predictions)

# 7. Plot the logistic neuron output
x_plot = np.linspace(X_train.min() - 1, X_train.max() + 1, 300)
x_tensor = torch.tensor(x_plot, dtype=torch.float32).reshape(-1, 1)

with torch.no_grad():
    y_plot = model(x_tensor).numpy().flatten()

plt.figure(figsize=(8, 5))

# Probability curve
plt.plot(x_plot, y_plot, label="Logistic neuron")

# Shaded probability regions
plt.fill_between(x_plot, y_plot, alpha=0.15)

# Training data
plt.scatter(
    X_train[Y_train == 0],
    Y_train[Y_train == 0],
    label="Class 0"
)

plt.scatter(
    X_train[Y_train == 1],
    Y_train[Y_train == 1],
    label="Class 1"
)

plt.axhline(0.5, linestyle="--", label="Threshold = 0.5")

plt.xlabel("X")
plt.ylabel("Probability")
plt.title("Logistic Neuron Using PyTorch")
plt.ylim(-0.05, 1.05)
plt.legend()
plt.grid(True)
plt.show()


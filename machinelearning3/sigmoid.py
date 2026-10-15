import numpy as np

# Multiple features: 6 samples, 2 features
X = np.array([
    [1, 2],
    [2, 1],
    [3, 2],
    [4, 5],
    [5, 4],
    [6, 5]
])

# Target values
y = np.array([0, 0, 0, 1, 1, 1])

def sigmoid(z):
    return 1 / (1 + np.exp(-z))


# Initialize weights and bias
w = np.zeros(X.shape[1])
b = 0

learning_rate = 0.1
epochs = 1000

n = len(X)

for epoch in range(epochs):

    # Forward pass
    z = X @ w + b
    y_pred = sigmoid(z)

    # Calculate error
    error = y_pred - y

    # Gradients
    dw = (1 / n) * (X.T @ error)
    db = (1 / n) * np.sum(error)

    # Update weights and bias
    w = w - learning_rate * dw
    b = b - learning_rate * db


# Final probabilities
probabilities = sigmoid(X @ w + b)

# Convert probabilities into classes
predictions = (probabilities >= 0.5).astype(int)

print("Weights:", w)
print("Bias:", b)
print("Probabilities:", probabilities)
print("Predictions:", predictions)
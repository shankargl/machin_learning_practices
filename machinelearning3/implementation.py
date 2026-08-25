import numpy as np

X = np.array([1, 2, 3, 4, 5, 6])
y = np.array([0, 0, 0, 1, 1, 1])


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


w = 0
b = 0

learning_rate = 0.1
epochs = 1000

n = len(X)

for epoch in range(epochs):

    # Forward pass
    z = w * X + b
    y_pred = sigmoid(z)

    # Gradients
    dw = (1 / n) * np.sum(X * (y_pred - y))
    db = (1 / n) * np.sum(y_pred - y)

    # Update
    w = w - learning_rate * dw
    b = b - learning_rate * db


# Final probabilities
probabilities = sigmoid(w * X + b)

# Convert probabilities to classes
predictions = (probabilities >= 0.5).astype(int)

print("Weight:", w)
print("Bias:", b)
print("Probabilities:", probabilities)
print("Predictions:", predictions)
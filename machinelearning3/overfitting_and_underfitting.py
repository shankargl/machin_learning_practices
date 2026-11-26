import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Dataset
X = np.array([1, 2, 3, 4, 5, 6, 7]).reshape(-1, 1)
y = np.array([40, 50, 65, 70, 85, 90, 95])

# Create test points for smooth curve plotting
X_test = np.linspace(0, 8, 100).reshape(-1, 1)

def plot_model(degree, title, subplot):
    poly = PolynomialFeatures(degree=degree)
    X_poly = poly.fit_transform(X)
    model = LinearRegression()
    model.fit(X_poly, y)

    # Predictions
    X_test_poly = poly.transform(X_test)
    y_pred = model.predict(X_test_poly)

    # Plot
    plt.subplot(1, 3, subplot)
    plt.scatter(X, y, color="red", label="Data Points")
    plt.plot(X_test, y_pred, color="blue", label=f"Degree {degree} Fit")
    plt.title(title)
    plt.xlabel("Study Hours")
    plt.ylabel("Exam Score")
    plt.legend()

plt.figure(figsize=(15, 4))

# Underfitting: Degree 1 (Linear)
plot_model(degree=1, title="Underfitting (Linear)", subplot=1)

# Good Fit: Degree 2 (Quadratic)
plot_model(degree=2, title="Good Fit (Quadratic)", subplot=2)

# Overfitting: Degree 6 (High Polynomial)
plot_model(degree=6, title="Overfitting (6th Degree)", subplot=3)

plt.tight_layout()
plt.savefig("fitting_examples.png", dpi=300)  # Save as high-quality PNG
plt.close()  # Close the figure to free memory

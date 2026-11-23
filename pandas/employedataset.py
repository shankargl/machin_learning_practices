
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Load Dataset
# -----------------------------
df = pd.read_csv("employee_practice.csv")
print("First 5 rows:\n", df.head())

# -----------------------------
# Step 2: Identify Features & Label
# -----------------------------
features = df.drop("Promotion_Eligibility", axis=1)
label = df["Promotion_Eligibility"]

print("\nFeatures:\n", features.columns)
print("Label:\n", label.name)

# -----------------------------
# Step 3: Handle Missing Values
# -----------------------------
print("\nMissing Values Before:\n", df.isnull().sum())

# Numerical: Fill with median
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Years_Experience"] = df["Years_Experience"].fillna(df["Years_Experience"].median())

# Categorical: Fill with mode
df["Department"] = df["Department"].fillna(df["Department"].mode()[0])
df["Promotion_Eligibility"] = df["Promotion_Eligibility"].fillna(df["Promotion_Eligibility"].mode()[0])

print("\nMissing Values After:\n", df.isnull().sum())

# -----------------------------
# Step 4: Detect & Handle Outliers
# -----------------------------
salary_outliers = df[
    (df["Salary"] < 30000) | (df["Salary"] > 150000)
]

print("\nSalary Outliers:\n", salary_outliers)

# Remove Salary outliers
df = df[
    (df["Salary"] >= 30000) & 
    (df["Salary"] <= 150000)
]

# Remove Years_Experience outliers
df = df[df["Years_Experience"] <= 30]

# -----------------------------
# Step 5: Descriptive Statistics
# -----------------------------
print("\nDescriptive Statistics:\n", df.describe())

print("\nEmployees per Department:\n", df["Department"].value_counts())

plt.figure(figsize=(6,4))
plt.boxplot(df["Salary"])
plt.title("Salary Distribution After Handling Outliers")
plt.ylabel("Salary")
plt.savefig("salary_boxplot.png")
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
np.random.seed(42)
X = np.random.randint(10, 100, 50).reshape(-1, 1)
y = 3 * X.squeeze() + np.random.randn(50) * 20
model = LinearRegression()
model.fit(X, y)
slope = model.coef_[0]
intercept = model.intercept_
r_squared = r2_score(y, model.predict(X))
print(f"Slope (m): {slope:.2f}")
print(f"Intercept (b): {intercept:.2f}")
print(f"R-squared Value: {r_squared:.2f}")
plt.figure(figsize=(8, 6))
sns.scatterplot(x=X.squeeze(), y=y, color='blue', label='Data Points')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Regression Line')
plt.xlabel("Independent Variable (X)")
plt.ylabel("Dependent Variable (y)")
plt.title("Simple Linear Regression: X vs y")
plt.legend()
plt.grid(True)
plt.show()

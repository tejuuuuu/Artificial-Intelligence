import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(42) 
data = {
    'Variable_A': np.random.randint(10, 100, 50), 
    'Variable_B': np.random.randint(5, 50, 50),    
    'Variable_C': np.random.randn(50) * 10 + 50,   
    'Variable_D': np.random.randint(1, 100, 50)   
}
df = pd.DataFrame(data)
plt.figure(figsize=(10, 5))
sns.scatterplot(x=df['Variable_A'], y=df['Variable_B'], color='blue')
plt.title("Scatter Plot: Variable_A vs Variable_B")
plt.xlabel("Variable_A")
plt.ylabel("Variable_B")
plt.grid(True)
plt.show()
correlation_matrix = df.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, fmt=".2f")
plt.title("Heatmap of Correlation Matrix")
plt.show()

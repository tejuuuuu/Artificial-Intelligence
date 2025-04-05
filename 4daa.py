import numpy as np
import matplotlib.pyplot as plt
data = np.random.randn(1000)
fig, axs = plt.subplots(2, 2, figsize=(15, 10))
axs[0, 0].bar(range(len(data)), data, color='blue')
axs[0, 0].set_title('Bar Chart')
axs[0, 1].hist(data, bins=30, color='green')
axs[0, 1].set_title('Histogram')
axs[1, 0].hist(data, bins=30, density=True, color='red', alpha=0.6)
axs[1, 0].set_title('Distplot')
density = np.histogram(data, bins=30, density=True)
x = np.linspace(min(data), max(data), 1000)
kde = np.exp(-0.5 * ((x[:, None] - data) / data.std())**2).sum(axis=1)
kde /= kde.sum()
axs[1, 0].plot(x, kde, color='red')
axs[1, 1].boxplot(data, vert=False, patch_artist=True, boxprops=dict(facecolor='purple'))
axs[1, 1].set_title('Boxplot')
plt.tight_layout()
plt.show()
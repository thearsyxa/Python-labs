import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

x1 = np.random.normal(2, 0.5, 50)
y1 = np.random.normal(2, 0.5, 50)

x2 = np.random.normal(5, 0.5, 50)
y2 = np.random.normal(5, 0.5, 50)

x3 = np.random.normal(8, 0.5, 50)
y3 = np.random.normal(2, 0.5, 50)

plt.figure(figsize=(10, 8))

plt.scatter(x1, y1, color='blue', marker='o', label='Cluster 1', alpha=0.7)
plt.scatter(x2, y2, color='red', marker='s', label='Cluster 2', alpha=0.7)
plt.scatter(x3, y3, color='green', marker='^', label='Cluster 3', alpha=0.7)

plt.title('Scatter Plot with Three Clusters', fontsize=16)
plt.xlabel('X values', fontsize=12)
plt.ylabel('Y values', fontsize=12)
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.6)
plt.xlim(0, 10)
plt.ylim(0, 7)

plt.savefig('scatter_clusters.png', dpi=300, bbox_inches='tight')
plt.show()
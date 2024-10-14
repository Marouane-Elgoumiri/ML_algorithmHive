import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Define our data points
X = np.array([[1, 2], [2, 1], [4, 3], [5, 4], [1, 6], [2, 5], [4, 7], [5, 8]])

# Create a KMeans instance with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)

# Fit the model to our data
kmeans.fit(X)

# Get the cluster centers and labels
centers = kmeans.cluster_centers_
labels = kmeans.labels_

# Plotting
plt.figure(figsize=(10, 8))

# Plot the data points
scatter = plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')

# Plot the cluster centers
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='x', s=200, linewidths=3)

# Add labels for each point
for i, (x, y) in enumerate(X):
    plt.annotate(f'A{i+1}', (x, y), xytext=(5, 5), textcoords='offset points')

plt.title('K-means Clustering Results')
plt.xlabel('X coordinate')
plt.ylabel('Y coordinate')

# Add a color bar
plt.colorbar(scatter)

plt.show()

# Print the cluster assignments
for i, label in enumerate(labels):
    print(f'Point A{i+1} is in cluster {label}')

# Print the final centroids
for i, center in enumerate(centers):
    print(f'Centroid {i} is at position {center}')
# K-means algorithm:
### Understanding the Concept:
<div align="center">
    
![Screenshot from 2024-10-14 11-29-46](https://github.com/user-attachments/assets/380754c7-0458-4a0c-877e-a558a847ba72)

</div>

***Using a manual example:***
<div align="center">

![Screenshot from 2024-10-14 11-43-46](https://github.com/user-attachments/assets/aa64489b-2784-4d85-b716-f848103594bb)

</div>



### Initial data:


We have 8 data points with their (x,y) coordinates:
A1(1,2), A2(2,1), A3(4,3), A4(5,4), A5(1,6), A6(2,5), A7(4,7), A8(5,8)

### Using the K-means algorithm:

```
    # Define our data points
    X = np.array([[1, 2], [2, 1], [4, 3], [5, 4], [1, 6], [2, 5], [4, 7], [5, 8]])
    
    # Create a KMeans instance with 3 clusters
    kmeans = KMeans(n_clusters=3, random_state=42)
    
    # Fit the model to our data
    kmeans.fit(X)
    
    # Get the cluster centers and labels
    centers = kmeans.cluster_centers_
    labels = kmeans.labels_
```
### Plotting the result:

```
# Plotting
plt.figure(figsize=(10, 8))

# Plot the data points
scatter = plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')

# Plot the cluster centers
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='x', s=200, linewidths=3)

plt.title('K-means Clustering Results')
plt.xlabel('X coordinate')
plt.ylabel('Y coordinate')

# Add a color bar
plt.colorbar(scatter)

plt.show()
```


### Result:
<div align="center">

![Screenshot from 2024-10-14 11-15-32](https://github.com/user-attachments/assets/400ecb70-22e4-4db8-b040-253d623b46e6)

</div>

### Important notes:
**The results may vary slightly from our manual calculation because:**

The K-means algorithm in scikit-learn uses a more sophisticated initialization method (k-means++) than our simple random selection.
The algorithm runs for multiple iterations to refine the clusters, whereas we only did one iteration in our manual example.

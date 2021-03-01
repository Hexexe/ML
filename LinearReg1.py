import numpy as np
# input values for three mökkis: size, size of sauna, distance to water, number of indoor bathrooms, 
# proximity of neighbors
X = np.array([[66, 5, 15, 2, 500], 
     [21, 3, 50, 1, 100], 
     [120, 15, 5, 2, 1200]])
c = np.array([3000, 200, -50, 5000, 100])    # coefficient values

def predict(X, c):
    price = "\n".join(str(x) for x in np.dot(X,c))
    print(price)
    
predict(X, c)
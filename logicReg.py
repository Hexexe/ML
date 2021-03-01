import math
import numpy as np

x = np.array([4, 3, 0])
#C1,C2,C3
c = np.array([[-.5, .1, .08],[-.2, .2, .31],[.5, -.1, 2.53]])

def sigmoid(z):
    return 1/(1+math.exp(-z))

# calculate the output of the sigmoid for x with all three coefficients
print([sigmoid(i) for i in c @ x])
import numpy as np
import warnings
# find the gradle decent

# exploring normal equation form : matrix approach
# inv(X'X) * X'*y
def get_min_cost(features,label):
    Xs = np.array(features)
    ys = np.array(label)
    Xs_multiply = np.dot(Xs.T,Xs)
    try:
        inverse = np.linalg.inv(Xs_multiply)
    except np.linalg.LinAlgError:
        warnings("looks like matrix is non-inverable")

    min_cost = np.dot(inverse, np.dot(Xs.T,ys))
    return min_cost



from Algos.RegressionsAlgo import MultiVariateAnalysis
import numpy as np

# compute weight for given height and age data
# x1 = 4, 9, 5
# x2 = 89,124,103
# y = 16,28,20
X1 = [4,9,5]
X2 = [89,124,103]
X0 = [1,1,1]
y = np.array([[16],[28],[20]])
Xs = np.array([X0,X1,X2]).T
#print (Xs)
#print (y)
min_cost = MultiVariateAnalysis.get_min_cost(Xs,y)

print(min_cost)
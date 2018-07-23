import numpy as np
from Algos.RegressionsAlgo import LinearRegresssionAlgo



#demo data x and y coordinates
xs = np.array([1,2,3,4,5,6,7,8,9,10],dtype=np.float64)
ys = np.array([2,3,5,6,1,2,7,8,11,2],dtype=np.float64)

m ,b  = LinearRegresssionAlgo.slop_and_intercept(xs,ys)

print ("slop = " , m , " y-intercept = " , b)


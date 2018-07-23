import numpy as np
from Algos.RegressionsAlgo import LinearRegresssionAlgo
from matplotlib import pyplot


#demo data x and y coordinates
xs = np.array([1,2,3,4,5,6,7,8,9,10],dtype=np.float64)
ys = np.array([2,3,5,6,1,2,7,8,11,2],dtype=np.float64)

m ,b  = LinearRegresssionAlgo.slop_and_intercept(xs,ys)

print ("slop = " , m , " y-intercept = " , b)

regression_line = [b + (m * x) for x in xs]

#graph it to understand it clearly
pyplot.scatter(xs,ys)

#prediction point
prdX = 15 # x =15
prdY = m * prdX + b
pyplot.scatter(prdX,prdY , color="green")
pyplot.plot(xs,regression_line)
pyplot.show()
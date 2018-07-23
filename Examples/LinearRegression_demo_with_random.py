from Algos.RegressionsAlgo import LinearRegresssionAlgo
from matplotlib import pyplot
import random
import numpy as np
#hm : number of data  & variance : limit the random datas between -variance to +variance.
def random_data_sets(hm,variance):
    ys = []
    for i in range(hm):
        y = random.randrange(-variance,variance)
        ys.append(y)
    xs = [i for i in range(0,len(ys))]
    return np.array(xs, dtype=np.float64),np.array(ys,dtype=np.float64)


xs,ys = random_data_sets(40,10)
m,b = LinearRegresssionAlgo.slop_and_intercept(xs,ys)

print("slop = " , m , "intercept = " ,b )
regression_line = [b + (m * x) for x in xs]

#graph it to understand it clearly
pyplot.scatter(xs,ys)
pyplot.plot(xs,regression_line)
pyplot.show()

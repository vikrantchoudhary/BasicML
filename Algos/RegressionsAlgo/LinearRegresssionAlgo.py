from statistics import mean


# compute m and b of y= mx +b
def slop_and_intercept(xs,ys):
    xmean = mean(xs)
    ymean = mean(ys)
    xsqmean = mean(xs * xs)
    mslop = ((xmean * ymean - mean(xs * ys)) /
             (xmean ** 2 - xsqmean))
    b = mean(ys) - mslop * mean(xs)
    return mslop ,b
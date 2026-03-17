import numpy as np

x = [163,765,141,166,137,355,136,1206,433,1130]
y = [186,699,132,272,291,331,199,1890,788,1601]
xk = 386
xavg = np.average(x)
yavg = np.average(y)
n = len(x)

B1 = ((sum(x)*sum(y))-(n*xavg*yavg))/((sum(np.pow(x,2)))-(n*(xavg**2)))

B0 = yavg - B1

rxy = (n*(sum(x)*sum(y))-(sum(x)*sum(y)))/((n*(sum(np.pow(x,2)))-(sum(x)**2))*((n*sum(np.pow(y,2)))-(sum(y)**2)))**(1/2)

r2 = rxy*rxy

Yk = B0+(B1*xk)

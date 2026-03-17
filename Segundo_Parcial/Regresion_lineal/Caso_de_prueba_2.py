#caso prueba 1
import numpy as np

x = [130,650,99,150,128,302,95,945,368,961]
y = [15,69.9,6.5,22.4,28.4,65.9,19.4,198.7,38.8,138.2]
xk = 386
xavg = np.average(x)
yavg = np.average(y)
n = len(x)

B1 = ((sum(x)*sum(y))-(n*xavg*yavg))/((sum(np.pow(x,2)))-(n*(xavg**2)))

B0 = yavg - B1

rxy = (n*(sum(x)*sum(y))-(sum(x)*sum(y)))/((n*(sum(np.pow(x,2)))-(sum(x)**2))*((n*sum(np.pow(y,2)))-(sum(y)**2)))**(1/2)

r2 = rxy*rxy

Yk = B0+(B1*xk)

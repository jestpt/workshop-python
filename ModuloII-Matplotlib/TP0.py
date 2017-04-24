import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 1000)

fig = plt.figure()
ax = plt.axes()
ax.plot(x, np.sin(x));
plt.show()

#Using Pylab
plt.plot(x, np.sin(x));
plt.show()
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,20,1000)
plt.plot(x,np.sin(x),'-r',label="Sine")
plt.plot(x,np.cos(x),'-b',label="Cosine")
plt.plot(x,np.sin(x)+np.cos(x),'-g', label="Sine plus Cosine")
plt.show()
plt.plot(x,5*np.sin(x)-2*np.cos(x),'-y', label="Sine minus Cosine")
plt.legend(loc='upper right')
plt.show()
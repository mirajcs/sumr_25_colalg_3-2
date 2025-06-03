import numpy as np 
import matplotlib.pyplot as plt 

#define intervals 
x1 = np.linspace(-3,-1,300, endpoint=False)
x2 = np.linspace(-1,1, 300, endpoint=True)
x3 = np.linspace(1, 3, 300, endpoint=False)

#define functions
y1 = x1**2
y2 = x2**2
y3 = x3 + 5

#Plot segment 
plt.plot(x1, y1, color='blue')
plt.plot(x2, y2, color='yellow')
plt.plot(x3, y3, color='green')

plt.plot(-3,(-3)**2, 'o', markeredgecolor='blue', markerfacecolor='white')
plt.plot(-1, (-1)**2, 'o', markeredgecolor='blue', markerfacecolor='white')


plt.show()

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1/x

x = np.linspace(-5,5,500)
x = x[x !=0]

y = f(x)

plt.plot(x, y)
plt.title('$f(x)=\\frac{1}{x}$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.ylim(-10,10)
plt.show()
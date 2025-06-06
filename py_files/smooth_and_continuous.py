import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -(x + 3)*(x+2)*(x +1)*x

x = np.linspace(-3.2,0.2,500)

y = f(x)

plt.plot(x, y , label= '$f(x)=2x^4 - 3x ^3 +x^2 - 5x +1$')
plt.title('Quartic Function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.show()
from Equations import *
import numpy as np
from Constants import *
import matplotlib.pyplot as plt

print(Tx(0.1))

x = np.linspace(0.1,la*0.9,100)
y = []
for i in range(len(x)):
    y.append(Tx(x[i]))


plt.plot(x,y)
plt.show()


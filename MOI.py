import numpy as np
import matplotlib.pyplot as plt

h = 17.3
ca = 48.4

straight = np.sqrt((h / 2) ** 2 + (ca - h / 2) ** 2)  # length of straight section

s = (straight + np.pi * h / 4) / 9  # distance between stringers

g = s / (h / 2)
h1 = g
h2 = 2 * g

# stringer op 0 deg - 33 deg - 67 deg
z = [-h / 2, -np.cos(h1) * (h / 2), -np.cos(h2) * (h / 2)]  # stringer positions on curved section
y = [0, np.sin(h1) * (h / 2), np.sin(h2) * (h / 2)]  # stringer positions on curved section

alpha = h / 2 / (ca - h / 2)

rest = 3 * s - np.pi * (h / 4)
z.append(rest * np.cos(alpha))  # stringer positions on straight section
y.append(h / 2 - rest * np.sin(alpha))  # stringer positions on straight section

for i in range(1, 6):
    z.append((rest + i * s) * np.cos(alpha))
    y.append(h / 2 - (rest + i * s) * np.sin(alpha))

plt.scatter(z, y)  # plot upper part

z2 = z
y2 = []
for y_coord in y:
    y2.append(y_coord * -1)

plt.scatter(z2, y2)  # plot under part

rico = (h / 2) / (ca - h / 2)
line = []
graph_straight1 = []
graph_straight2 = []
arange = np.arange(0, ca - h / 2, 0.1)
for zz in arange:
    line.append(zz)
    graph_straight1.append(-rico * zz + h / 2)
    graph_straight2.append(rico * zz - h / 2)

plt.plot(arange, graph_straight1,"b")
plt.plot(arange, graph_straight2,"b")

spar_yy = np.arange(-h / 2, h / 2, 0.1)
spar_xx = np.zeros(len(spar_yy))

c1x = -np.arange(0,h/2+0.01,0.01)
c1y = -np.sqrt((h/2)**2-c1x*c1x)
c2x = -np.arange(0,h/2+0.01,0.01)
c2y = np.sqrt((h/2)**2-c2x*c2x)

plt.plot(spar_xx, spar_yy)

plt.plot(c1x,c1y,"b")
plt.plot(c2x,c2y,"b")
plt.show()





















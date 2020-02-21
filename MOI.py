import numpy as np
import matplotlib.pyplot as plt

h = 17.3 #cm
ca = 48.4 #cm
stringers = 13
hst = 1.4 #cm
wst = 1.8 #cm
tst = 1.2/10 #cm
t = 1.1/10 #cm
tspar= 2.5/10 #cm


# plotting stringers as booms

straight = np.sqrt((h / 2) ** 2 + (ca - h / 2) ** 2)  # length of straight section

s = (2*straight +np.pi*h/2)/stringers # distance between stringers

g = s / (h / 2)
h1 = g




# stringer op
z = [-h / 2, -np.cos(h1) * (h / 2)]  # stringer positions on curved section
y = [0, np.sin(h1) * (h / 2)]  # stringer positions on curved section

alpha = h / 2 / (ca - h / 2)

rest = 2 * s - np.pi * (h / 4)
z.append(rest * np.cos(alpha))  # stringer positions on straight section
y.append(h / 2 - rest * np.sin(alpha))  # stringer positions on straight section

for i in range(1, int((stringers+1)/2-2)):
    z.append((rest + i * s) * np.cos(alpha))
    y.append(h / 2 - (rest + i * s) * np.sin(alpha))
print(np.array(z)+h/2)
print(y)
plt.scatter(z, y, color = 'green')  # plot upper part

z2 = np.array(z)
y2 = []
for y_coord in y:
    y2.append(y_coord * -1)

plt.scatter(z2, y2, color = 'green')  # plot under part

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

plt.plot(spar_xx, spar_yy, 'r')

plt.plot(c1x,c1y,"b")
plt.plot(c2x,c2y,"b")
plt.show()

# moment of inertia
A_stringer = tst*hst + wst*tst

y_cen = (-(2*(h/2)/(np.pi))*np.pi*(h/2)*t + 2*straight*t*(ca-h/2)/2+sum(A_stringer*np.array(z[1:]))*2+A_stringer*z[0])\
        /(np.pi*(h/2)*t+2*straight*t+tspar*h+stringers*A_stringer)
print(y_cen)

Izz_stringer = 1/12*tst*hst**3
Iyy_stringer= 1/12*tst*wst**3

Izz_spar =  1/12*tspar*h**3

d2_y = np.square(y)
d2_z = np.square(z[1:]-y_cen)

Steiner_z= 2*A_stringer*(sum(d2_y))
Steiner_y = A_stringer*(h/2+ y_cen)**2 + 2*A_stringer*(sum(d2_z))

Izz_circle = (np.pi * (h/2)**3 * t)/2
Iyy_circle = (h/2)**3*t*(np.pi/2-4/np.pi)

Izz_straight = (t*straight/12)*(straight**2 * (np.sin(alpha))**2)*2
Iyy_straight = (t*straight/12)*(straight**2 * (np.cos(alpha))**2)*2

Steiner_circle_y = (2*(h/2)/(np.pi)+y_cen)**2 * (np.pi*(h/2)*t)
Steiner_spar = tspar*h*(y_cen)**2
Steiner_straight_z = 2*(straight*t)*(h/4)**2
Steiner_straight_y = 2*(straight*t)*((ca-h/2)/2-y_cen)**2

Izz_total = Izz_circle + Izz_straight + Steiner_z + Steiner_straight_z + Izz_spar #+ Izz_stringer*stringers
Iyy_total = Iyy_circle +Iyy_straight + Steiner_y  + Steiner_circle_y + Steiner_straight_y+Steiner_spar #+ Iyy_stringer*stringers

print(Izz_total, Iyy_total)

#enclosed area
Am_cell1 = (np.pi*(h/2)**2)/2
Am_cell2 = (h*(ca-h/2))/2

print(Am_cell1, Am_cell2)






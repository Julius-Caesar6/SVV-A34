from MOI import Izz_total, Am_cell1 , Am_cell2, A_stringer, y, z , h, straight, t , tspar, ca
import numpy as np
import matplotlib.pyplot as plt

#qb1 -------------------------------------------------------------------------------------------------------------------
input1 = np.linspace(0,np.pi/2,100) #list of range of integral
output1 = np.cos(input1) #list of outputs
zvalues1 = np.linspace(-h/2,0,100)

line1 = []
for i in output1:
    qb1_line = -1/Izz_total * ((t*h**2/4)*(-i +1) + A_stringer*y[1] + A_stringer*y[2])
    line1.append(qb1_line)
#value1 = 1                   #integral (sin(theta).dtheta) from 0 to pi/2
qb1 = -1/Izz_total*(t*h**2/4*(-output1[-1] + 1 ) + A_stringer*y[1] + A_stringer*y[2])
line1plot = [q*1 for q in line1]

plt.plot(zvalues1,line1plot)


#qb2 -------------------------------------------------------------------------------------------------------------------
input2 = np.linspace(0,h/2,100)
output2 = (input2**2)/2
yvalues2 = np.linspace(0,h/2,100)

line2 = []
for j in output2:
    qb2_line = -1/Izz_total *tspar * j
    line2.append(qb2_line)

#value2 = 37.41125                   #integral (y.dy) from 0 to h/2
qb2 = -1/Izz_total *t*output2[-1]
line2plot = [r*1 for r in line2]
plt.plot(line2plot,yvalues2)

#qb3 -------------------------------------------------------------------------------------------------------------------
input3 = np.linspace(0,straight,100)
output3 = (input3**2)/2
zvalues3 = np.linspace(0,ca-h/2,100)
line3 = []
for k in output3:
    qb3_line = qb1 + qb2 - 1/Izz_total*t*(h/2 - (h/2)/straight *k + A_stringer*sum(y[3:]))
    line3.append(qb3_line)

#value3 =    827.44                #integral (y,dy) from 0 to straight
qb3 = qb1 + qb2 - 1/Izz_total*t*(h/2 - (h/2)/straight*output3[-1]+ A_stringer*sum(y[3:]))
line3plot = [b*1 for b in line3]

plt.plot(zvalues3,line3plot)

#qb4 -------------------------------------------------------------------------------------------------------------------
input4 = np.linspace(0,straight,100)
output4 = (input4**2)/2
zvalues4 = np.linspace(ca-h/2 , 0, 100)
line4 = []
for l in output4:
    qb4_line = qb3 - 1/Izz_total*t *  ( ((-h/2)/straight)*l - A_stringer*sum(y[3:]))
    line4.append(qb4_line)

#value4 =  827.44                  #integral (y*dy) from 0 to straight
qb4 = qb3 - 1/Izz_total*t *  ( ((-h/2)/straight)*output4[-1] - A_stringer*sum(y[3:]))
line4plot = [p*1 for p in line4]

plt.plot(zvalues4, line4plot)

#qb5 -------------------------------------------------------------------------------------------------------------------
input5 = np.linspace(-h/2,0,100)
output5 = (input5**2)/2
yvalues5 = np.linspace(-h/2,0,100)
line5 = []
for w in output5:
    qb5_line = qb4 - 1/Izz_total*tspar *w
    line5.append(qb5_line)

#value5 =     -37.41125                       #integral (y*dy) from -h/2 to 0
qb5 = qb4 - 1/Izz_total*tspar*(0-output5[-1])
line5plot = [a*1 for a in line5]

plt.plot(line5plot,yvalues5)
#qb6 -------------------------------------------------------------------------------------------------------------------
input6 = np.linspace(-np.pi/2,0,100)
output6 = np.cos(input6)
zvalues6 = np.linspace(0, -h/2, 100)
line6 = []

for e in output6:
    qb6_line =qb4 - qb5 - (1/Izz_total)*t*h**2/4 *(-e+1) - A_stringer*y[1]-A_stringer*y[2]
    line6.append(qb6_line)

#value6 =      1               #integral (cos(theta)*dtheta) from -pi/2 to 0
qb6 = qb4 - qb5 - (1/Izz_total)*t*h**2/4 *(-output6[-1] +1 ) - A_stringer*y[1]-A_stringer*y[2]
line6plot = [m*1 for m in line6]

plt.plot(zvalues6,line6plot)
#-----------------------------------------------------------------------------------------------------------------------






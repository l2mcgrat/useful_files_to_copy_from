import matplotlib.pyplot as plt
from sys import argv
import numpy as np
from numpy import zeros,sqrt,mean, sin, pi
import matplotlib.patches as mpatches

values1 = argv[1]
values2 = argv[2]
values3 = argv[3]
numberofbins = int(argv[4])
numberofsteps = int(values1[values1.find("N")+1:values1.find("S")])
numberofbeads = int(values1[values1.find("P")+1:values1.find("F")])
filesize = numberofsteps*numberofbeads
bins1 = zeros( numberofbins , float )
bins2 = zeros( numberofbins , float )
bins3 = zeros( numberofbins , float )

values1 = open(values1, "r")
values2 = open(values2, "r")
values3 = open(values3, "r")

odds = 0.0

for i in range(filesize):
    value1 = float(values1.readline())
    value2 = float(values2.readline())
    value3 = float(values3.readline())
    for j in range(numberofbins):

        if (value1 >= (180.0*j/(numberofbins-1))) and (value1 < ((180.0*(j+1)/(numberofbins-1)))) and (value1 > 0.000001):
            bins1[j] += 1.0/(sin(pi*value1/180.0)*filesize)

        if (value1 < 0.000001):
            bins1[0] += 1.0/filesize
            odds += 1.0/(3.0*filesize)

        if (value2 >= (180.0*j/(numberofbins-1))) and (value2 < ((180.0*(j+1)/(numberofbins-1)))) and (value2 > 0.000001):
            bins2[j] += 1.0/(sin(pi*value2/180.0)*filesize)

        if (value2 < 0.000001):
            bins2[0] += 1.0/filesize
            odds += 1.0/(3.0*filesize)

        if (value3 >= (180.0*j/(numberofbins-1))) and (value3 < ((180.0*(j+1)/(numberofbins-1)))) and (value3 > 0.000001):
            bins3[j] += 1.0/(sin(pi*value3/180.0)*filesize)

        if (value3 < 0.000001):
            bins3[0] += 1.0/filesize
            odds += 1.0/(3.0*filesize)

values1.close()
values2.close()
values3.close()

print odds

theta1 = zeros( numberofbins , float )
theta2 = zeros( numberofbins , float )
theta3 = zeros( numberofbins , float )

for i in range(numberofbins):
    theta1[i] = (180.0*i)/(numberofbins-1)
    theta2[i] = (180.0*i)/(numberofbins-1)
    theta3[i] = (180.0*i)/(numberofbins-1)

plt.plot(theta1, bins1, 'b-')
plt.plot(theta2, bins2, 'r-')
plt.plot(theta3, bins3, 'g-')
plt.xlabel('theta')
plt.ylabel('frequency')
plt.title('Angle Distribution')

blue_patch = mpatches.Patch(color='blue', label='15 K')
red_patch = mpatches.Patch(color='red', label='95 K')
green_patch = mpatches.Patch(color='green', label='293 K')

plt.legend(handles=[blue_patch, red_patch, green_patch])
plt.show()


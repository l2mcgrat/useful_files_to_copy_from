import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from sys import argv
import numpy as np
from numpy import zeros,sqrt,mean

# start with lowest temperature, 15.0 K

file1 = np.loadtxt(argv[1])  # imports necessary values, they are unsorted so we must sort them, but first we will put them in arrays

radii1 = zeros( len(file1[:,0]) , float )
rotationalenergyvalues1 = zeros( len(file1[:,0]) , float )
rotationalenergyerrorvalues1 = zeros( len(file1[:,0]) , float )
potentialenergyvalues1 = zeros( len(file1[:,0]) , float )
potentialenergyerrorvalues1 = zeros( len(file1[:,0]) , float )

for i in range(len(file1[:,0])):
    radii1[i] = file1[i,0]*10.0
    rotationalenergyvalues1[i] = file1[i,1]
    rotationalenergyerrorvalues1[i] = file1[i,2]
    potentialenergyvalues1[i] = file1[i,3]
    potentialenergyerrorvalues1[i] = file1[i,4]

# sorting algorithm for file1

length = len(file1[:,0]) + 1
startsortindex = -1
swapindex = 0

for i in range(len(file1[:,0])-1):
    length -= 1
    startsortindex += 1
    minimumvalue = radii1[startsortindex]
    for j in range(length):
        if radii1[j + startsortindex] <= minimumvalue:
            swapindex = j + startsortindex
            minimumvalue = radii1[j + startsortindex]

    tempval = radii1[startsortindex]
    radii1[startsortindex] = radii1[swapindex]
    radii1[swapindex] = tempval
    tempval = rotationalenergyvalues1[startsortindex]
    rotationalenergyvalues1[startsortindex] = rotationalenergyvalues1[swapindex]
    rotationalenergyvalues1[swapindex] = tempval
    tempval = rotationalenergyerrorvalues1[startsortindex]
    rotationalenergyerrorvalues1[startsortindex] = rotationalenergyerrorvalues1[swapindex]
    rotationalenergyerrorvalues1[swapindex] = tempval
    tempval = potentialenergyvalues1[startsortindex]
    potentialenergyvalues1[startsortindex] = potentialenergyvalues1[swapindex]
    potentialenergyvalues1[swapindex] = tempval
    tempval = potentialenergyerrorvalues1[startsortindex]
    potentialenergyerrorvalues1[startsortindex] = potentialenergyerrorvalues1[swapindex]
    potentialenergyerrorvalues1[swapindex] = tempval

# next do temperature, 70.0 K

file2 = np.loadtxt(argv[2])

radii2 = zeros( len(file2[:,0]) , float )
rotationalenergyvalues2 = zeros( len(file2[:,0]) , float )
rotationalenergyerrorvalues2 = zeros( len(file2[:,0]) , float )
potentialenergyvalues2 = zeros( len(file2[:,0]) , float )
potentialenergyerrorvalues2 = zeros( len(file2[:,0]) , float )

for i in range(len(file2[:,0])):
    radii2[i] = file2[i,0]*10.0
    rotationalenergyvalues2[i] = file2[i,1]
    rotationalenergyerrorvalues2[i] = file2[i,2]
    potentialenergyvalues2[i] = file2[i,3]
    potentialenergyerrorvalues2[i] = file2[i,4]

# sorting algorithm for file2

length = len(file2[:,0]) + 1
startsortindex = -1
swapindex = 0

for i in range(len(file2[:,0])-1):
    length -= 1
    startsortindex += 1
    minimumvalue = radii2[startsortindex]
    for j in range(length):
        if radii2[j + startsortindex] <= minimumvalue:
            swapindex = j + startsortindex
            minimumvalue = radii2[j + startsortindex]

    tempval = radii2[startsortindex]
    radii2[startsortindex] = radii2[swapindex]
    radii2[swapindex] = tempval
    tempval = rotationalenergyvalues2[startsortindex]
    rotationalenergyvalues2[startsortindex] = rotationalenergyvalues2[swapindex]
    rotationalenergyvalues2[swapindex] = tempval
    tempval = rotationalenergyerrorvalues2[startsortindex]
    rotationalenergyerrorvalues2[startsortindex] = rotationalenergyerrorvalues2[swapindex]
    rotationalenergyerrorvalues2[swapindex] = tempval
    tempval = potentialenergyvalues2[startsortindex]
    potentialenergyvalues2[startsortindex] = potentialenergyvalues2[swapindex]
    potentialenergyvalues2[swapindex] = tempval
    tempval = potentialenergyerrorvalues2[startsortindex]
    potentialenergyerrorvalues2[startsortindex] = potentialenergyerrorvalues2[swapindex]
    potentialenergyerrorvalues2[swapindex] = tempval

# next do temperature, 95.0 K

file3 = np.loadtxt(argv[3])

radii3 = zeros( len(file3[:,0]) , float )
rotationalenergyvalues3 = zeros( len(file3[:,0]) , float )
rotationalenergyerrorvalues3 = zeros( len(file3[:,0]) , float )
potentialenergyvalues3 = zeros( len(file3[:,0]) , float )
potentialenergyerrorvalues3 = zeros( len(file3[:,0]) , float )

for i in range(len(file3[:,0])):
    radii3[i] = file3[i,0]*10.0
    rotationalenergyvalues3[i] = file3[i,1]
    rotationalenergyerrorvalues3[i] = file3[i,2]
    potentialenergyvalues3[i] = file3[i,3]
    potentialenergyerrorvalues3[i] = file3[i,4]

# sorting algorithm for file3

length = len(file3[:,0]) + 1
startsortindex = -1
swapindex = 0

for i in range(len(file3[:,0])-1):
    length -= 1
    startsortindex += 1
    minimumvalue = radii3[startsortindex]
    for j in range(length):
        if radii3[j + startsortindex] <= minimumvalue:
            swapindex = j + startsortindex
            minimumvalue = radii3[j + startsortindex]

    tempval = radii3[startsortindex]
    radii3[startsortindex] = radii3[swapindex]
    radii3[swapindex] = tempval
    tempval = rotationalenergyvalues3[startsortindex]
    rotationalenergyvalues3[startsortindex] = rotationalenergyvalues3[swapindex]
    rotationalenergyvalues3[swapindex] = tempval
    tempval = rotationalenergyerrorvalues3[startsortindex]
    rotationalenergyerrorvalues3[startsortindex] = rotationalenergyerrorvalues3[swapindex]
    rotationalenergyerrorvalues3[swapindex] = tempval
    tempval = potentialenergyvalues3[startsortindex]
    potentialenergyvalues3[startsortindex] = potentialenergyvalues3[swapindex]
    potentialenergyvalues3[swapindex] = tempval
    tempval = potentialenergyerrorvalues3[startsortindex]
    potentialenergyerrorvalues3[startsortindex] = potentialenergyerrorvalues3[swapindex]
    potentialenergyerrorvalues3[swapindex] = tempval

# next do temperature, 140.0 K

file4 = np.loadtxt(argv[4])

radii4 = zeros( len(file4[:,0]) , float )
rotationalenergyvalues4 = zeros( len(file4[:,0]) , float )
rotationalenergyerrorvalues4 = zeros( len(file4[:,0]) , float )
potentialenergyvalues4 = zeros( len(file4[:,0]) , float )
potentialenergyerrorvalues4 = zeros( len(file4[:,0]) , float )

for i in range(len(file4[:,0])):
    radii4[i] = file4[i,0]*10.0
    rotationalenergyvalues4[i] = file4[i,1]
    rotationalenergyerrorvalues4[i] = file4[i,2]
    potentialenergyvalues4[i] = file4[i,3]
    potentialenergyerrorvalues4[i] = file4[i,4]

# sorting algorithm for file4

length = len(file4[:,0]) + 1
startsortindex = -1
swapindex = 0

for i in range(len(file4[:,0])-1):
    length -= 1
    startsortindex += 1
    minimumvalue = radii4[startsortindex]
    for j in range(length):
        if radii4[j + startsortindex] <= minimumvalue:
            swapindex = j + startsortindex
            minimumvalue = radii4[j + startsortindex]

    tempval = radii4[startsortindex]
    radii4[startsortindex] = radii4[swapindex]
    radii4[swapindex] = tempval
    tempval = rotationalenergyvalues4[startsortindex]
    rotationalenergyvalues4[startsortindex] = rotationalenergyvalues4[swapindex]
    rotationalenergyvalues4[swapindex] = tempval
    tempval = rotationalenergyerrorvalues4[startsortindex]
    rotationalenergyerrorvalues4[startsortindex] = rotationalenergyerrorvalues4[swapindex]
    rotationalenergyerrorvalues4[swapindex] = tempval
    tempval = potentialenergyvalues4[startsortindex]
    potentialenergyvalues4[startsortindex] = potentialenergyvalues4[swapindex]
    potentialenergyvalues4[swapindex] = tempval
    tempval = potentialenergyerrorvalues4[startsortindex]
    potentialenergyerrorvalues4[startsortindex] = potentialenergyerrorvalues4[swapindex]
    potentialenergyerrorvalues4[swapindex] = tempval

# temperature; 145.0 K

file5 = np.loadtxt(argv[5])  # imports necessary values, they are unsorted so we must sort them, but first we will put them in arrays

radii5 = zeros( len(file5[:,0]) , float )
rotationalenergyvalues5 = zeros( len(file5[:,0]) , float )
rotationalenergyerrorvalues5 = zeros( len(file5[:,0]) , float )
potentialenergyvalues5 = zeros( len(file5[:,0]) , float )
potentialenergyerrorvalues5 = zeros( len(file5[:,0]) , float )

for i in range(len(file5[:,0])):
    radii5[i] = file5[i,0]*10.0
    rotationalenergyvalues5[i] = file5[i,1]
    rotationalenergyerrorvalues5[i] = file5[i,2]
    potentialenergyvalues5[i] = file5[i,3]
    potentialenergyerrorvalues5[i] = file5[i,4]

# sorting algorithm for file5

length = len(file5[:,0]) + 1
startsortindex = -1
swapindex = 0

for i in range(len(file5[:,0])-1):
    length -= 1
    startsortindex += 1
    minimumvalue = radii5[startsortindex]
    for j in range(length):
        if radii5[j + startsortindex] <= minimumvalue:
            swapindex = j + startsortindex
            minimumvalue = radii5[j + startsortindex]

    tempval = radii5[startsortindex]
    radii5[startsortindex] = radii5[swapindex]
    radii5[swapindex] = tempval
    tempval = rotationalenergyvalues5[startsortindex]
    rotationalenergyvalues5[startsortindex] = rotationalenergyvalues5[swapindex]
    rotationalenergyvalues5[swapindex] = tempval
    tempval = rotationalenergyerrorvalues5[startsortindex]
    rotationalenergyerrorvalues5[startsortindex] = rotationalenergyerrorvalues5[swapindex]
    rotationalenergyerrorvalues5[swapindex] = tempval
    tempval = potentialenergyvalues5[startsortindex]
    potentialenergyvalues5[startsortindex] = potentialenergyvalues5[swapindex]
    potentialenergyvalues5[swapindex] = tempval
    tempval = potentialenergyerrorvalues5[startsortindex]
    potentialenergyerrorvalues5[startsortindex] = potentialenergyerrorvalues5[swapindex]
    potentialenergyerrorvalues5[swapindex] = tempval

# next do temperature, 150.0 K

file6 = np.loadtxt(argv[6])

radii6 = zeros( len(file6[:,0]) , float )
rotationalenergyvalues6 = zeros( len(file6[:,0]) , float )
rotationalenergyerrorvalues6 = zeros( len(file6[:,0]) , float )
potentialenergyvalues6 = zeros( len(file6[:,0]) , float )
potentialenergyerrorvalues6 = zeros( len(file6[:,0]) , float )

for i in range(len(file6[:,0])):
    radii6[i] = file6[i,0]*10.0
    rotationalenergyvalues6[i] = file6[i,1]
    rotationalenergyerrorvalues6[i] = file6[i,2]
    potentialenergyvalues6[i] = file6[i,3]
    potentialenergyerrorvalues6[i] = file6[i,4]

# sorting algorithm for file6

length = len(file6[:,0]) + 1
startsortindex = -1
swapindex = 0

for i in range(len(file6[:,0])-1):
    length -= 1
    startsortindex += 1
    minimumvalue = radii6[startsortindex]
    for j in range(length):
        if radii6[j + startsortindex] <= minimumvalue:
            swapindex = j + startsortindex
            minimumvalue = radii6[j + startsortindex]

    tempval = radii6[startsortindex]
    radii6[startsortindex] = radii6[swapindex]
    radii6[swapindex] = tempval
    tempval = rotationalenergyvalues6[startsortindex]
    rotationalenergyvalues6[startsortindex] = rotationalenergyvalues6[swapindex]
    rotationalenergyvalues6[swapindex] = tempval
    tempval = rotationalenergyerrorvalues6[startsortindex]
    rotationalenergyerrorvalues6[startsortindex] = rotationalenergyerrorvalues6[swapindex]
    rotationalenergyerrorvalues6[swapindex] = tempval
    tempval = potentialenergyvalues6[startsortindex]
    potentialenergyvalues6[startsortindex] = potentialenergyvalues6[swapindex]
    potentialenergyvalues6[swapindex] = tempval
    tempval = potentialenergyerrorvalues6[startsortindex]
    potentialenergyerrorvalues6[startsortindex] = potentialenergyerrorvalues6[swapindex]
    potentialenergyerrorvalues6[swapindex] = tempval

# next do temperature, 155.0 K

file7 = np.loadtxt(argv[7])

radii7 = zeros( len(file7[:,0]) , float )
rotationalenergyvalues7 = zeros( len(file7[:,0]) , float )
rotationalenergyerrorvalues7 = zeros( len(file7[:,0]) , float )
potentialenergyvalues7 = zeros( len(file7[:,0]) , float )
potentialenergyerrorvalues7 = zeros( len(file7[:,0]) , float )

for i in range(len(file7[:,0])):
    radii7[i] = file7[i,0]*10.0
    rotationalenergyvalues7[i] = file7[i,1]
    rotationalenergyerrorvalues7[i] = file7[i,2]
    potentialenergyvalues7[i] = file7[i,3]
    potentialenergyerrorvalues7[i] = file7[i,4]

# sorting algorithm for file7

length = len(file7[:,0]) + 1
startsortindex = -1
swapindex = 0

for i in range(len(file7[:,0])-1):
    length -= 1
    startsortindex += 1
    minimumvalue = radii7[startsortindex]
    for j in range(length):
        if radii7[j + startsortindex] <= minimumvalue:
            swapindex = j + startsortindex
            minimumvalue = radii7[j + startsortindex]

    tempval = radii7[startsortindex]
    radii7[startsortindex] = radii7[swapindex]
    radii7[swapindex] = tempval
    tempval = rotationalenergyvalues7[startsortindex]
    rotationalenergyvalues7[startsortindex] = rotationalenergyvalues7[swapindex]
    rotationalenergyvalues7[swapindex] = tempval
    tempval = rotationalenergyerrorvalues7[startsortindex]
    rotationalenergyerrorvalues7[startsortindex] = rotationalenergyerrorvalues7[swapindex]
    rotationalenergyerrorvalues7[swapindex] = tempval
    tempval = potentialenergyvalues7[startsortindex]
    potentialenergyvalues7[startsortindex] = potentialenergyvalues7[swapindex]
    potentialenergyvalues7[swapindex] = tempval
    tempval = potentialenergyerrorvalues7[startsortindex]
    potentialenergyerrorvalues7[startsortindex] = potentialenergyerrorvalues7[swapindex]
    potentialenergyerrorvalues7[swapindex] = tempval

# next do temperature, 160.0 K

file8 = np.loadtxt(argv[8])

radii8 = zeros( len(file8[:,0]) , float )
rotationalenergyvalues8 = zeros( len(file8[:,0]) , float )
rotationalenergyerrorvalues8 = zeros( len(file8[:,0]) , float )
potentialenergyvalues8 = zeros( len(file8[:,0]) , float )
potentialenergyerrorvalues8 = zeros( len(file8[:,0]) , float )

for i in range(len(file8[:,0])):
    radii8[i] = file8[i,0]*10.0
    rotationalenergyvalues8[i] = file8[i,1]
    rotationalenergyerrorvalues8[i] = file8[i,2]
    potentialenergyvalues8[i] = file8[i,3]
    potentialenergyerrorvalues8[i] = file8[i,4]

# sorting algorithm for file8

length = len(file8[:,0]) + 1
startsortindex = -1
swapindex = 0

for i in range(len(file8[:,0])-1):
    length -= 1
    startsortindex += 1
    minimumvalue = radii8[startsortindex]
    for j in range(length):
        if radii8[j + startsortindex] <= minimumvalue:
            swapindex = j + startsortindex
            minimumvalue = radii8[j + startsortindex]

    tempval = radii8[startsortindex]
    radii8[startsortindex] = radii8[swapindex]
    radii8[swapindex] = tempval
    tempval = rotationalenergyvalues8[startsortindex]
    rotationalenergyvalues8[startsortindex] = rotationalenergyvalues8[swapindex]
    rotationalenergyvalues8[swapindex] = tempval
    tempval = rotationalenergyerrorvalues8[startsortindex]
    rotationalenergyerrorvalues8[startsortindex] = rotationalenergyerrorvalues8[swapindex]
    rotationalenergyerrorvalues8[swapindex] = tempval
    tempval = potentialenergyvalues8[startsortindex]
    potentialenergyvalues8[startsortindex] = potentialenergyvalues8[swapindex]
    potentialenergyvalues8[swapindex] = tempval
    tempval = potentialenergyerrorvalues8[startsortindex]
    potentialenergyerrorvalues8[startsortindex] = potentialenergyerrorvalues8[swapindex]
    potentialenergyerrorvalues8[swapindex] = tempval

# next do temperature, 293.0 K

file9 = np.loadtxt(argv[9])

radii9 = zeros( len(file9[:,0]) , float )
rotationalenergyvalues9 = zeros( len(file9[:,0]) , float )
rotationalenergyerrorvalues9 = zeros( len(file9[:,0]) , float )
potentialenergyvalues9 = zeros( len(file9[:,0]) , float )
potentialenergyerrorvalues9 = zeros( len(file9[:,0]) , float )

for i in range(len(file9[:,0])):
    radii9[i] = file9[i,0]*10.0
    rotationalenergyvalues9[i] = file9[i,1]
    rotationalenergyerrorvalues9[i] = file9[i,2]
    potentialenergyvalues9[i] = file9[i,3]
    potentialenergyerrorvalues9[i] = file9[i,4]

# sorting algorithm for file9

length = len(file9[:,0]) + 1
startsortindex = -1
swapindex = 0

for i in range(len(file9[:,0])-1):
    length -= 1
    startsortindex += 1
    minimumvalue = radii9[startsortindex]
    for j in range(length):
        if radii9[j + startsortindex] <= minimumvalue:
            swapindex = j + startsortindex
            minimumvalue = radii9[j + startsortindex]

    tempval = radii9[startsortindex]
    radii9[startsortindex] = radii9[swapindex]
    radii9[swapindex] = tempval
    tempval = rotationalenergyvalues9[startsortindex]
    rotationalenergyvalues9[startsortindex] = rotationalenergyvalues9[swapindex]
    rotationalenergyvalues9[swapindex] = tempval
    tempval = rotationalenergyerrorvalues9[startsortindex]
    rotationalenergyerrorvalues9[startsortindex] = rotationalenergyerrorvalues9[swapindex]
    rotationalenergyerrorvalues9[swapindex] = tempval
    tempval = potentialenergyvalues9[startsortindex]
    potentialenergyvalues9[startsortindex] = potentialenergyvalues9[swapindex]
    potentialenergyvalues9[swapindex] = tempval
    tempval = potentialenergyerrorvalues9[startsortindex]
    potentialenergyerrorvalues9[startsortindex] = potentialenergyerrorvalues9[swapindex]
    potentialenergyerrorvalues9[swapindex] = tempval

# Plotting section 

plt.errorbar(radii1, rotationalenergyvalues1, yerr = rotationalenergyerrorvalues1)
plt.errorbar(radii1, potentialenergyvalues1, yerr = potentialenergyerrorvalues1)
plt.errorbar(radii2, rotationalenergyvalues2, yerr = rotationalenergyerrorvalues2)
plt.errorbar(radii2, potentialenergyvalues2, yerr = potentialenergyerrorvalues2)
plt.errorbar(radii3, rotationalenergyvalues3, yerr = rotationalenergyerrorvalues3)
plt.errorbar(radii3, potentialenergyvalues3, yerr = potentialenergyerrorvalues3)
plt.errorbar(radii4, rotationalenergyvalues4, yerr = rotationalenergyerrorvalues4)
plt.errorbar(radii4, potentialenergyvalues4, yerr = potentialenergyerrorvalues4)
plt.errorbar(radii5, rotationalenergyvalues5, yerr = rotationalenergyerrorvalues5)
plt.errorbar(radii5, potentialenergyvalues5, yerr = potentialenergyerrorvalues5)
plt.errorbar(radii6, rotationalenergyvalues6, yerr = rotationalenergyerrorvalues6)
plt.errorbar(radii6, potentialenergyvalues6, yerr = potentialenergyerrorvalues6)
plt.errorbar(radii7, rotationalenergyvalues7, yerr = rotationalenergyerrorvalues7)
plt.errorbar(radii7, potentialenergyvalues7, yerr = potentialenergyerrorvalues7)
plt.errorbar(radii8, rotationalenergyvalues8, yerr = rotationalenergyerrorvalues8)
plt.errorbar(radii8, potentialenergyvalues8, yerr = potentialenergyerrorvalues8)
plt.errorbar(radii9, rotationalenergyvalues9, yerr = rotationalenergyerrorvalues9)
plt.errorbar(radii9, potentialenergyvalues9, yerr = potentialenergyerrorvalues9)

plt.xlabel('Lattice Spacing (Angstrom)')
plt.ylabel('Energies (K)')
plt.axis([0,30,-3000,1000])
plt.title('Energies vs. Lattice Spacing for 2 Waters and 1 Bead per Molecule')
plt.text(12, -300, r'Blue --> T = 15.0 K Potential Energies,')
plt.text(12, -450, r'Yellow --> T = 15.0 K Rotational Energies,')
plt.text(12, -600, r'Blue --> T = 70.0 K Potential Energies,')
plt.text(12, -750, r'Yellow --> T = 70.0 K Rotational Energies,')
plt.text(12, -900, r'Blue --> T = 95.0 K Potential Energies,')
plt.text(12, -1050, r'Yellow --> T = 95.0 K Rotational Energies,')
plt.text(12, -1200, r'Blue --> T = 140.0 K Potential Energies,')
plt.text(12, -1350, r'Yellow --> T = 140.0 K Rotational Energies,')
plt.text(12, -1500, r'Blue --> T = 145.0 K Potential Energies,')
plt.text(12, -1650, r'Yellow --> T = 145.0 K Rotational Energies,')
plt.text(12, -1800, r'Blue --> T = 150.0 K Potential Energies,')
plt.text(12, -1950, r'Yellow --> T = 150.0 K Rotational Energies,')
plt.text(12, -2100, r'Blue --> T = 155.0 K Potential Energies,')
plt.text(12, -2250, r'Yellow --> T = 155.0 K Rotational Energies,')
plt.text(12, -2400, r'Blue --> T = 160.0 K Potential Energies,')
plt.text(12, -2550, r'Yellow --> T = 160.0 K Rotational Energies,')
plt.text(12, -2700, r'Blue --> T = 293.0 K Potential Energies,')
plt.text(12, -2850, r'Yellow --> T = 293.0 K Rotational Energies,')
plt.show()

N = argv[10]
P = argv[11]

plt.savefig('N'+str(N)+'P'+str(P))


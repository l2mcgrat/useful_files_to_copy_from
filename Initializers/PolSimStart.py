from MMTK import *

from mbpol import mbpolForceField
from MMTK import Features
from MMTK.ForceFields.ForceField import CompoundForceField
#from MMTK.ForceFields.ForceFieldTest import gradientTest
from MMTK.Minimization import ConjugateGradientMinimizer
from MMTK.Environment import PathIntegrals
#from MMTK.NormalModes import VibrationalModes
from MMTK.Trajectory import Trajectory, TrajectoryOutput, \
                            RestartTrajectoryOutput, StandardLogOutput, \
                            trajectoryInfo

from sys import argv,exit
from numpy import zeros,cos,sin,sqrt,pi, dot, asarray, sign, arctan, arccos

#CHANGE INTEGRATOR HERE AND FURTHER BELOW WHERE THE INTEGRATOR IS CALLED

from H20Rigid3DRotor_PINormalModeIntegrator import Rigid3DRotor_PINormalModeIntegrator, Rigid3DRotor_PILangevinNormalModeIntegrator
from RotOnlyPINormalModeIntegrator import RotOnly3D_PINormalModeIntegrator, RotOnly3D_PILangevinNormalModeIntegrator

#CHANGE POTENTIAL (FORCEFIELD) HERE AND FURTHER BELOW WHERE THE POTENTIAL IS CALLED

#####################################
## set the number of quantum beads ##
#####################################

label = "Dip"
outdir = "/scratch/l2mcgrat/trajectoryfiles/"

# Parameters
rhoname = argv[1]
erotname = argv[2]
esqname = argv[3]

Rot_Step = argv[4] #Rot Step
R_e = float(argv[5])
Rot_Skip = argv[6] #Rot Skip Step

temperature = float(rhoname[rhoname.find("T")+1:rhoname.find("P")])*Units.K
P = int(rhoname[rhoname.find("P")+1:rhoname.find(".rho")])
numsteps = 100

lattice_spacing = R_e*Units.Ang

ndens = 23588101
denrho = zeros(ndens,float)
denerot = zeros(ndens,float)
denesq = zeros(ndens,float)

universe = InfiniteUniverse()
# nanometers

universe.addObject(PathIntegrals(temperature))

nmolecules = 2

center = zeros( (nmolecules,3) , float)

for i in range(nmolecules):
	universe.addObject(Molecule('water', position = Vector(i*lattice_spacing, 0., 0.)))
        center[i][0] = i*lattice_spacing

for atom in universe.atomList():
	atom.setNumberOfBeads(P)

# print "ATOMS"
# print  universe.atomList()

natoms = len(universe.atomList())/nmolecules

ff=[]

universe.setForceField(mbpolForceField(universe))

temp = zeros( ( P*natoms*nmolecules , 3 ) , float )

for i in range(P*natoms*nmolecules):
    for j in range(3):
        spacing = lattice_spacing*int(i/(P*natoms))
        temp[i][j] = universe.configuration().array[i][j]
        if j == 0:
            temp[i][j] = universe.configuration().array[i][j] - spacing
        universe.configuration().array[i][j] = 0.0

phi = 0.0
theta = pi/2.0
chi = 0.0

cp = cos(phi)
sp = sin(phi)
ct = cos(theta)
st = sin(theta)
ck = cos(chi)
sk = sin(chi)

rotmat = zeros( (3,3) , float )

rotmat[0][0]=cp*ct*ck-sp*sk
rotmat[0][1]=-cp*ct*sk-sp*ck
rotmat[0][2]=cp*st
rotmat[1][0]=sp*ct*ck+cp*sk
rotmat[1][1]=-sp*ct*sk+cp*ck
rotmat[1][2]=sp*st
rotmat[2][0]=-st*ck
rotmat[2][1]=st*sk
rotmat[2][2]=ct

for i in range(nmolecules*P*natoms):
    for j in range(3):
        for k in range(3):
            universe.configuration().array[i][j] += rotmat[j][k]*temp[i][k]

for i in range(P*natoms*nmolecules):
    for j in range(3):
        spacing = lattice_spacing*int(i/(P*natoms))
        temp[i][j] = universe.configuration().array[i][j]
        if j == 0:
            temp[i][j] = universe.configuration().array[i][j] + spacing
            universe.configuration().array[i][j] = temp[i][j]

# Minimize
#minimizer = ConjugateGradientMinimizer(universe,
#                                       actions=[StandardLogOutput(50)])
#minimizer(convergence = 1.e-3, steps = 10000)

universe.writeToFile('u2.pdb')

# gradientTest(universe)
#print (universe.energy())*120
universe.initializeVelocitiesToTemperature(temperature)

rhofile=open(rhoname,"r")
erotfile=open(erotname, "r")
esqfile=open(esqname, "r")

for i in range(ndens):
        denrho[i]=float(rhofile.readline())
        denerot[i]=float(erotfile.readline())*1.1963e-2 #cm-1 to kJ/mol [MMTK Units of Energy]
        denesq[i]=float(esqfile.readline())*(1.1963e-2)*(1.1963e-2)

rhofile.close()
erotfile.close()
esqfile.close()

dt = 1.0*Units.fs

# Initialize velocities
universe.initializeVelocitiesToTemperature(temperature)

# USE THE FRICTION PARAMETER FROM BEFORE
friction = 0.0

#integrator = Rigid3DRotor_PILangevinNormalModeIntegrator(universe, delta_t = dt, centroid_friction = friction, denrho = denrho, denerot = denerot, denesq = denesq, rotstep = float(Rot_Step), rotskipstep=float(Rot_Skip))

integrator = RotOnly3D_PILangevinNormalModeIntegrator(universe, delta_t = dt, centroid_friction = friction, denrho = denrho, denerot = denerot, denesq = denesq, rotstep = float(Rot_Step), rotskipstep=float(Rot_Skip))

integrator(steps = 3, actions = [ TrajectoryOutput(None,('configuration','time'), 0, None, 100)] )  # relates to the default_options = {'first_step': 0...} section of the main code.

RunSteps = int(numsteps)*Units.fs/dt
SkipSteps = 1.0*Units.fs/dt

filename = outdir+"N"+str(nmolecules)+"H20T"+str(temperature)+"P"+str(P)+"R"+str(lattice_spacing)+"FilePVersion"+str(numsteps)+"Steps"+label+".nc"

trajectory = Trajectory(universe, outdir+"N"+str(nmolecules)+"H20T"+str(temperature)+"P"+str(P)+"R"+str(lattice_spacing)+"FilePVersion"+str(numsteps)+"Steps"+label+".nc", "w", "A simple test case")

Nblocks = 1

############################## BEGIN ROTATION SIMULATION ##############################

# RUN PIMD WITH PIMC ROTATION INCLUDED
print "We're going to run the Langevin integrator for ", RunSteps/SkipSteps, "independent steps of PIMD"
integrator(steps=RunSteps,
           # Remove global translation every 50 steps.
	   actions = [
		   TrajectoryOutput(trajectory, ("time", "thermodynamic", "energy",
						 "configuration", "auxiliary"),
                                    0, None, SkipSteps)])


##############################              BEGIN ANALYSIS           ##############################
#gradientTest(universe)

cosfile = open("cosfile-"+"N"+str(nmolecules)+"H20T"+str(temperature)+"P"+str(P)+"R"+str(lattice_spacing)+"FilePVersion"+str(numsteps)+"Steps"+label,"w")

for step in trajectory:
    universe.setConfiguration(step['configuration'])
    for i in range(P):
        for a in range(len(universe.objectList()) - 1):         # loops over all molecules

            x1=universe.objectList()[a].atomList()[0].beadPositions()[i]  # hydrogen L
            x2=universe.objectList()[a].atomList()[1].beadPositions()[i]  # hydrogen R
            x3=universe.objectList()[a].atomList()[2].beadPositions()[i]  # oxygen

            mo1=universe.objectList()[a].atomList()[0].mass()
            mo2=universe.objectList()[a].atomList()[1].mass()
            mo3=universe.objectList()[a].atomList()[2].mass()

            cm = (x1*mo1 + x2*mo2 + x3*mo3) / (mo1 + mo2 + mo3)

            mu = x3 - cm

            norm1 = sqrt(dot(mu,mu))

            mu /= norm1

            cost = mu[0]
            theta = arccos(cost)*180.0/pi

            cosfile.write(str(theta)+"\n")

cosfile.close()

raise()

###################################################################################################
##############################       AUTOCORRELATION FUNCTIONS       ##############################

T = len(trajectory) #numbsteps
x = zeros( len(trajectory) , float )
counter = -1

#  we are trying to find C(tau) for the x position of the Oxygen atom on the water molecule
#  for the average bead position of the oxygen in each bead.

for step in trajectory:
    universe.setConfiguration(step['configuration'])
    counter += 1
    x[counter] = universe.objectList()[1].atomList()[2].position()[0]

C1file=open("C1file-"+str(nmolecules)+"-P-"+str(P)+"-"+label,"w")
C2file=open("C2file-"+str(nmolecules)+"-P-"+str(P)+"-"+label,"w")

for tau in range(T):
    C1 = 0.0
    C2 = 0.0

    for t in range(T - tau):
        C1 += ( x[t]*x[t+tau] - mean*mean ) / ( ( T + 1 - tau )*( variance ) )
        C2 += ( x[t] - mean )*( x[t+tau] - mean ) / ( ( T + 1 - tau )*( variance ) )

    if tau <= 3*T/4:
        C1file.write(str(C1)+"\n")
        C2file.write(str(C2)+"\n")

###################################################################################################

npoints = len(trajectory)
universe = trajectory.universe
natoms = universe.numberOfAtoms()
time = trajectory.time
np = universe.numberOfPoints()
P = np / natoms
#gradientTest(universe)
trajectory.close()

afile1.close()
afile2.close()
Xfile.close()
C1file.close()
C2file.close()


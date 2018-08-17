#!/usr/bin/python
import os
from os import system
from subprocess import call

def jobstring_sbatch(T,R,S,N,P):
	'''
	This function creats jobstring for #SBATCH script
	'''
	job_name       = "MyjobT"+str(T)+"R"+str(R)+"S"+str(S)
	walltime       = "40-00:00"
	omp_thread     = 1
#    logPath        = "/home/l2mcgrat/MBPolPaperN8/output_files/"+job_name

	exe_file       = "$HOME/.mmtk/bin/python2.7 test-pimd-energy_analysis.py /scratch/l2mcgrat/trajectoryfiles/N"+str(N)+"H20T"+str(T)+"P"+str(P)+"R"+str(R)+"FilePVersion"+str(S)+"StepsDip.nc"

	job_string     = """#!/bin/bash
#SBATCH --job-name=%s
#SBATCH --time=00:10:00
#SBATCH --mem-per-cpu=3069M 
#SBATCH --account=rrg-pnroy
#SBATCH --output=%s.out
%s
""" % (job_name, job_name, exe_file)

	return job_string

# Main function

NList = [2, 4, 6, 8, 10]
PList = [10]
RList = [0.24, 0.255, 0.27, 0.285, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.6, 2.0, 2.5, 3.0]
SList = [1000]
TList = [15.0, 70.0, 95.0, 140.0, 145.0, 150.0, 155.0, 160.0, 293.0]

print(TList)
print(RList)
print(SList)

for S in SList:
    for R in RList:
        for T in TList:
            for N in NList:
                for P in PList:
                    fname="job-N"+str(N)+"P"+str(P)+"R"+str(R)+"T"+str(T)+"S"+str(S)
                    fileName = open(fname,'w')
                    fileName.write(jobstring_sbatch(T,R,S,N,P))
                    fileName.close()
                    call(["sbatch", fname])
                    call(["rm", fname])


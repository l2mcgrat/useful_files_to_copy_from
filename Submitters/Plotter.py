#!/usr/bin/python
import os
from os import system
from subprocess import call

def jobstring_sbatch(N, P):
	'''
	This function creats jobstring for #SBATCH script
	'''
	job_name       = "MyjobN"+str(N)+"P"+str(P) 
	walltime       = "40-00:00"
	omp_thread     = 1
#    logPath        = "/home/l2mcgrat/MBPolPaperN8/output_files/"+job_name

	exe_file       = "$HOME/.mmtk/bin/python2.7 plotenergiesvslatticespacing.py energy-T15.0steps1000nmolecules"+str(N)+"nbeads"+str(P)+" energy-T70.0steps1000nmolecules"+str(N)+"nbeads"+str(P)+" energy-T95.0steps1000nmolecules"+str(N)+"nbeads"+str(P)+" energy-T140.0steps1000nmolecules"+str(N)+"nbeads"+str(P)+" energy-T145.0steps1000nmolecules"+str(N)+"nbeads"+str(P)+" energy-T150.0steps1000nmolecules"+str(N)+"nbeads"+str(P)+" energy-T155.0steps1000nmolecules"+str(N)+"nbeads"+str(P)+" energy-T160.0steps1000nmolecules"+str(N)+"nbeads"+str(P)+" energy-T293.0steps1000nmolecules"+str(N)+"nbeads"+str(P)+" "+str(N)+" "+str(P)

	job_string     = """#!/bin/bash
#SBATCH --job-name=%s
#SBATCH --time=00:03:00
#SBATCH --mem-per-cpu=3069M 
#SBATCH --account=rrg-pnroy
#SBATCH --output=%s.out       
%s
""" % (job_name, job_name, exe_file)

	return job_string

# Main function

PList = [2, 4, 6, 8, 10]
NList = [2, 4, 6, 8, 10]

print(NList)

for N in NList:
    for P in PList:
        fname="job-N"+str(N)+"P"+str(P)
        fileName = open(fname,'w')
        fileName.write(jobstring_sbatch(N,P))
        fileName.close()
        call(["sbatch", fname])
        call(["rm", fname])

#!/usr/bin/python
import os
from os import system
from subprocess import call

def jobstring_sbatch(T,R,S):
	'''
	This function creats jobstring for #SBATCH script
	'''
	job_name       = "MyjobT"+str(T)+"R"+str(R)+"S"+str(S)
	walltime       = "40-00:00"
	omp_thread     = 1
#    logPath        = "/home/l2mcgrat/MBPolPaperN8/output_files/"+job_name

	exe_file       = "time $HOME/.mmtk/bin/python2.7 PolSimStart.py /scratch/l2mcgrat/d/H2O_T"+str(T)+"P8.rho /scratch/l2mcgrat/d/H2O_T"+str(T)+"P8.eng /scratch/l2mcgrat/d/H2O_T"+str(T)+"P8.esq "+str(S)+" "+str(R)+" 1"

	job_string     = """#!/bin/bash
#SBATCH --job-name=%s
#SBATCH --time=00:40:00
#SBATCH --mem-per-cpu=3069M 
#SBATCH --account=rrg-pnroy
#SBATCH --output=%s.out       
%s
""" % (job_name, job_name, exe_file)

	return job_string

# Main function

RList = [2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.25, 3.5, 3.75, 4.0]
TList = [15, 70, 95, 140, 145, 150, 155, 160, 293]  
SList = [0.3, 0.15, 0.12, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3, 0.15, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3, 0.15, 0.15, 0.1, 0.1, 0.1, 0.1, 0.1, 0.07, 0.3, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.07, 0.3, 0.15, 0.12, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3, 0.13, 0.15, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3, 0.13, 0.13, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3, 0.13, 0.13, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3, 0.13, 0.13, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3, 0.13, 0.13, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3, 0.13, 0.13, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

print(TList)
print(RList)
print(SList)

it = 0
for R in RList:
	for T in TList:
		S = SList[it]
		it += 1
		fname="job-T"+str(T)+"R"+str(R)+"S"+str(S)
		fileName = open(fname,'w')
		fileName.write(jobstring_sbatch(T,R,S))
		fileName.close()
		call(["sbatch", fname])
		call(["rm", fname])


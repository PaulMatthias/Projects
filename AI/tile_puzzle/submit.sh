#!/bin/bash
#SBATCH --job-name=tile_puzzle
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --partition=compute
##SBATCH --partition=atlas,atlasnew
##SBATCH --exclude hpc-mem01
##SBATCH --nodelist=hpc-mem01
#SBATCH --mail-type=end
#SBATCH --mail-user=pm101481@physik.uni-greifswald.de
#SBATCH --share

source ~/.bashrc

echo "$SLURM_JOB_ID"

#module load superlu/4.3
#module load mkl/2015.3.187
#module load gcc/5.2.0
#module load openmpi/1.10.0/gcc/5.2.0  
#module load openmpi

ulimit -s unlimited


echo " "
echo "** jobname: $SLURM_JOB_NAME"
echo "** SLURM_JOB_ID = $SLURM_JOB_ID"
#echo "** RECOVRUN = $RECOVRUN"



python driver.py dfs 1,2,5,3,4,0,6,7,8

#scp -r $RUNDIR/ gstoppa@141.53.32.31:/home/gstoppa/Desktop/test
# possible plot routine auto call, e.g. for initial and final state of the discharge

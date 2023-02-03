#!/bin/bash
#PBS -N lich-compute
#PBS -q cheminf
#PBS -l select=1:host=lich-compute9:ncpus=8:mem=4gb
#PBS -l walltime=48:00:00
#PBS -e /home/$USER/diplomka/class_algorithm/settings_default/log
#PBS -o /home/$USER/diplomka/class_algorithm/settings_default/log


# define a DATADIR variable: directory where the input files are taken from and where output will be copied to
DATADIR=/home/$USER/diplomka/class_algorithm/settings_default
SCRATCHDIR=/scratch/$USER/

# append a line to a file "jobs_info.txt" containing the ID of the job, the hostname of node it is run on
# this information helps to find the scratch directory (and other files) in case the job fails and you need to remove the scratch directory manually 
echo "$PBS_JOBID is running on node `hostname -f` in a scratch directory $SCRATCHDIR" >> $DATADIR/jobs_info.txt

echo "JOB_ID: $PBS_JOBID yours INPUT_DATA: $arg1 $arg2 $arg3 $arg4 $arg5">> $DATADIR/jobs_id_input.txt


# copy files we will need for the calculation to our scratch
# if the copy operation fails, issue an error message and exit
mkdir $SCRATCHDIR/$PBS_JOBID
cp /home/$USER/diplomka/data/data_set_bi_pro_Martina.csv $SCRATCHDIR/$PBS_JOBID || { echo >&2 "Error while copying input file(s)!"; exit 2; }
cp $DATADIR/run_class.py $SCRATCHDIR/$PBS_JOBID || { echo >&2 "Error while copying input file(s)!"; exit 2; }
#cp $DATADIR/input_pair_VDR.csv $SCRATCHDIR/$PBS_JOBID || { echo >&2 "Error while copying input file(s)!"; exit 2; }


# move into scratch directory
cd $SCRATCHDIR/$PBS_JOBID



# run your code
eval "$(command conda 'shell.bash' 'hook' 2> /dev/null)"
conda activate /home/$USER/.conda/envs/molpher-lib-run/
#echo "$(printenv;nvidia-smi;conda env list;conda list)" > environment.txt
python3 run_class.py  ${arg1} ${arg2} ${arg3} ${arg4} ${arg5} # some hard work for the CPUs and GPUs


cd ..
if [[ -f $PBS_JOBID/run_class_${arg2}_${arg3}/result.csv ]]
then 
    
    cp -R $PBS_JOBID $DATADIR/results|| { echo >&2 "Result file(s) copying failed (with a code $?)!!! You can retrieve your files from `hostname -f`:`pwd`"; exit 4; }
    
fi


# clean the SCRATCH directory
rm -r $PBS_JOBID

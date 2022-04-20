#!/bin/bash


a=0
sed 1d $"/home/$USER/diplomka/data/data_set_bi_pro_Martina.csv" | while IFS=, read -r id_pair start_id stop_id start_smiles stop_smiles
#while IFS=, read -r start_id stop_id start_smiles stop_smiles

do 
   echo "$a"
   echo "$start_id";
   echo "$stop_id";
   echo "$start_smiles";
   echo "$stop_smiles";
   
   qsub -v arg1=$id_pair,arg2=$start_id,arg3=$stop_id,arg4=$start_smiles,arg5=$stop_smiles skript_pro_run_class.sh
   let "a++"
   
done 
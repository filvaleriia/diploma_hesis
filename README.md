# diploma_thesis

# CONTENT
1. folder data consist of:
  - VDRML_chembl_inputs.csv - 47 active VDR ligands on which scaffold analysis was performed
  - inputs_VDR_pairs.csv - input data for Molpher algorithm already containing start and target (stop) molecule
  - output_Molpher/
    - contains output_data_after_Molpher.zip, where are all generated sets
  - scaffolds/
    -  contains scaffolds.zip where all sets are already converted to scaffolds
  - metrics/
    - contains metrics.zip, where Metrics are calculated, but without TPRA and TPRAR metrics for each path
   
2. folder Molpher consist of:
  - pousteni_run_class.sh - a script that did the job for each start / target pair
  - skript_pro_run_class.sh - script responsible for assigning CPU, RAM and copying the resulting output files back from scratch to home directory
  - run_class.py - Molpher script in python, this example script is for default settings, to change a parameter it is necessary to change settings
  

3. folder plots: contains metrics visualizations

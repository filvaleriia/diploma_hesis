#!/usr/bin/python 
from molpher.algorithms.bidirectional.run import run as run_bi
from molpher.algorithms.classic.run import run as run_class
from molpher.algorithms.settings import Settings

import pandas as pd
import sys
import os, time
from rdkit import DataStructs
from rdkit import Chem




def generate_path(id_pair,start_id, stop_id, start, finish, algorithm = run_class, storage_dir = None, max_threads = 2):
    tanimota_podobnost = DataStructs.FingerprintSimilarity(Chem.RDKFingerprint(Chem.MolFromSmiles(start_smiles))
                                                     ,Chem.RDKFingerprint(Chem.MolFromSmiles(stop_smiles)),
                                                     metric=DataStructs.TanimotoSimilarity)
    for interakce in range(5):
        
        print("Tanimotova podobnost:", tanimota_podobnost)
        storage_dir=f"run_class_{start_id}_{stop_id}"
        print(storage_dir)
        if not os.path.exists(storage_dir):
            os.makedirs(storage_dir)

        settings = Settings(
            start
            , finish
            , storage_dir
            , max_iters=300
            , max_threads=max_threads
        )
        before = time.perf_counter()
        try:
            path = algorithm(settings)
        except:
            continue
        after = time.perf_counter()
        print('Path found after', after - before, 'seconds.')
        
        delka = len(path)
        print("Delka",delka)
        
        print("Tanimotova podobnost:", tanimota_podobnost)
        
        print("PATH: ", path)
        print("\n")
        
        out = open(f"run_class_{start_id}_{stop_id}/out.csv","a")
        #out.write("Start {0} Stop {1} Interakce {2} Delka {3} Time {4} Tanimotov {5}".format(start_id, stop_id,interakce,delka,after-before,tanimota_podobnost))
        out.write("{0},{1},{2},{3},{4},{5},{6} \n".format(id_pair,interakce,start_id, stop_id,delka,after-before,tanimota_podobnost))
        out.close()

        result=open(f"run_class_{start_id}_{stop_id}/result.csv","a")
        result.write("{0},{1},{2},{3},{4},{5},{6} \n".format(id_pair,interakce,start_id,stop_id, start_smiles,stop_smiles,list(path)))
        result.close()

        result_1=open(f"run_class_{start_id}_{stop_id}/result_split_path.csv","a")
        for morph in path:
            result_1.write("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9}\n".format(id_pair,interakce,start_id,stop_id, start_smiles,stop_smiles,morph,tanimota_podobnost,delka,after-before))
        result_1.close()

    return path

id_pair=sys.argv[1]
start_id = sys.argv[2]
stop_id = sys.argv[3]
start_smiles = sys.argv[4]
stop_smiles = sys.argv[5]


print(start_id)
print(stop_id)
print(start_smiles)
print(stop_smiles)

bi_path = generate_path(
    id_pair,
    start_id,
    stop_id,  
    start_smiles, ##'CN1C2CCC1C(C(=O)OC)C(OC(=O)c1ccccc1)C2',
    stop_smiles, #'O=C(OCCN(CC)CC)c1ccc(N)cc1',
    run_class,
    max_threads=8,
)



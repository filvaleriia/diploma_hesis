import pandas as pd
import numpy as np
from rdkit import Chem
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem import AllChem
from rdkit.Chem.Scaffolds.MurckoScaffold import GetScaffoldForMol
from rdkit.Chem.Scaffolds.MurckoScaffold import MurckoScaffoldSmiles
from rdkit.Chem.Scaffolds.MurckoScaffold import MakeScaffoldGeneric
import seaborn as sns
import matplotlib.pyplot as plt
import sys

def convert_to_scaffold(df):
    print("Convert_")
    
    df = df[0].apply(lambda x : MurckoScaffoldSmiles(Chem.MolToSmiles(MakeScaffoldGeneric(Chem.MolFromSmiles(x)))))
    return df

def add_columns_same_like_input_function(df_generated, inputt):
    print("add_columns_same_like_input_function")
    df_generated = pd.DataFrame(df_generated)   
    df = pd.DataFrame()
    df[0] = inputt
    df[1] = int(0)
    for x in range(len(inputt)):
        print(x)
        y = df[0][x]
        df[1][x] = [df_generated[0].value_counts()[y] if y in df_generated[0].unique() else 0][0]       
    
    df[2] = df[1].apply(lambda x : 1 if x > 0 else 0)
    return df


def main_function(df_generated, df_input):
    df_input = convert_to_scaffold(df_input)
    df_generated = convert_to_scaffold(df_generated)
    unique_compounds_in_whole_generated_set = df_generated.unique()
    unique_input = df_input.unique()
    
    df = add_columns_same_like_input_function(df_generated, unique_input)
    
    df1 = add_columns_same_like_input_function(unique_compounds_in_whole_generated_set, unique_input)

    print("Pocet_unikatnich_scaffoldu", len(unique_compounds_in_whole_generated_set))
    print("Size of dataset", len(df_generated))
    print("SeScY",len(unique_compounds_in_whole_generated_set)/len(df_generated))
    print(f"TPRA:  {df[2].value_counts()[1]}/{len(df)} = {df[2].value_counts()[1]/len(df)}", )
    print("SeScR",df1[2].sum()/len(unique_compounds_in_whole_generated_set))
    print("aSeScR",df[1].sum()/len(df_generated))
    
    


if __name__ == "__main__":
    generated_compounds = []
    input_coumpounds = []
    
    #nacitani vstupu
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            generated_compounds.append(line)
    df_generated = pd.DataFrame(generated_compounds)

    with open(sys.argv[2], 'r') as f:
        for line in f.readlines():
            input_coumpounds.append(line)
    df_input = pd.DataFrame(input_coumpounds)

    print(type(df_generated))
    print(type(df_input))
    
    main_function(df_generated, df_input)

    
       




















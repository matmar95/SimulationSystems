import pandas as pd
import numpy as np
import scipy
import scipy.stats as st
import os
import math
import csv

for root, dirs, files in os.walk('../ResponseTimeNetwork/results'):
    for name in files:
        if str(name)=='I5_E2.csv':

            df = pd.read_csv('../ResponseTimeNetwork/results/I5_E2.csv',index_col=0)
            df.rename(columns={'Unnamed: 4': 'value'}, inplace=True)
            keep_col = ['repetition', 'value']
            newDf = df[keep_col]
            print(newDf['value'].mean())
            newDf.to_csv("newFile.csv", index=False)

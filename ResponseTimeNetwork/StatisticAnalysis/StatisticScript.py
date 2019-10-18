import pandas as pd
import numpy as np
import scipy
import scipy.stats as st
import os
import math
import csv

runs = 20
t95 = 2.093
t90 = 1.729

for x in os.walk('./data'):
    for i in ['First', 'Second', 'Third']:
        if './data/' + i + '_config' == str(x[0]):
            rowLength = []
            rowLifeTime = []
            rowMinMax = []
            for y in os.walk(x[0]):
                for e in ['2', '5', '8', '9']:
                    config_dir = './data/' + i + '_config'+'/' + i + '_exit_' + e
                    if config_dir == str(y[0]):
                        for root, dirs, files in os.walk(y[0]):
                            print("\n*******************************\n")
                            print(config_dir + "\n")
                            for name in files:
                                if name != ".DS_Store":
                                    file_dir = config_dir + "/" + str(name)
                                    print(name)
                                    df = pd.read_csv(file_dir)
                                    newHeader = ['run', 'repetition', 'Module', 'Name', 'Value']
                                    df.to_csv(file_dir, header=newHeader, index=False)
                                    mean = df['Value'].mean()
                                    stdDev = df['Value'].std()
                                    variance = df['Value'].var()
                                    stdErr = stdDev/(math.sqrt(runs))
                                    print("Media: " + str(mean))
                                    print("Deviazione standard: "+ str(stdDev))
                                    print("Variance: " + str(variance))
                                    print("Err standard: " + str(stdErr))
                                    min_95 = mean - (t95 * math.sqrt(variance) / math.sqrt(runs))
                                    max_95 = mean + (t95 * math.sqrt(variance) / math.sqrt(runs))
                                    print("LowBound t95 ConfInt: " + str(min_95) + " - UpBound ConfInt: " + str(max_95))
                                    min_90 = mean - (t90 * math.sqrt(variance) / math.sqrt(runs))
                                    max_90 = mean + (t90 * math.sqrt(variance) / math.sqrt(runs))
                                    print("LowBound t95 ConfInt: " + str(min_90) + " - UpBound ConfInt: " + str(max_90))
                                    print("\n")
                                    newName = name[:-4]
                                    if "Length" in name:
                                        rowLength.append([e, newName, round(mean, 3), round(min_95, 3), round(max_95, 3)])
                                    if "LifeTime" in name:
                                        if "min" in name or "max" in name:
                                            rowMinMax.append([e, newName, round(mean, 3), round(min_95, 3), round(max_95, 3)])
                                        else:
                                            rowLifeTime.append([e, newName, round(mean, 3), round(min_95, 3), round(max_95, 3)])

                dfRowLength = pd.DataFrame(rowLength, columns=["exitProb", "name", "mean", "lowConfInt", "upConfInt"])
                dfRowLength.to_csv('./data/' + i + '_config/results/'+i+'_LengthQueue.csv', index=False)
                dfLifeTime = pd.DataFrame(rowLifeTime, columns=["exitProb", "name", "mean", "lowConfInt", "upConfInt"])
                dfLifeTime.to_csv('./data/' + i + '_config/results/' + i + '_LifeTime.csv', index=False)
                dfRowMinMax = pd.DataFrame(rowMinMax, columns=["exitProb", "name", "mean", "lowConfInt", "upConfInt"])
                dfRowMinMax.to_csv('./data/' + i + '_config/results/' + i + '_LifeTimeMinMax.csv', index=False)

                print(rowLifeTime)
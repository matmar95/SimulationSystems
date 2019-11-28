import pandas as pd
import numpy as np
import scipy
import scipy.stats as st
import os
import math
import csv
import matplotlib
import matplotlib.pyplot as plt


runs = 20
t95 = 2.093
t90 = 1.729

for x in os.walk('./data'):
    for i in ['First', 'Second', 'Third']:
        if './data/' + i + '_config' == str(x[0]):
            rowLength = []
            rowLifeTime = []
            rowMinMax = []
            rowLifeTimeCount = []
            rowServiceTime = []
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
                                    df = pd.read_csv(file_dir)
                                    #setHeader
                                    newHeader = ['Run', 'Repetition', 'Module', 'Name', 'Value']
                                    df.to_csv(file_dir, header=newHeader, index=False)
                                    dfNew = pd.read_csv(file_dir)

                                    if name == 'LifeTimeCount.csv':
                                        rowRatio = []
                                        for rep in range(0, 20):
                                            rowNumJobs = dfNew.loc[
                                                (dfNew['Repetition'] == rep) & (dfNew['Name'] == 'numJobs:count')]
                                            row2s = dfNew.loc[
                                                (dfNew['Repetition'] == rep) & (dfNew['Name'] == 'lifeTime2s:count')]
                                            row3s = dfNew.loc[
                                                (dfNew['Repetition'] == rep) & (dfNew['Name'] == 'lifeTime3s:count')]
                                            row4s = dfNew.loc[
                                                (dfNew['Repetition'] == rep) & (dfNew['Name'] == 'lifeTime4s:count')]
                                            ratio2s = int(row2s['Value']) / int(rowNumJobs['Value'])
                                            ratio3s = int(row3s['Value']) / int(rowNumJobs['Value'])
                                            ratio4s = int(row4s['Value']) / int(rowNumJobs['Value'])
                                            rowRatio.append([ratio2s, ratio3s, ratio4s])

                                        rowRatio = np.array(rowRatio)
                                        mean = np.mean(rowRatio, axis=0)
                                        stdDev = np.std(rowRatio, axis=0)
                                        variance = np.var(rowRatio, axis=0)
                                        stdErr = stdDev / (math.sqrt(runs))
                                        min_95_2s = mean[0] - (t95 * math.sqrt(variance[0]) / math.sqrt(runs))
                                        max_95_2s = mean[0] + (t95 * math.sqrt(variance[0]) / math.sqrt(runs))
                                        min_95_3s = mean[1] - (t95 * math.sqrt(variance[1]) / math.sqrt(runs))
                                        max_95_3s = mean[1] + (t95 * math.sqrt(variance[1]) / math.sqrt(runs))
                                        min_95_4s = mean[2] - (t95 * math.sqrt(variance[2]) / math.sqrt(runs))
                                        max_95_4s = mean[2] + (t95 * math.sqrt(variance[2]) / math.sqrt(runs))
                                        rowLifeTimeCount.append([e, 'Threshold-2s', round(mean[0]*100, 2), round(min_95_2s*100, 2), round(max_95_2s*100, 2)])
                                        rowLifeTimeCount.append([e, 'Threshold-3s', round(mean[1]*100, 2), round(min_95_3s*100, 2), round(max_95_3s*100, 2)])
                                        rowLifeTimeCount.append([e, 'Threshold-4s', round(mean[2]*100, 2), round(min_95_4s*100, 2), round(max_95_4s*100, 2)])
                                    else:
                                        mean = dfNew['Value'].mean()
                                        stdDev = dfNew['Value'].std()
                                        variance = dfNew['Value'].var()
                                        stdErr = stdDev/(math.sqrt(runs))
                                        min_95 = mean - (t95 * math.sqrt(variance) / math.sqrt(runs))
                                        max_95 = mean + (t95 * math.sqrt(variance) / math.sqrt(runs))
                                        min_90 = mean - (t90 * math.sqrt(variance) / math.sqrt(runs))
                                        max_90 = mean + (t90 * math.sqrt(variance) / math.sqrt(runs))
                                        newName = name[:-4]
                                        if "Total" in name:
                                            rowServiceTime.append([e, newName, round(mean,3)])
                                        if "Length" in name:
                                            rowLength.append([e, newName, round(mean, 3), round(min_95, 3), round(max_95, 3)])
                                        if "LifeTime" in name:
                                            if "min" in name or "max" in name:
                                                rowMinMax.append([e, newName, round(mean, 3), round(min_95, 3), round(max_95, 3)])
                                            else:
                                                rowLifeTime.append([e, newName, round(mean, 3), round(min_95, 3), round(max_95, 3)])

                dfRowLength = pd.DataFrame(rowLength, columns=["exitProb", "Name", "Mean", "lowConfInt", "upConfInt"])
                dfRowLength.to_csv('./data/' + i + '_config/results/'+i+'_LengthQueue.csv', index=False)
                dfLifeTime = pd.DataFrame(rowLifeTime, columns=["exitProb", "Name", "Mean", "lowConfInt", "upConfInt"])
                dfLifeTime.to_csv('./data/' + i + '_config/results/' + i + '_LifeTime.csv', index=False)
                dfRowMinMax = pd.DataFrame(rowMinMax, columns=["exitProb", "Name", "Mean", "lowConfInt", "upConfInt"])
                dfRowMinMax.to_csv('./data/' + i + '_config/results/' + i + '_LifeTimeMinMax.csv', index=False)
                dfLifeTimeCount = pd.DataFrame(rowLifeTimeCount, columns=["exitProb", "Name", "Mean", "lowConfInt", "upConfInt"])
                dfLifeTimeCount.to_csv('./data/' + i + '_config/results/' + i + '_LifeTimeThreshold.csv', index=False)
                dfServiceTime = pd.DataFrame(rowServiceTime, columns=["exitProb", "Name", "Mean"])
                dfServiceTime.to_csv('./data/' + i + '_config/results/' + i + '_ServiceTime.csv', index=False)


for x in os.walk('./data'):
    for i in ['First', 'Second', 'Third']:
        if './data/' + i + '_config/results' == str(x[0]):
            lengthQueue = []
            lifeTime = []
            lifeTimeMinMax = []
            threshold = []
            for name in ['LengthQueue.csv', 'LifeTime.csv', 'LifeTimeMinMax.csv', 'LifeTimeThreshold.csv']:
                file_dir = './data/' + i + '_config/results/'+i+"_"+name
                df = pd.read_csv(file_dir)
                df = df.sort_values(by=['exitProb'])
                print("**************************")
                print(i + " " + name)
                print(df)
                if name == 'LengthQueue.csv':
                    arr = ['LengthQueueU1', 'LengthQueueU2', 'LengthSS1', 'LengthSS2']
                if name == 'LifeTime.csv':
                    arr = ['LifeTimeTot', 'LifeTimeU1', 'LifeTimeU2']
                if name == 'LifeTimeMinMax.csv':
                    arr = ['LifeTimeU1max', 'LifeTimeU1min', 'LifeTimeU2max', 'LifeTimeU2min']
                if name == 'LifeTimeThreshold.csv':
                    arr = ['Threshold-2s', 'Threshold-3s', 'Threshold-4s']

                for element in arr:
                    arrElement = df.loc[
                        (df['Name'] == element)]
                    plot = arrElement.plot(x="exitProb", y=['lowConfInt', "Mean", 'upConfInt'], kind="bar", width=0.9)
                    for p in plot.patches:
                        plot.annotate(round(p.get_height(), 2), (round(p.get_x(), 2), round(p.get_height(), 2)))
                    plot.set_title(str(i + " config - " + element), fontsize=20)
                    plt.savefig('./graph/notransient/' + i + "_config_" + element + ".png")
                    plt.rcParams.update({'font.size': 8})
                    #plt.show()
                    #plot = element.plot(kind="line", x="exitProb", y='lowConfInt', ax=ax)


                '''for rep in [2, 5, 8, 9]:
                    if name == 'LengthQueue.csv':
                        lengthQueueU2 = df.loc[
                            (df['exitProb'] == rep) & (df['Name'] == 'LengthQueueU2')]
                        lengthQueueU1 = df.loc[
                            (df['Name'] == 'LengthQueueU1')]
                        lengthSS1 = df.loc[
                            (df['exitProb'] == rep) & (df['Name'] == 'LengthSS1')]
                        lengthSS2 = df.loc[
                            (df['exitProb'] == rep) & (df['Name'] == 'LengthSS2')]
                        
                        print(groupby)
                        #lengthQueue.append([rep, round(float(lengthQueueU1['Mean']), 3), round(float(lengthQueueU2['Mean']), 3), round(float(lengthSS1['Mean']), 3), round(float(lengthSS2['Mean']),3)])
                        #print(lengthQueue)
                    if name == 'LifeTime.csv':
                        lifeTimeU1 = df.loc[
                            (df['exitProb'] == rep) & (df['Name'] == 'lifeTimeU1')]
                        lifeTimeU2 = df.loc[
                            (df['exitProb'] == rep) & (df['Name'] == 'lifeTimeU2')]
                        lifeTimeTot = df.loc[
                            (df['exitProb'] == rep) & (df['Name'] == 'lifeTimeTot')]
                        lifeTimeU1 = lifeTimeU1['Mean'].astype(int)
                        lifeTimeU2 = lifeTimeU2['Mean'].astype(int)
                        lifeTimeTot = lifeTimeTot['Mean'].astype(int)
                        lifeTime.append([rep, round(lifeTimeU1, 3), round(lifeTimeU2, 3), round(lifeTimeTot, 3)])

                    if name == 'LifeTimeMinMax.csv':
                        lifeTimeU1min = df.loc[
                            (df['exitProb'] == rep) & (df['Name'] == 'lifeTimeU1min')]
                        lifeTimeU1max = df.loc[
                            (df['exitProb'] == rep) & (df['Name'] == 'lifeTimeU1max')]
                        lifeTimeU2min = df.loc[
                            (df['exitProb'] == rep) & (df['Name'] == 'lifeTimeU2min')]
                        lifeTimeU2max = df.loc[
                            (df['exitProb'] == rep) & (df['Name'] == 'lifeTimeU2max')]
                        lifeTimeU1min = lifeTimeU1min['Mean'].astype(int)
                        lifeTimeU1max = lifeTimeU1max['Mean'].astype(int)
                        lifeTimeU2min = lifeTimeU2min['Mean'].astype(int)
                        lifeTimeU2max = lifeTimeU2max['Mean'].astype(int)
                        lifeTimeMinMax.append([rep, round(lifeTimeU1min, 3), round(lifeTimeU1max, 3), round(lifeTimeU2min, 3), round(lifeTimeU2max, 3)])

                    if name == 'LifeTimeTreshold.csv':
                        treshold2s = df.loc[
                            (df['exitProb'] == rep) & (df['Name'] == 'Treshold-2s')]
                        treshold3s = df.loc[
                            (df['exitProb'] == rep) & (df['Name'] == 'Treshold-3s')]
                        treshold4s = df.loc[
                            (df['exitProb'] == rep) & (df['Name'] == 'Treshold-4s')]
                        treshold2s = treshold2s['Mean'].astype(int)
                        treshold3s = treshold3s['Mean'].astype(int)
                        treshold4s = treshold4s['Mean'].astype(int)
                        treshold.append([rep, round(treshold2s, 3), round(treshold3s, 3), round(treshold4s, 3)])

            dfLengthQueue = pd.DataFrame(lengthQueue, columns=["exitProb", "LengthQueueU1", "LengthQueueU2", "LengthSS1", "LengthSS2"])
            dfLengthQueue.to_csv('./data/' + i + '_config/results/' + i + '_LengthQueueMean.csv', index=False)

            dfLifeTime = pd.DataFrame(lifeTime, columns=["exitProb", "LifeTimeU1", "LifeTimeU2", "LifeTimeTot"])
            dfLifeTime.to_csv('./data/' + i + '_config/results/' + i + '_LifeTimeMean.csv', index=False)

            dfLifeTimeMinMax = pd.DataFrame(lifeTimeMinMax, columns=["exitProb", "LifeTimeU1min", "LifeTimeU1max", "LifeTimeU2min", "LifeTimeU2max"])
            dfLifeTimeMinMax.to_csv('./data/' + i + '_config/results/' + i + '_LifeTimeMinMaxMean.csv', index=False)

            dfTreshold = pd.DataFrame(treshold, columns=["exitProb", "Treshold-2s", "Treshold-3s", "Treshold-4s"])
            dfTreshold.to_csv('./data/' + i + '_config/results/' + i + '_LifeTimeTresholdMean.csv', index=False)'''

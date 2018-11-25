#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 14:44:08 2018

@author: swat
"""
import pandas as pd



data=pd.read_csv('/Users/swat/Desktop/Sem_1/Text_Analytics/data.csv')

Threshold = data['Threshold']
TP = data['TP']
FN = data['FN']
FP = data['FP']
TN = data['TN'] 

Precision = []

for p,q in zip(TP,FP):
    ppv = round(p/(p+q),4)
    Precision.append(ppv)

print("Precision:",Precision)

Recall = []

for p,q in zip(TP,FN):
    TPR = p/(p+q)
    Recall.append(TPR)
    
print("Recall:",Recall)

F1Measure = []

for p,q,r in zip(TP,FP,FN):
    FM = round((2*p)/((2*p)+q+r),4)
    F1Measure.append(FM)
    
print("F1Measure:",F1Measure)

FPR = []

for p,q in zip(FP,TN):
    FPRate = p/(p+q)
    FPR.append(FPRate)
print("FalsePositiveRate:",FPR)

FNR = []

for p,q in zip(FN,TP):
    FNRate = p/(p+q)
    FNR.append(FNRate)
print("FalseNegativeRate:",FNR)


final_matrix=[]


final_matrix.append(Threshold)
final_matrix.append(TP)
final_matrix.append(FN)
final_matrix.append(FP)
final_matrix.append(TN)
final_matrix.append(Precision)
final_matrix.append(Recall)
final_matrix.append(F1Measure)

import numpy
print('Threshold  TP      FN      FP      TN     Precision   Recall   F1Measure')
print(numpy.transpose(final_matrix))

#t_matrix=zip(*final_matrix)
#
#print('Threshold TP FN FP TN Precision Recall F1Measure')
#for row in t_matrix:
#    print (row)






import matplotlib.pyplot as plt

plt.plot(FPR, Recall, color='red')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC curve')
plt.show()

#import matplotlib.pyplot as plt1
import numpy as np

#plt1.plot(FPR, FNR, color='green')
#plt1.xscale('log')
#plt1.yscale('log')
#plt1.xlabel('False Positive Rate')
#plt1.ylabel('False Negative Rate')
#plt1.title('DET curve')
#ticks=[0.02,0.05,0.1,0.2,0.5,1,2]
#plt1.xticks(ticks)
#plt1.show()

from matplotlib import pyplot as plt
import matplotlib as ml
axis_min = min(FPR[0],FNR[-1])
fig,ax = plt.subplots()
plt.plot(FPR,FNR)
plt.yscale('log')
plt.xscale('log')
plt.xlabel('False Positive Rate(%)')
plt.ylabel('False Negative Rate(%)')
plt.title('DET curve')
ticks_to_use = [0.2,0.03,0.04,0.06,0.1,0.2,0.5,1]
ax.get_xaxis().set_major_formatter(ml.ticker.ScalarFormatter())
ax.get_yaxis().set_major_formatter(ml.ticker.ScalarFormatter())
ax.set_xticks(ticks_to_use)
ax.set_yticks(ticks_to_use)
#axis([0.001,50,0.001,50])

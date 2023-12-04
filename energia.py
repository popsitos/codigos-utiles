#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 13:21:26 2023

@author: solcanale
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
##voy a hacer los graficos de energia de foldx de las mutantes elegidas
m="/home/solcanale/calculos nuevos con alphafold/resultados pop y foldx/FOLDX/Rank1/Table-all"

df=pd.read_csv(m,header=0)
df=df.loc[:, (df != 0).any(axis=0)]
mutantes=["TA173I","AA293P","SA243E","SA98E","NA279S","QA247E","DA106N","DA130E","EA96S"]

def barras(mutante,save,nombre,label):
    subset = df[df["mutant"] == mutante]
    
    y=list(subset.values)[0][3:]

    fig, ax = plt.subplots()
    
    energia=list(subset.columns)[3:]
    x=np.arange(len(energia))
    for xc in x:
        plt.axvline(xc,color="black",alpha=0.3,linestyle='dotted')
        
    colores=sns.color_palette("rainbow",16).as_hex()
    
    for i in range(len(energia)):
        ax.bar(x[i], y[i],color=colores[i],label=energia[i])
        
    ax.set_ylabel("kcal/mol",rotation=90,fontsize=15)
    plt.axhline(y=0,color="black")
    ax.set_title(mutante,fontsize=20,y=1.05)
    plt.xticks(x, rotation=90,fontsize=12) 
    #plt.xticks([])
    ax.spines[['top',"right"]].set_visible(False)
    if label:
        ax.legend(bbox_to_anchor=(1.08, 1),fontsize=14)



    if save==True:    
        plt.savefig(nombre, transparent=True,bbox_inches='tight',dpi=500)
    plt.show()
    handles,labels = ax.get_legend_handles_labels()



  
barras("HA218E",True,"HA218E.png",True) #este sale con las labels
for mutante in mutantes:
    nombre=mutante+".png"
    barras(mutante,True,nombre,False)

